# Docs Auto-Generator Skill

## Purpose
Générer automatiquement une documentation utilisateur complète pour un indicateur de trading, incluant guides, références de paramètres, et exemples.

## Trigger
Ce skill est invoqué en Phase 6 (Delivery) pour générer la documentation finale.

## Inputs
- `RULES_SPEC.md`: Spécification technique
- `ARCHITECTURE.md`: Architecture
- Code source
- Exemples d'utilisation

## Outputs
- `USER_GUIDE.md`: Guide utilisateur complet
- `PARAMETERS_REFERENCE.md`: Référence des paramètres
- `EXAMPLES.md`: Exemples d'utilisation avec screenshots
- `QUICK_START.md`: Guide de démarrage rapide

## Process

### 1. Analyse du code
- Extraire les paramètres configurables
- Identifier les outputs visuels
- Mapper les comportements

### 2. Génération USER_GUIDE
Structurer:
- Introduction et résumé
- Installation pas à pas
- Configuration des paramètres
- Interprétation des signaux
- Conseils d'utilisation
- Limites et avertissements

### 3. Génération PARAMETERS_REFERENCE
Pour chaque paramètre:
- Nom technique
- Type et plage
- Valeur par défaut
- Description détaillée
- Impact sur le comportement
- Conseils de configuration

### 4. Génération EXAMPLES
- Scénarios d'utilisation courants
- Configurations recommandées
- Exemples de graphiques (descriptions)
- Cas d'usage spécifiques

### 5. Génération QUICK_START
- Installation en 3 étapes
- Configuration minimale
- Premier test

## Output Example
```markdown
# Guide Utilisateur - Super RSI

## Introduction
Super RSI est un indicateur avancé qui combine...

## Installation
1. Télécharger le fichier...
2. Compiler dans MetaEditor...
3. Ajouter au graphique...

## Paramètres
### RSI Period
- Type: Entier
- Défaut: 14
- Plage: 2-100
- Description: Période de calcul du RSI
- Conseil: Period plus court = plus sensible

## Signaux
- **Achete**: RSI &lt; 30 et croisement haussier
- **Vendre**: RSI &gt; 70 et croisement baissier

## Exemples
### Trend following
Utiliser avec EMA 200 pour filtrer les signaux...
```

## Validation
- Documentation complète et précise
- Accessible aux débutants
- Toutes les options documentées

## Example
```
Input: RSI code + rules
Output: 4 fichiers docs générés automatiquement
```