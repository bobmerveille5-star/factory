# MT5 Review Skill

## Purpose
Reviewer et valider le code MQL5 généré pour un indicateur de trading, identifiant les problèmes techniques, les non-conformités, et les opportunités d'amélioration.

## Trigger
Ce skill doit être invoqué après `mt5_indicator_codegen_skill`. Il produit le MT5_REVIEW_REPORT.md.

## Inputs
- Fichier source `...mq5` généré
- `RULES_SPEC.md`: Spécification technique originale
- `MT5_DOCS_CHECKED.md`: Validation des APIs
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- `MT5_REVIEW_REPORT.md`: Rapport de revue contenant:
  - Statut global (APPROVED / NEEDS_REVISION / REJECTED)
  - Problèmes bloquants identifiés
  - Warnings et suggestions
  - Conformité avec les TEST_CASES
  - Score de qualité

## Process

### 1. Analyse syntaxique
- Vérifier que le code compile dans MetaEditor
- Identifier les erreurs de syntaxe
- Vérifier les types et conversions

### 2. Vérification de conformité
Pour chaque règle de RULES_SPEC:
- Le paramètre est-il correctement implémenté?
- La logique de calcul est-elle conforme?
- Les border cases sont-ils gérés?

### 3. Validation des APIs
- Aucune fonction INVALID utilisée
- Les handles sont correctement libérés
- Les buffers sont correctement dimensionnés

### 4. Vérification des tests
Pour chaque TEST_CASE:
- Le code permet-il d'implémenter le test?
- Les données nécessaires sont-elles disponibles?
- Les outputs sont-ils correctes?

### 5. Analyse qualité
- Conventions de nommage respectées?
- Code factorisé ou duplication?
- Gestion des erreurs présente?
- Performance acceptable?

### 6. Génération du rapport
Structurer selon:
```
# MT5 Review Report - [INDICATEUR]

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
- Syntaxe: [X]
- Conformité: [X]
- Performance: [X]
- Maintenabilité: [X]
```

## Validation
- Chaque TEST_CASE doit être vérifié
- Au moins un problème doit être identifié (sinon le skill est trop faible)
- Les suggestions doivent être actionnables

## Example
```
Input: Code swing highs généré
Output:
- B-001: Handle non libéré (OnDeinit manquant)
- W-001: swingPeriod > bars disponibles non géré
- TF-001: OK - calcul implémenté
- TL-001: FAIL - pas de gestion données manquantes
- Score: 75/100
```