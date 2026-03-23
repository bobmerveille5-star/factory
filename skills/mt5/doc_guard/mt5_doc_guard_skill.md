# MT5 Doc Guard Skill

## Purpose
Protéger contre l'hallucination d'API MQL5 en validant que chaque fonction, classe, et constante utilisée existe dans la documentation officielle de MetaTrader 5.

## Trigger
Ce skill doit être invoqué avant tout génération de code MQL5. Il vérifie la conformité des règles techniques (RULES_SPEC.md) avec les APIs disponibles.

## Inputs
- `RULES_SPEC.md`: Spécification technique de l'indicateur
- `platform_docs_url`: URL vers la documentation MQL5 (défaut: https://www.mql5.com/en/docs)

## Outputs
- `MT5_DOCS_CHECKED.md`: Rapport de validation contenant:
  - Liste des fonctions/classes utilisées
  - Statut de validation pour chaque élément
  - Alternatives suggérées pour les éléments non trouvés
  - Recommandations d'implémentation

## Process

### 1. Collecte des API candidates
Extraire de RULES_SPEC.md:
- Fonctions demandées (ex: `iMA`, `iRSI`, `CopyRates`)
- Classes demandées (ex: `CTrade`, `CNamedPipe`)
- Constantes demandées (ex: `MODE_EMA`, `PRICE_CLOSE`)
- Types personnalisés demandés

### 2. Validation documentaire
Pour chaque candidat:
- Rechercher dans la doc MQL5 officielle
- Vérifier la signature exacte (paramètres, types de retour)
- Vérifier la période de disponibilité (certains indicateurs ont changé entre versions)

### 3. Génération du rapport
Pour chaque élément:
- **VALID**: Existe et signature correcte
- **INVALID**: N'existe pas ou signature différente
- **DEPRECATED**: Existe mais marqué comme obsolète
- **PARTIAL**: Existe mais nécessite vérification manuelle

### 4. Suggestions Alternatives
Pour les INVALID:
- Proposer l'équivalent fonctionnel
- Proposer la solution de contournement documentée

## Validation
- Chaque fonction utilisée dans le futur code doit être marquée VALID ou DEPRECATED
- Aucune marque INVALID sans alternative suggérée

## Example
```
Input: RULES_SPEC utilise iRSI, CopyRates, MODE_EMA
Output:
- iRSI: VALID (exist in indicators.mqh)
- CopyRates: VALID (exist in TerminalInfoInteger)
- MODE_EMA: INVALID (does not exist, use MODE_SMA with EMA calculation)
  Suggestion: Utiliser iMA avec MODE_SMA et calculer EMA manuellement
```