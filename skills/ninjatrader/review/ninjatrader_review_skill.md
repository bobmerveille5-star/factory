# NinjaTrader Review Skill

## Purpose
Reviewer et valider le code NinjaScript généré pour un indicateur NinjaTrader, identifiant les problèmes techniques, les non-conformités, et les opportunités d'amélioration.

## Trigger
Ce skill doit être invoqué après `ninjatrader_indicator_codegen_skill`. Il produit le NINJATRADER_REVIEW_REPORT.md.

## Inputs
- Fichier source `...cs` généré
- `RULES_SPEC.md`: Spécification technique originale
- `NINJATRADER_DOCS_CHECKED.md`: Validation des APIs
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- `NINJATRADER_REVIEW_REPORT.md`: Rapport de revue contenant:
  - Statut global (APPROVED / NEEDS_REVISION / REJECTED)
  - Problèmes bloquants identifiés
  - Warnings et suggestions
  - Conformité avec les TEST_CASES
  - Score de qualité

## Process

### 1. Analyse syntaxique
- Vérifier que le code compile dans NinjaTrader
- Valider la structure de classe NinjaScript
- Vérifier les types et conversions C#

### 2. Vérification de conformité
Pour chaque règle de RULES_SPEC:
- Le paramètre est-il correctement implémenté avec [Parameter]?
- La logique de calcul est-elle conforme?
- Les border cases sont-ils gérés?

### 3. Validation des APIs NinjaTrader
- Aucune méthode INVALID utilisée
- Les méthodes [Output] sont correctement déclarées
- OnStateChange/OnBarUpdate implémentés correctement

### 4. Vérification du cycle de vie
- State.Configure: Configuration des paramètres
- State.DataLoaded: Préparation des données
- OnBarUpdate: Calculs par barre
- Disposal: Nettoyage des ressources

### 5. Vérification des tests
Pour chaque TEST_CASE:
- Le code permet-il d'implémenter le test?
- Les outputs sont-ils déclarés correctement?

### 6. Analyse qualité
- Conventions C# respectées?
- Documentation XML présente?
- Gestion des erreurs?
- Performance acceptable?

### 7. Génération du rapport
Structurer selon:
```
# NinjaTrader Review Report - [INDICATEUR]

## Statut global
[APPROVED / NEEDS_REVISION / REJECTED]

## Problèmes bloquants
### B-001: [Titre]
- Problème: [description]
- Correction: [suggestion]

## Warnings
### W-001: [Titre]
- Description: [description]
- Suggestion: [suggestion]

## Conformité TEST_CASES
| Test | Statut | Notes |
|------|--------|-------|
| TF-001 | OK/FAIL | ... |

## Score de qualité
[X/100]
```

## Validation
- Chaque TEST_CASE doit être vérifié
- Au moins un problème doit être identifié
- Les suggestions doivent être actionnables
- Version NinjaTrader (NT8/NT9) documentée

## Example
```
Input: Code swing highs NinjaTrader généré
Output:
- B-001: OnBarUpdate utilise BarsArray[1] sans vérification
- W-001: [Output] manquant pour swingLow
- TF-001: OK - calcul implémenté
- Score: 75/100
```