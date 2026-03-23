# Architecture Skill

## Purpose
Définir l'architecture technique complète pour l'implémentation multi-plateforme d'un indicateur de trading.

## Trigger
Ce skill doit être invoqué après `rules_formalizer_skill` et `test_design_skill`. Il produit l'ARCHITECTURE.md qui guide la génération de code.

## Inputs
- `RULES_SPEC.md`: Spécification technique détaillée
- `TEST_CASES.md`: Cas de test définissant les critères de succès

## Outputs
- `ARCHITECTURE.md`: Documentation architecturale contenant:
  - Schéma de données (inputs, outputs, états)
  - Architecture algorithmique (flow, étapes de calcul)
  - Découpage en modules/fonctions
  - Points d'extension identifiés
  - Contraintes techniques par plateforme
  - Stratégie de mise en cache des calculs lourds

## Process

### 1. Analyse des flux de données
- Identifier les entrées (prix, indicateurs, paramètres)
- Identifier les transformations intermédiaires
- Identifier les sorties (valeurs, visuel)
- Cartographier les dépendances de calcul

### 2. Conception algorithmique
Définir:
- Ordre des calculs (qu'est-ce qui doit être calculé en premier)
- Partitionnement (quels calculs peuvent être parallélisés)
- Périmètre temporel ( Rolling window, indicateur complet)
- Stratégie de gestion des données manquantes

### 3. Découpage en modules
Pour chaque plateforme, définir:
- **Module principal**: Classe/fichier central
- **Module données**: Accès aux prix, normalisation
- **Module calcul**: Logique des indicateurs
- **Module rendu**: Affichage (plot, lignes, zones)
- **Module paramètres**: Gestion de la configuration

### 4. Identification des points d'extension
- Paramètres additionnels futurs
- Indicateurs可选
- Signaux additionnels
- Personnalisation visuelle

### 5. Contraintes par plateforme
Documenter pour chaque plateforme:
- Limites de performances (calcul par barre)
- Contraintes mémoire
- Limites d'affichage (nombre de plots, labels)
- Différences architecturales MT5/MT4/Pine/NinjaTrader

### 6. Génération ARCHITECTURE.md
Structurer selon le template:
```
# Architecture - [NOM]

## Schéma de données
### Entrées
- [Input 1]: Type, source,频率

### Sorties
- [Output 1]: Type, destination

## Architecture algorithmique
### Flux principal
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

### Optimisations
- [Stratégie 1]
- [Stratégie 2]

## Découpage par plateforme

### MetaTrader 5
- Fichier principal: `...mq5`
- Modules: [...]

### MetaTrader 4
- Fichier principal: `...mq4`
- Modules: [...]

### Pine Script
- Fichier principal: `...pine`
- Modules: [...]

### NinjaTrader
- Fichier principal: `...cs`
- Modules: [...]

## Points d'extension
- [Extension 1]
- [Extension 2]
```

## Validation
- L'architecture doit permettre d'implémenter tous les TEST_CASES
- Chaque plateforme doit avoir une stratégie claire
- Les dépendances entre modules doivent être minimales

## Example
```
Input: RULES_SPEC pour swing highs, TEST_CASES vérifiant précision des pics
Output: ARCHITECTURE avec:
- Buffer circulaire pour historique
- Calcul incrémental vs recomplet
- Comparaison O(n) pour trouver max/min
- Limite de lookback configurable
```