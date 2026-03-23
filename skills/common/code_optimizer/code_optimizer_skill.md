# Code Optimizer Skill

## Purpose
Optimiser automatiquement le code généré pour les indicateurs de trading, améliorer les performances, réduire la mémoire, et appliquer les meilleures pratiques.

## Trigger
Ce skill est invoqué après `indicator_codegen` pour optimiser le code avant review.

## Inputs
- Code source généré (fichier .mq5, .mq4, .pine, .cs)
- `RULES_SPEC.md`: Spécification technique
- `ARCHITECTURE.md`: Architecture
- Contrainte de performance (optionnel)

## Outputs
- Code optimisé
- `OPTIMIZATION_REPORT.md`: Rapport des optimisations appliquées

## Process

### 1. Analyse du code
- Identifier les calculs redondants
- Détecter les allocations mémoire inutiles
- Trouver les boucles non optimisées
- Vérifier l'utilisation des buffers

### 2. Optimisations de performance
**Calculs:**
- Mise en cache des indicateurs
- Calcul incrémental vs complet
- Réduction des appels de fonctions
- Utilisation de buffers circulaires

**Mémoire:**
- Réutilisation des tableaux
- Limitation de la taille des buffers
- Libération des ressources

### 3. Optimisations spécifiques par plateforme

**MQL5:**
- Utilisation des handles d'indicateurs
- Reset des buffers avec EMPTY_VALUE
- Gestion des barres manquantes

**MQL4:**
- IndicatorCounted() optimisé
- Limitation à 8 buffers
- Accès direct aux prix

**Pine Script:**
- var pour variables persistantes
- Limiter security()
- max_bars_back approprié

**NinjaTrader:**
- Réutilisation des DataSeries
- OnBarUpdate optimisé
- Gestion d'état efficace

### 4. Génération OPTIMIZATION_REPORT
```markdown
# Optimization Report - [INDICATEUR]

## Métriques avant
- Temps de calcul: X ms/bar
- Mémoire: Y KB

## Métriques après
- Temps de calcul: X ms/bar (-Y%)
- Mémoire: Y KB (-Y%)

## Optimisations appliquées
### 1. [Nom]
- Description: [détail]
- Impact: [performance]

### 2. [Nom]
- Description: [détail]
- Impact: [performance]

## Score d'optimisation
[85/100]
```

## Validation
- Le code optimisé doit fonctionner identique
- Les performances doivent être améliorées
- Aucune régression fonctionnelle

## Example
```
Input: Code avec recalcul complet à chaque barre
Output:
- Optimisation: Buffer circulaire pour historique
- Impact: -60% temps de calcul
- Code refactorisé avec缓存
```