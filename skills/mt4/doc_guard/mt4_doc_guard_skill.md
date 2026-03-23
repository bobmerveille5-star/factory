# MT4 Doc Guard Skill

## Purpose
Protéger contre l'hallucination d'API MQL4 en validant que chaque fonction, classe, et constante utilisée existe dans la documentation officielle de MetaTrader 4.

## Trigger
Ce skill doit être invoqué avant tout génération de code MQL4. Il vérifie la conformité des règles techniques avec les APIs disponibles.

## Inputs
- `RULES_SPEC.md`: Spécification technique de l'indicateur
- `platform_docs_url`: URL vers la documentation MQL4 (défaut: https://docs.mql4.com)

## Outputs
- `MT4_DOCS_CHECKED.md`: Rapport de validation contenant:
  - Liste des fonctions/classes utilisées
  - Statut de validation pour chaque élément
  - Alternatives suggérées pour les éléments non trouvés
  - Recommandations d'implémentation

## Process

### 1. Collecte des API candidates
Extraire de RULES_SPEC.md:
- Fonctions demandées (ex: `iMA`, `iRSI`, `iStochastic`)
- Constantes demandées (ex: `MODE_SMA`, `PRICE_CLOSE`)
- Types personnalisés demandés

### 2. Validation documentaire
Pour chaque candidat:
- Rechercher dans la doc MQL4 officielle
- Vérifier la signature exacte (paramètres, types de retour)
- **Attention aux différences MT4 vs MT5**: Certaines fonctions n'existent que dans MT5

### 3. Différences MT4/MT5 à vérifier
- MQL4 n'a pas de classes CTrade, CSymbolInfo
- MQL4 n'a pas `ArraySetAsSeries`
- MQL4 utilise `IndicatorCounted()` différemment
- MQL4 n'a pas de support natif des timelines multiples

### 4. Génération du rapport
Pour chaque élément:
- **VALID**: Existe et signature correcte
- **INVALID**: N'existe pas dans MQL4
- **DIFF_MT5**: Existe en MT5 mais pas en MT4
- **PARTIAL**: Existe mais nécessite vérification manuelle

## Validation
- Chaque fonction должна существовать в MQL4
- Aucune fonction MT5-only ne doit être utilisée

## Example
```
Input: RULES_SPEC utilise iRSI, CopyRates, CTrade
Output:
- iRSI: VALID (exist in indicators.mq4)
- CopyRates: INVALID (MQL4 uses iLow, iHigh instead)
  Suggestion: Utiliser iCopyLow et iCopyHigh
- CTrade: DIFF_MT5 (class does not exist in MQL4)
  Suggestion: Use OrderSend() directly
```