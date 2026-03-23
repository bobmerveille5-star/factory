# Trading Indicator Factory

**CLI pour générer des indicateurs de trading multi-plateformes.**

```
Idée: "RSI avec alertes sur surachat/survente"
↓
python3 src/gsd/cli.py new my-rsi "RSI avec alertes"
python3 src/gsd/cli.py generate my-rsi
↓
→ my-rsi.mq5 (MT5)
→ my-rsi.mq4 (MT4)
→ my-rsi.pine (TradingView)
→ my-rsi.cs (NinjaTrader)
```

## 🎯 C'est quoi ?

Un outil qui transforme une idée d'indicateur en code prêt-à-compiler pour **4 plateformes** :
- MetaTrader 5 (MQL5)
- MetaTrader 4 (MQL4)
- Pine Script (TradingView)
- NinjaTrader (NinjaScript)

## ⚡ Exemple réel

```bash
# 1. Créer un indicateur
$ python3 src/gsd/cli.py new my-rsi "RSI avec alertes"
➜ Project my-rsi created

# 2. Générer le code (4 plateformes)
$ python3 src/gsd/cli.py generate my-rsi
➜   mt5: my-rsi.mq5
➜   mt4: my-rsi.mq4
➜   pine: my-rsi.pine
➜   ninjatrader: my-rsi.cs

# 3. Vérifier la structure
$ python3 src/gsd/cli.py validate my-rsi
➜ Project my-rsi is valid ✓
```

## 📁 Résultat obtenu

```
my-rsi/
├── mt5/src/my-rsi.mq5      # Prêt pour MetaTrader 5
├── mt4/src/my-rsi.mq4      # Prêt pour MetaTrader 4
├── pine/src/my-rsi.pine     # Prêt pour TradingView
├── ninjatrader/src/my-rsi.cs # Prêt pour NinjaTrader
├── PRODUCT_SPEC.md
├── RULES_SPEC.md
├── ARCHITECTURE.md
└── TEST_CASES.md
```

## 🔧 Commandes CLI

```bash
python3 src/gsd/cli.py list-skills              # Voir les skills disponibles
python3 src/gsd/cli.py detect "RSI + MACD"     # Détecter les patterns
python3 src/gsd/cli.py new <nom> <desc>        # Créer un projet
python3 src/gsd/cli.py run-skill <skill> <proj> # Exécuter un skill
python3 src/gsd/cli.py generate <nom>           # Générer le code
python3 src/gsd/cli.py validate <nom>           # Valider la structure
python3 src/gsd/cli.py build <nom>              # Compiler le projet
python3 src/gsd/cli.py status <nom>             # Voir le statut
```

## 🧪 Tests

```bash
# Tests unitaires (détection de patterns)
python3 -c "
import sys; sys.path.insert(0, 'src')
from lib.core import detect_patterns
assert 'rsi' in detect_patterns('RSI avec alertes')
print('✓ Tests passent')
"

# Tests de génération (création + 4 fichiers)
python3 tests/test_generation.py
```

## 📦 Structure du projet

```
factory/
├── src/gsd/cli.py          # CLI principale
├── src/lib/core.py          # Moteur de patterns (7 indicateurs)
├── tests/                   # Tests unitaires + génération
├── skills/                  # 42 skills (spécifications)
├── projects/               # Projets générés
└── .github/workflows/       # CI/CD
```

## ✅ / 🚧 État actuel

| Fonctionnalité | État |
|----------------|------|
| Détection patterns (RSI, MACD, SMA, EMA, Bollinger, ATR, Stochastic) | ✅ OK |
| Génération code 4 plateformes | ✅ OK |
| Validation projet | ✅ OK |
| Tests de génération | ✅ OK |
| Templates avancés (multi-timeframe, backtest) | 🚧 En cours |
| Validation syntaxe MQL | 🚧 En cours |

## 🆚 Comparaison

| Approche | Résultats |
|----------|-----------|
| **Factory** | Fichiers prêts, validation, tests |
| ChatGPT | Code à copier-coller, erreurs possibles |
| Manuel | Temps, erreurs, maintenance difficile |

## 📝 License

MIT