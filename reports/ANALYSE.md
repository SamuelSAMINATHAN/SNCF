# 📊 Rapport d'Analyse : Fréquentation des Gares SNCF 2015-2023

## Résumé Exécutif
Cette analyse porte sur l'évolution de la fréquentation des gares SNCF entre 2015 et 2023, avec un focus particulier sur l'impact de la pandémie COVID-19 et la reprise qui a suivi.

## 🎯 Objectifs de l'Analyse
1. Identifier des profils types de gares selon leur fréquentation
2. Évaluer l'impact de la crise COVID-19 sur le trafic ferroviaire
3. Analyser les disparités régionales dans la reprise post-COVID
4. Fournir des insights pour l'optimisation du réseau

## 📈 Méthodologie
1. **Préparation des données**
   - Nettoyage et standardisation des données brutes
   - Calcul des métriques d'évolution
   - Fusion avec les données de géolocalisation

2. **Segmentation des gares**
   - Application d'un clustering K-means
   - Analyse en composantes principales (PCA)
   - Caractérisation des clusters

3. **Analyse temporelle**
   - Étude des tendances pré-COVID (2015-2019)
   - Évaluation de l'impact COVID (2020)
   - Analyse de la reprise (2021-2023)

## 🔍 Résultats Principaux

### 1. Segmentation des Gares
- **Cluster 1** : Grandes gares urbaines
  - Fort trafic (>10M voyageurs/an)
  - Impact COVID important
  - Reprise progressive

- **Cluster 2** : Gares moyennes régionales
  - Trafic modéré (1-10M voyageurs/an)
  - Impact COVID modéré
  - Bonne reprise

- **Cluster 3** : Petites gares rurales
  - Trafic faible (<1M voyageurs/an)
  - Impact COVID limité
  - Maintien du trafic

- **Cluster 4** : Gares touristiques
  - Trafic saisonnier
  - Impact COVID très fort
  - Reprise variable

### 2. Impact COVID-19
- Baisse moyenne du trafic : -45% en 2020
- Impact plus marqué dans les zones touristiques
- Résilience des gares rurales

### 3. Reprise Post-COVID
- 75% des gares ont retrouvé leur niveau de 2019
- Disparités régionales importantes
- Nouvelles tendances de mobilité

## 📍 Analyse Géographique
1. **Zones urbaines**
   - Concentration du trafic
   - Forte sensibilité aux crises
   - Reprise rapide

2. **Zones rurales**
   - Trafic stable
   - Résilience aux crises
   - Service public essentiel

3. **Zones touristiques**
   - Forte saisonnalité
   - Vulnérabilité aux restrictions
   - Reprise dépendante du tourisme

## 💡 Recommandations
1. **Adaptation du service**
   - Ajustement des fréquences selon les profils
   - Optimisation des connexions
   - Services spécifiques par cluster

2. **Résilience**
   - Plans de continuité adaptés
   - Diversification des services
   - Flexibilité opérationnelle

3. **Innovation**
   - Solutions digitales
   - Services multimodaux
   - Expérience voyageur personnalisée

## 📊 Visualisations Clés
Les visualisations détaillées sont disponibles dans le dossier `reports/figures/` :
- Cartes de clusters
- Évolutions temporelles
- Analyses d'impact
- Comparaisons régionales

## 📝 Annexes
- Détails méthodologiques dans les notebooks
- Sources des données
- Scripts d'analyse