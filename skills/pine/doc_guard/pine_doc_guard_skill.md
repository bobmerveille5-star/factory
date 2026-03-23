# Pine Doc Guard Skill

## Purpose
Protéger contre l'hallucination d'API Pine Script en validant que chaque fonction, variable système, et constante utilisée existe dans la documentation officielle de TradingView.

## Trigger
Ce skill doit être invoqué avant tout génération de code Pine Script. Il vérifie la conformité des règles techniques avec les APIs disponibles.

## Inputs
- `RULES_SPEC.md`: Spécification technique de l'indicateur
- `platform_docs_url`: URL vers la documentation Pine (défaut: https://www.tradingview.com/pine-script-docs/)

## Outputs
- `PINE_DOCS_CHECKED.md`: Rapport de validation contenant:
  - Liste des fonctions/utilisations utilisées
  - Statut de validation pour chaque élément
  - Alternatives suggérées pour les éléments non trouvés
  - Recommandations d'implémentation

## Process

### 1. Collecte des API candidates
Extraire de RULES_SPEC.md:
- Fonctions Pine demandées (ex: `ta.sma()`, `ta.rsi()`, `plot()`)
- Variables système (ex: `time`, `close`, `volume`, `bar_index`)
- Paramètres de plot (ex: `color`, `linewidth`, `style`)
- Fonctions de stratégie (ex: `strategy.entry()`, `strategy.order()`)

### 2. Validation documentaire
Pour chaque candidat:
- Rechercher dans la doc Pine Script officielle
- Vérifier la version Pine requise (v1 à v5)
- Vérifier les paramètres exacts et types
- **Attention aux versions**: Certaines fonctions ont changé entre v3, v4, v5

### 3. Différences de version Pine à vérifier
- v5: Support natif des tableaux et matrices
- v4: `var` keyword, improved security
- v3: Limitaciones significativas
- Types de retour différents selon version

### 4. Génération du rapport
Pour chaque élément:
- **VALID**: Existe avec la version minimale requise
- **DEPRECATED**: Fonctionne mais recommandée autrement
- **INVALID**: N'existe pas dans les versions supportées
- **VERSION**: Version minimale requise

## Validation
- Chaque fonction должна существовать dans Pine
- La version minimale doit être documentée
- Aucune fonction "future" qui n'existe pas encore

## Example
```
Input: RULES_SPEC utilise ta.rsi(), plot(), strategy.entry
Output:
- ta.rsi(): VALID (Pine v2+)
- plot(): VALID (Pine v1+)
- strategy.entry: VALID (Pine v2+)
- ta.vwap(): VERSION (Pine v4+, vérifiercompatibilité)
```