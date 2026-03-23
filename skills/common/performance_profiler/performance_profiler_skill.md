# Performance Profiler Skill

## Purpose
Profiler et analyser les performances du code d'un indicateur, identifiant les goulots d'étranglement et suggérant des optimisations.

## Trigger
Ce skill est invoqué après `code_optimizer` ou quand l'utilisateur veut optimiser les performances.

## Inputs
- Code source de l'indicateur
- Contraintes de performance (optionnel)
- Données de test (optionnel)

## Outputs
- `PERFORMANCE_REPORT.md`: Rapport de profilage contenant:
  - Métriques de performance
  - Points lents identifiés
  - Recommandations d'optimisation
  - Code optimisé (optionnel)

## Process

### 1. Analyse statique du code
- Compter les opérations par barre
- Identifier les boucles
- Détecter les allocations mémoire
- Mapper les dépendances

### 2. Métriques collectées
- **Temps de calcul**: ms par barre
- **Mémoire**: KB utilisés
- **Appels de fonctions**: nombre par calcul
- **Complexité**: O(n), O(n²), etc.

### 3. Identification des problèmes
Pour chaque problème:
- Localisation (ligne, fonction)
- Impact (HIGH, MEDIUM, LOW)
- Cause racine

### 4. Recommandations
Proposer:
- Caching des résultats
- Calcul incrémental
- Réduction des allocations
- Utilisation de buffers circulaires

### 5. Génération PERFORMANCE_REPORT
```markdown
# Performance Report - [INDICATEUR]

## Métriques
- Temps moyen: 0.5ms/bar
- Temps max: 2.3ms/bar
- Mémoire: 128KB
- Complexité: O(n)

## Analyse par fonction

### OnCalculate
- Temps: 0.4ms/bar (80%)
- Appels: 5 fonctions
- Problème: Recalcul complet chaque barre

### CalculRSI
- Temps: 0.2ms/bar
- Problème: Accès mémoire non optimisé

## Optimisations suggérées

### O-001: Cache indicateurs
- Impact: -40% temps
- Implémentation: Stocker résultat previous

### O-002: Buffer circulaire
- Impact: -30% mémoire
- Implémentation: Utiliser buffer comme circulaire

## Recommandations
1. Implémenter cache pour RSI
2. Utiliser buffer circulaire pour historique
3. Réduire appels iCustom
```

## Validation
- Chaque métrique doit être mesurable
- Les recommendations doivent être actionnables
- Impact estimé doit être réaliste

## Example
```
Input: Code avec recalcul complet
Output: 
- Problèmes identifiés: 3
- Optimisations: 5 suggérées
- Gain potentiel: -50% temps
```