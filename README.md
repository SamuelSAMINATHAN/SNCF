# Analyse des Gares SNCF : Segmentation et Impact COVID-19

## 📊 Vue d'ensemble
Ce projet analyse les données de fréquentation des gares SNCF entre 2015 et 2023, avec un focus particulier sur l'impact de la pandémie COVID-19 et l'identification de profils types de gares.

### 🎯 Objectifs
- Segmenter les gares selon leurs profils de fréquentation
- Analyser l'évolution temporelle du trafic voyageurs
- Évaluer l'impact du COVID-19 sur différents types de gares
- Identifier les tendances de reprise post-pandémie

### 💡 Insights Clés
- Identification de profils types de gares (clusters)
- Analyse de l'impact COVID par segment
- Visualisation géographique des tendances
- Dashboard interactif pour l'exploration des données

## 🔧 Structure du Projet
```
sncf-gare-analysis/
├── data/
│   ├── raw/                  # Données brutes
│   ├── processed/            # Données nettoyées
│   └── external/             # Données externes (géolocalisation)
├── notebooks/
│   ├── exploration_donnees.ipynb    # EDA et nettoyage
│   ├── clustering_gares.ipynb       # Segmentation
│   ├── evolution_trafic_region.ipynb # Analyse temporelle
│   └── carte.ipynb                  # Visualisation géographique
├── dashboard/
│   └── app.py               # Application Streamlit
└── requirements.txt         # Dépendances Python
```

## 🛠️ Installation
```bash
# Cloner le repository
git clone [URL_DU_REPO]

# Installer les dépendances
pip install -r requirements.txt

# Lancer le dashboard
cd dashboard
streamlit run app.py
```

## 📈 Méthodologie
1. **Préparation des données**
   - Nettoyage et standardisation
   - Calcul des métriques d'évolution

2. **Analyse exploratoire**
   - Tendances temporelles
   - Distribution des fréquentations
   - Corrélations géographiques

3. **Segmentation**
   - Clustering K-means
   - Validation par métriques (silhouette, elbow)
   - Caractérisation des clusters

4. **Visualisation**
   - Cartes interactives
   - Graphiques temporels
   - Dashboard Streamlit

## 📊 Résultats Principaux
*(À compléter avec les résultats spécifiques de l'analyse)*

## 🔍 Documentation
- Les notebooks sont auto-documentés avec des explications détaillées
- Le dashboard inclut des tooltips explicatifs
- Chaque étape de l'analyse est justifiée et commentée

## 📝 License
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## 👥 Contact
Pour toute question ou suggestion d'amélioration, n'hésitez pas à ouvrir une issue ou à me contacter directement.# SNCF
