# Multi-Timeframe Mapper Skill

## Purpose
Permettre à un indicateur de fonctionner automatiquement sur plusieurs timeframes, permettant l'analyse multi-timeframe (ex: RSI sur H1 avec confirmation H4).

## Trigger
Ce skill est invoqué quand l'utilisateur veut un indicateur qui utilise des données de multiples timeframes.

## Inputs
- Indicateur de base
- Timeframes cibles
- Mode de combinaison (overlay, confirmation, filter)

## Outputs
- `MTF_SPEC.md`: Spécification multi-timeframe contenant:
  - Configuration des timeframes
  - Logique de fusion
  - Code pour chaque plateforme

## Process

### 1. Définition des timeframes
Pour chaque timeframe:
- Timeframe source (M1, M5, M15, H1, H4, D1, etc.)
- Usage (signal, confirmation, filter)
- Décalage optionnel

### 2. Modes de combinaison
**Overlay:**
- Afficher indicateur de multiple timeframes sur même chart
- Ex: H1 + H4 + D1 sur graphique H1

**Confirmation:**
- Signal principal sur timeframe bas
- Confirmation sur timeframe haut
- Ex: BUY si RSI H1 & RSI H4

**Filter:**
- Timeframe haut filtre les signaux
- Ex: Trend EMA 200 sur D1 filtre signaux H1

### 3. Implémentation par plateforme

**MT5:**
- `iSecurity()` pour获取 other timeframes
- Attention aux handles et ressources

**MT4:**
- `iCustom()` avec变换
- Limité, peut être complexe

**Pine:**
- `security()` function native
- Facile et performant

**NinjaTrader:**
- `BarsArray` pour autres timeframes
- Requiert configuration

### 4. Génération MTF_SPEC
```markdown
# Multi-Timeframe Specification

## Configuration
| Timeframe | Usage | Décalage |
|----------|-------|----------|
| H1 | Signal principal | 0 |
| H4 | Confirmation | 0 |
| D1 | Filter trend | 0 |

## Logique
### Signal BUY
1. RSI(H1) &lt; 30
2. RSI(H4) &lt; 40 (confirmation)
3. EMA(D1) &gt; close (trend haussier)

### Signal SELL
1. RSI(H1) &gt; 70
2. RSI(H4) &gt; 60 (confirmation)
3. EMA(D1) &lt; close (trend baissier)

## Paramètres
| Param | Type | Description |
|-------|------|-------------|
| signalTF | enum | Timeframe du signal |
| confirmTF | enum | Timeframe de confirmation |
| filterTF | enum | Timeframe du filter |
```

## Validation
- Chaque timeframe doit être accessible
- Performance doit être acceptable
- Sync des données doit être correcte

## Example
```
Input: RSI avec confirmation H4
Output: Indicateur qui affiche RSI H1 avec signaux filtrés par RSI H4
```