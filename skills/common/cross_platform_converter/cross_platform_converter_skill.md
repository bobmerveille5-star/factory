# Cross-Platform Converter Skill

## Purpose
Convertir automatiquement du code d'indicateur d'une plateforme vers une autre (MT5→MT4, Pine→MT5, etc.), en gérant les différences d'API et les limitations de chaque plateforme.

## Trigger
Ce skill est invoqué quand l'utilisateur veut porter un indicateur d'une plateforme vers une autre ou maintenir plusieurs versions.

## Inputs
- Code source (fichier .mq5, .mq4, .pine, .cs)
- Plateforme cible
- Options de conversion

## Outputs
- Code converti pour la plateforme cible
- `CONVERSION_REPORT.md`: Rapport de conversion contenant:
  - Équivalences utilisées
  - Avertissements
  - Limitations

## Process

### 1. Analyse du code source
- Parser la syntaxe source
- Extraire les fonctions utilisées
- Identifier les APIs spécifiques
- Détecter les patterns non supportés

### 2. Mapping des APIs
Pour chaque fonction:
- Trouver l'équivalente dans la plateforme cible
- Si pas d'équivalente, générer code custom
- Documenter les différences

### 3. Conversion syntaxe
**MQL5 → MQL4:**
- Classes CTrade → OrderSend()
- Handles → calculs directs
- ArraySetAsSeries → array indexing manuel

**Pine → MQL5:**
- ta.rsi() → iRSI()
- plot() → SetIndexBuffer()
- strategy.entry → Signaux manuels

**MQL5 → Pine:**
- iRSI() → ta.rsi()
- SetIndexBuffer → plot()
- CTrade → Non applicable (Pine = indicateur seul)

**NinjaTrader conversions:**
- Similar to above with .NET specifics

### 4. Génération CONVERSION_REPORT
```markdown
# Conversion Report: [INDICATEUR]

## Source → Cible
- Source: MT5
- Cible: Pine Script v5

## Équivalences
| Original | Équivalente | Notes |
|----------|-------------|-------|
| iRSI | ta.rsi() | OK |
| iMA(EMA) | ta.ema() | OK |
| CTrade | N/A | Pas de trading |

## Avertissements
- A-001: CTrade removed (Pine ne support pas le trading)
- A-002: Handle converted to inline calculation

## Limitations
- L-001: Max 3 plots (Pine limit)
- L-002: Pas de multi-devises
```

## Validation
- Code doit être syntaxiquement valide
- Fonctionnalité principale préservée
- Différences documentées

## Example
```
Input: RSI.mq5 (MT5)
Output: RSI.pine (Pine Script) + Conversion Report
```