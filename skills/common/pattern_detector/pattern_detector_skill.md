# Pattern Detector Skill

## Purpose
Détecter automatiquement les patterns graphiques classiques (supports/résistances, figures chartistes, séquences de prix) dans les données de prix et générer des signals basés sur ces patterns.

## Trigger
Ce skill est invoqué quand l'utilisateur veut détecter des patterns dans les prix ou quand il veut un indicateur qui détecte des figures chartistes.

## Inputs
- Données de prix (OHLCV) ou indicateur existant
- Types de patterns à détecter (optionnel)
- Sensibilité (optionnel)

## Outputs
- `PATTERNS_DETECTED.md`: Rapport de détection contenant:
  - Patterns trouvés avec coordonnées
  - Fiabilité de chaque pattern
  - Signaux générés
  - Code pour chaque plateforme

## Process

### 1. Définition des patterns supportés
**Patterns de prix:**
- Support/Resistance (horizontal, trend line)
- Double Top/Bottom
- Triple Top/Bottom
- Head and Shoulders
- Triangle (ascending, descending, symmetric)
- Wedge (rising, falling)
- Flag et Pennant
- Round Bottom/Top

**Patterns de chandelier:**
- Doji
- Hammer/Hanging Man
- Engulfing
- Morning/Evening Star
- Piercing Line

### 2. Algorithmes de détection
Pour chaque pattern:
- Identification des points clés ( highs, lows)
- Vérification des conditions géométriques
- Calcul du score de fiabilité

### 3. Génération des signals
Pour chaque pattern détecté:
- Type: BREAKOUT, REVERSAL, CONTINUATION
- Direction: BUY, SELL
- Confidence: HIGH, MEDIUM, LOW

### 4. Implémentation par plateforme
Générer le code en respectant les limites de chaque plateforme.

## Output Example
```markdown
# Pattern Detection Report

## Patterns Détectés

### P-001: Double Top
- Position: Bar 1450-1480
- Résistance: 1.2450
- Targets: 1.2300, 1.2200
- Fiabilité: 85%
- Signal: SELL

### P-002: Support Horizontal  
- Position: Bar 800-1200
- Support: 1.1800
- Touches: 5
- Fiabilité: 92%

## Signaux
| Pattern | Type | Direction | Confidence |
|---------|------|-----------|-------------|
| Double Top | REVERSAL | SELL | HIGH |
```

## Validation
- Chaque pattern doit avoir une fiabilité documentée
- Les faux positifs doivent être minimisés
- Le code doit être performant (< 5ms par détection)

## Example
```
Input: Prix EURUSD H4, détecter double top
Output: Double top détecté à 1.2450, fiabilité 85%, signal SELL
```