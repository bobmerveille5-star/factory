# Volume Analyzer Skill

## Purpose
Analyser le volume de trading pour identifier le Volume Weighted Average Price (VWAP), le Volume Profile, et les anomalies de volume.

## Trigger
Ce skill est invoqué quand l'utilisateur veut analyser le volume pour confirmer des signaux ou identifier des zones d'accumulation/distribution.

## Inputs
- Données de volume
- Configuration VWAP (session, reset)
- Configuration Volume Profile (bins, range)

## Outputs
- `VOLUME_ANALYSIS.md`: Rapport contenant:
  - VWAP par session
  - Points de contrôle (POC) du Volume Profile
  - Anomalies de volume
  - Signaux basés sur volume

## Process

### 1. VWAP (Volume Weighted Average Price)
- Calcul: Σ(Prix × Volume) / Σ(Volume)
- Par session: Daily, Weekly, Monthly
- Bandes: +1σ, +2σ, -1σ, -2σ

### 2. Volume Profile
- Diviser-range en bins horizontaux
- Identifier POC (Point of Control)
- Zones VA (Value Area 70%)
- Zones d'accumulation/distribution

### 3. Anomalies de volume
- Volume spike: Volume >> moyenne
- Volume collapse: Volume << moyenne
- Volume trend: Corrélation prix/volume

### 4. Signaux volume
- **VWAP Break**: Prix casse VWAP
- **POC Test**: Retour sur POC
- **Volume Spike**: Spike de volume

## Output Example
```markdown
# Volume Analysis

## VWAP
| Session | VWAP | +1σ | -1σ |
|---------|------|-----|-----|
| Daily | 1.2450 | 1.2500 | 1.2400 |
| Weekly | 1.2400 | 1.2550 | 1.2250 |

## Volume Profile
- POC: 1.2450 (25% du volume)
- VA High: 1.2500
- VA Low: 1.2400

## Anomalies
- Spike volume Bar 1450: 3x moyenne
- Trend volume: Positif (prix monte avec volume)

## Signaux
- VWAP Break BUY: Prix casse VWAP daily vers le haut
- POC Retest: Retour sur 1.2450 prévu
```

## Validation
- VWAP doit correspondre au calcul standard
- POC doit être dans la zone de prix la plus tradée
- Anomalies documentées avec contexte

## Example
```
Input: Volume EURUSD H1
Output: VWAP daily 1.2450, POC 1.2450, spike détecté bar 1450
```