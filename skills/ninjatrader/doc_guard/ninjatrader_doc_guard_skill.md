# NinjaTrader Doc Guard Skill

## Purpose
Protéger contre l'hallucination d'API NinjaScript en validant que chaque méthode, propriété, et type utilisé existe dans la documentation officielle de NinjaTrader.

## Trigger
Ce skill doit être invoqué avant tout génération de code NinjaScript. Il vérifie la conformité des règles techniques avec les APIs disponibles.

## Inputs
- `RULES_SPEC.md`: Spécification technique de l'indicateur
- `platform_docs_url`: URL vers la documentation NinjaTrader (défaut: https://ninjatrader.com/support/helpGuides/nt8/)

## Outputs
- `NINJATRADER_DOCS_CHECKED.md`: Rapport de validation contenant:
  - Liste des méthodes/propriétés utilisées
  - Statut de validation pour chaque élément
  - Alternatives suggérées pour les éléments non trouvés
  - Recommandations d'implémentation

## Process

### 1. Collecte des API candidates
Extraire de RULES_SPEC.md:
- Méthodes NinjaScript demandées (ex: `OnBarUpdate()`, `Plot()`)
- Propriétés (ex: `Close[]`, `High[]`, `Volume[]`)
- Indicateurs intégrés (ex: `SMA()`, `RSI()`, `MACD()`)
- Types de données NinjaScript (ex: `BarsArray`, `Instrument`)

### 2. Validation documentaire
Pour chaque candidat:
- Rechercher dans la doc NinjaTrader officielle
- Vérifier la signature exacte (paramètres, types de retour)
- Vérifier la version de NinjaTrader requise (NT7 vs NT8 vs NT9)

### 3. Différences NinjaTrader à vérifier
- NT8 vs NT9: Changements majeurs dans l'API
- Indicateurs personnalisés: Doivent hériter de `Indicator`
- Méthodes d'événement: `OnBarUpdate()`, `OnRender()`, `OnStateChange()`
- Accès aux données: `BarsArray[]`, `GetCurrent()`, `Backtest` vs Live

### 4. Génération du rapport
Pour chaque élément:
- **VALID**: Existe et signature correcte
- **INVALID**: N'existe pas dans NinjaTrader
- **DEPRECATED**: Fonctionne mais marqué comme obsolète
- **VERSION**: Version NinjaTrader requise

## Validation
- Chaque méthode/propriété doit exister dans NinjaTrader
- Aucune méthode .NET non disponible en NinjaScript
- La version requise doit être documentée

## Example
```
Input: RULES_SPEC utilise SMA(), OnBarUpdate, Close
Output:
- SMA(): VALID (built-in indicator)
- OnBarUpdate(): VALID (NT8+)
- Close: VALID (BarsArray[0].Close)
- BarsArray: VALID (NT8+)
- Plot(): VALID (NT8+ with rendering)
```