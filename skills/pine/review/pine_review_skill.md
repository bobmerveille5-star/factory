# Pine Review Skill

## Purpose
Reviewer et valider le code Pine Script généré pour un indicateur TradingView, identifiant les problèmes techniques, les non-conformités, et les opportunités d'amélioration.

## Trigger
Ce skill doit être invoqué après `pine_indicator_codegen_skill`. Il produit le PINE_REVIEW_REPORT.md.

## Inputs
- Fichier source `...pine` généré
- `RULES_SPEC.md`: Spécification technique originale
- `PINE_DOCS_CHECKED.md`: Validation des APIs Pine
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- `PINE_REVIEW_REPORT.md`: Rapport de revue contenant:
  - Statut global (APPROVED / NEEDS_REVISION / REJECTED)
  - Problèmes bloquants identifiés
  - Warnings et suggestions
  - Conformité avec les TEST_CASES
  - Score de qualité

## Process

### 1. Analyse syntaxique
- Vérifier la syntaxe Pine Script v5
- Valider les types de variables
- Vérifier la version déclarée

### 2. Vérification de conformité
Pour chaque règle de RULES_SPEC:
- Le paramètre est-il correctement implémenté avec input.*()?
- La logique de calcul est-elle conforme?
- Les border cases sont-ils gérés?

### 3. Validation des APIs Pine
- Aucune fonction INVALID ou DEPRECATED utilisée
- Utilisation correcte de ta.* (fonctions techniques)
- Utilisation correcte des fonctions de plot

### 4. Vérification des bonnes pratiques
- Utilisation de var pour les variables persistantes
- Éviter les références futures
- Limiter l'utilisation de security()
- max_bars_back configuré si nécessaire

### 5. Vérification des limites Pine
- Limite de 30k lignes de code
- Limite de ressources (scripts par chart)
- Pas d'appels réseau directs

### 6. Vérification des tests
Pour chaque TEST_CASE:
- Le code permet-il d'implémenter le test?
- Les outputs sont-ils accessibles?

### 7. Génération du rapport
Structurer selon:
```
# Pine Review Report - [INDICATEUR]

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

## Example
```
Input: Code swing highs Pine généré
Output:
- B-001: Référence future détectée (ligne 42)
- W-001: security() utilisé sans cache
- TF-001: OK
- Score: 80/100
```