# Cross Platform Review Skill

## Purpose
Valider la cohérence et l'équivalence fonctionnelle des implémentations d'un indicateur de trading à travers toutes les plateformes supportées (MT5, MT4, Pine, NinjaTrader).

## Trigger
Ce skill doit être invoqué après tous les skills de review individuels (mt5_review, mt4_review, pine_review, ninjatrader_review). Il produit le CROSS_PLATFORM_REVIEW.md.

## Inputs
- `MT5_REVIEW_REPORT.md`: Rapport de revue MT5
- `MT4_REVIEW_REPORT.md`: Rapport de revue MT4
- `PINE_REVIEW_REPORT.md`: Rapport de revue Pine
- `NINJATRADER_REVIEW_REPORT.md`: Rapport de revue NinjaTrader
- `RULES_SPEC.md`: Spécification technique originale
- `TEST_CASES.md`: Cas de test globaux

## Outputs
- `CROSS_PLATFORM_REVIEW.md`: Rapport de revue multi-plateforme contenant:
  - Statut global de cohérence
  - Incohérences identifiées entre plateformes
  - Équivalences fonctionnelles validées
  - Recommandations d'harmonisation
  - Score de cohérence globale

## Process

### 1. Collecte des statuts
- Lire chaque rapport de revue individuel
- Extraire les statuts (APPROVED/NEED_REVISION/REJECTED)
- Identifier les problèmes communs

### 2. Analyse de cohérence fonctionnelle
Pour chaque fonctionnalité de RULES_SPEC:
- MT5 implémente-t-elle la même logique que Pine?
- Les résultats numériques sont-ils comparables?
- Les border cases sont-ils gérés pareillement?

### 3. Analyse des paramètres
Vérifier que les paramètres sont:
- Présents sur toutes les plateformes
- Mêmes noms/identiques
- Mêmes plages de valeurs
- Mêmes valeurs par défaut

### 4. Analyse des outputs
Vérifier que les outputs sont:
- Mêm type de données sur toutes les plateformes
- Mêm comportement visuel
- Mêmgranularité (par barre, par signal)

### 5. Identification des incohérences
Pour chaque divergence:
- Quelle plateforme est "référence"?
- Quelle correction est nécessaire?
- Impact sur les autres plateformes?

### 6. Génération du rapport
Structurer selon:
```
# Cross Platform Review - [INDICATEUR]

## Statut global de cohérence
[COHERENT / INCOHERENT]

## Résumé par plateforme
| Plateforme | Statut | Score |
|------------|--------|-------|
| MT5 | APPROVED | 85 |
| MT4 | NEED_REVISION | 70 |
| Pine | APPROVED | 80 |
| NinjaTrader | APPROVED | 75 |

## Cohérence fonctionnelle
### CF-001: [Fonctionnalité]
- MT5: [description]
- Pine: [description]
- Cohérent: [OUI/NON]
- Correction: [si nécessaire]

## Paramètres
| Paramètre | MT5 | MT4 | Pine | NT | Cohérent |
|-----------|-----|-----|------|-----|----------|
| period | 14 | 14 | 14 | 14 | OUI |
| method | EMA | EMA | SMA | EMA | NON |

## Incohérences identifiées
### I-001: [Titre]
- Plates-formes affectées: [MT5, Pine]
- Problème: [description]
- Correction: [suggestion]

## Recommandations
- [Recommandation 1]
- [Recommandation 2]

## Score de cohérence
[X/100]
```

## Validation
- Chaque plateforme doit être comparée aux autres
- Au moins une incohérence doit être identifiée (si tout est parfait, le skill est trop faible)
- Les corrections doivent être actionnables

## Example
```
Input: 4 rapports de review
Output:
- I-001: swingPeriod max = 100 en MT5, 50 en Pine
- I-002: Confirmation differente entre MT4 et NT
- CF-001: Calcul des swing highs coherent sur MT5/Pine/NT
- Score: 75/100
```