# Signal Generator Skill

## Purpose
Générer automatiquement des signaux de trading (BUY/SELL/NEUTRAL) depuis un ou plusieurs indicateurs, avec gestion des conditions, confirmation et alertes.

## Trigger
Ce skill est invoqué quand l'utilisateur veut créer un indicateur qui génère des signaux actionnables.

## Inputs
- Indicateur(s) source (RSI, MACD, MA, etc.)
- Conditions de signal
- Configuration des alertes

## Outputs
- `SIGNAL_SPEC.md`: Spécification des signaux contenant:
  - Définition précise des signaux BUY/SELL
  - Conditions de confirmation
  - Logique de filtrage
  - Configuration des alertes
  - Code pour chaque plateforme

## Process

### 1. Définition des signaux
Pour chaque signal:
- **Type**: CROSS, OVERBOUGHT, OVERSOLD, DIVERGENCE, CROSSOVER
- **Direction**: BUY, SELL
- **Indicateurs impliqués**: Liste des indicateurs
- **Conditions**: Logique booléenne

### 2. Conditions avancées
- **Signal primaire**: Condition principale
- **Confirmation**: Condition secondaire (filtre)
- **Filter trend**: Direction du trend (EMA 200)
- **Timeframe filter**: Confirmer sur timeframe supérieur

### 3. Gestion des alertes
- **Alerte**: Notification push/email
- **Repaint**:，是否Repeint (oui/non)
- **History**: Signaux passés visibles
- **Sound**: Son d'alerte optionnel

### 4. Implémentation par plateforme
Générer code avec:
- Notifications intégrées (MT5, Pine)
- Alerts (NinjaTrader)
- PlaySound (MT4)

## Output Example
```markdown
# Signal Specification

## Signaux

### BUY Signal
- Condition: RSI < 30 AND RSI crosses above 30
- Confirmation: Price > EMA(200)
- Filter: ADX > 25
- Repaint: Non
- Alert: Push notification + Sound

### SELL Signal
- Condition: RSI > 70 AND RSI crosses below 70
- Confirmation: Price < EMA(200)
- Filter: ADX > 25
- Repaint: Non
- Alert: Push notification + Sound

## Parameters
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| rsiPeriod | int | 14 | RSI period |
| oversold | int | 30 | Oversold level |
| overbought | int | 70 | Overbought level |
| useEMAConfirm | bool | true | Use EMA confirmation |
```

## Validation
- Chaque signal doit avoir une condition précise
- Les alerts doivent être configurables
- Repaint doit être documenté

## Example
```
Input: RSI avec conditions "buy when oversold, sell when overbought"
Output: Signal BUY quand RSI<30 et cross up, Signal SELL quand RSI>70 et cross down
```