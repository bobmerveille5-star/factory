# MT4 Review Skill

## Purpose
Reviewer et valider le code MQL4 généré pour un indicateur de trading, identifiant les problèmes techniques, les non-conformités, et les opportunités d'amélioration.

## Trigger
Ce skill doit être invoqué après `mt4_indicator_codegen_skill`. Il produit le MT4_REVIEW_REPORT.md.

## Inputs
- Fichier source `...mq4` généré
- `RULES_SPEC.md`: Spécification technique originale
- `MT4_DOCS_CHECKED.md`: Validation des APIs
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- `MT4_REVIEW_REPORT.md`: Rapport de revue contenant:
  - Statut global (APPROVED / NEEDS_REVISION / REJECTED)
  - Problèmes bloquants identifiés
  - Warnings et suggestions
  - Conformité avec les TEST_CASES
  - Score de qualité

## Process

### 1. Analyse syntaxique
- Vérifier que le code compile dans MetaEditor
- Identifier les erreurs de syntaxe MQL4
- Vérifier les types et conversions
- Attention aux différences avec MQL5

### 2. Vérification de conformité
Pour chaque règle de RULES_SPEC:
- Le paramètre est-il correctement implémenté?
- La logique de calcul est-elle conforme?
- Les border cases sont-ils gérés?

### 3. Validation des APIs MQL4
- Aucune fonction INVALID utilisée
- Aucune fonction MT5-only utilisée
- Les buffers (max 8) ne sont pas dépassés
- Les indicateurs utilisent les fonctions i* (iMA, iRSI, etc.)

### 4. Vérification des limites MT4
- Nombre de buffers ≤ 8
- IndicatorCounted() utilisé correctement
- Accès aux prix via iOpen, iHigh, iLow, iClose
- Arrays gérés manuellement (pas de ArraySetAsSeries)

### 5. Vérification des tests
Pour chaque TEST_CASE:
- Le code permet-il d'implémenter le test?
- Les données nécessaires sont-elles disponibles?
- Les outputs sont-ils correctes?

### 6. Analyse qualité
- Conventions de nommage respectées?
- Code factorisé ou duplication?
- Gestion des erreurs présente?
- Performance acceptable?

### 7. Génération du rapport
Structurer selon:
```
# MT4 Review Report - [INDICATEUR]

## Statut global
[APPROVED / NEEDS_REVISION / REJECTED]

## Problèmes bloquants
### B-001: [Titre]
- Fichier: [ligne]
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
- Au moins un problème doit être identifié (sinon le skill est trop faible)
- Les suggestions doivent être actionnables
- Compatibilité MT4 Build 600+ vérifiée

## Example
```
Input: Code swing highs généré
Output:
- B-001: ArraySetAsSeries utilisé (inexistant en MQL4)
- B-002: 9 buffers declarés (limite: 8)
- W-001: extern manquant pour paramètre
- Score: 65/100
```