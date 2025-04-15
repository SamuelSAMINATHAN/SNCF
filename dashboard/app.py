import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Analyse des Gares SNCF",
    page_icon="🚂",
    layout="wide"
)

# Fonction pour charger les données
@st.cache_data
def load_data():
    # Chargement des données avec clusters
    data_path = Path("../data/processed/gares_avec_clusters.csv")
    if data_path.exists():
        df = pd.read_csv(data_path)
    else:
        # Fallback sur les données sans clusters
        data_path = Path("../data/processed/frequentation-gares-clean.csv")
        df = pd.read_csv(data_path)
        # Ajout d'une colonne cluster par défaut
        df['cluster'] = 0
    
    # Calcul des métriques d'évolution si elles n'existent pas
    if 'var_2015_2023' not in df.columns:
        df['var_2015_2023'] = ((df['total_voyageurs_2023'] - df['total_voyageurs_2015']) / df['total_voyageurs_2015'] * 100).fillna(0)
    
    if 'impact_covid' not in df.columns:
        df['impact_covid'] = ((df['total_voyageurs_2020'] - df['total_voyageurs_2019']) / df['total_voyageurs_2019'] * 100).fillna(0)
        
    return df

# Fonction pour créer la carte des gares
def create_map(df, color_by='cluster'):
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    
    # Définition des palettes de couleurs
    cluster_colors = px.colors.qualitative.Set1
    
    # Normalisation pour les valeurs continues
    if color_by != 'cluster' and color_by in df.columns:
        vmin = df[color_by].min()
        vmax = df[color_by].max()
        norm = lambda x: (x - vmin) / (vmax - vmin) if vmax > vmin else 0
    
    for idx, row in df.iterrows():
        # Détermination de la couleur
        if color_by == 'cluster':
            color = cluster_colors[int(row[color_by]) % len(cluster_colors)]
        elif color_by in df.columns:
            # Utilisation d'une échelle de couleur pour les valeurs continues
            normalized = norm(row[color_by])
            color = f'#{int(255*(1-normalized)):02x}{int(255*normalized):02x}00'  # Rouge à vert
        else:
            color = 'blue'
        
        # Détermination du rayon en fonction de la fréquentation
        radius = np.log1p(row['total_voyageurs_2023']) / 2
        radius = max(5, min(15, radius))  # Limiter entre 5 et 15
        
        # Création du popup avec plus d'informations
        popup_html = f"""
        <b>{row['nom_de_la_gare']}</b><br>
        Voyageurs 2023: {row['total_voyageurs_2023']:,.0f}<br>
        Évolution 2015-2023: {row.get('var_2015_2023', 0):.1f}%<br>
        Impact COVID: {row.get('impact_covid', 0):.1f}%<br>
        Cluster: {int(row['cluster'])}
        """
        
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=radius,
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=row['nom_de_la_gare'],
            color=color,
            fill=True,
            fill_opacity=0.7
        ).add_to(m)
    
    return m

def main():
    st.title("🚂 Analyse des Gares SNCF")
    st.subheader("Exploration interactive des données de fréquentation")

    # Chargement des données
    try:
        df = load_data()
        
        # Sidebar pour les filtres
        st.sidebar.header("Filtres")
        
        # Sélection de l'année
        selected_year = st.sidebar.selectbox(
            "Année d'analyse",
            range(2023, 2014, -1)
        )
        
        # Sélection de la région
        regions = sorted(df['region'].unique())
        selected_region = st.sidebar.multiselect(
            "Régions",
            regions,
            default=[]
        )
        
        # Filtrage des données
        filtered_df = df
        if selected_region:
            filtered_df = filtered_df[filtered_df['region'].isin(selected_region)]

        # Layout principal
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📍 Carte des Gares")
            map_fig = create_map(filtered_df)
            folium_static(map_fig)
        
        with col2:
            st.subheader("📊 Top 10 des Gares")
            col_name = f'total_voyageurs_{selected_year}'
            top_10 = filtered_df.nlargest(10, col_name)
            
            fig = px.bar(
                top_10,
                x='nom_de_la_gare',
                y=col_name,
                title=f"Top 10 des gares les plus fréquentées en {selected_year}"
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
        
        # Analyse temporelle
        st.subheader("📈 Évolution du trafic")
        cols_years = [f'total_voyageurs_{year}' for year in range(2015, 2024)]
        evolution_df = filtered_df[['nom_de_la_gare'] + cols_years].melt(
            id_vars=['nom_de_la_gare'],
            var_name='année',
            value_name='voyageurs'
        )
        evolution_df['année'] = evolution_df['année'].str.extract('(\d{4})').astype(int)
        
        fig_evolution = px.line(
            evolution_df,
            x='année',
            y='voyageurs',
            color='nom_de_la_gare',
            title="Évolution du trafic voyageurs par gare"
        )
        st.plotly_chart(fig_evolution, use_container_width=True)
        
        # Impact COVID
        st.subheader("🦠 Impact COVID-19")
        covid_impact = filtered_df.copy()
        covid_impact['impact_covid'] = (
            (covid_impact['total_voyageurs_2020'] - covid_impact['total_voyageurs_2019']) 
            / covid_impact['total_voyageurs_2019'] * 100
        )
        covid_impact['reprise_2023'] = (
            (covid_impact['total_voyageurs_2023'] - covid_impact['total_voyageurs_2019']) 
            / covid_impact['total_voyageurs_2019'] * 100
        )
        
        col3, col4 = st.columns(2)
        
        with col3:
            fig_covid = px.histogram(
                covid_impact,
                x='impact_covid',
                title="Distribution de l'impact COVID (2020 vs 2019)"
            )
            st.plotly_chart(fig_covid, use_container_width=True)
        
        with col4:
            fig_reprise = px.histogram(
                covid_impact,
                x='reprise_2023',
                title="Distribution de la reprise (2023 vs 2019)"
            )
            st.plotly_chart(fig_reprise, use_container_width=True)
            
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {str(e)}")
        st.info("Assurez-vous que le fichier de données est présent dans le dossier approprié.")

if __name__ == "__main__":
    main()