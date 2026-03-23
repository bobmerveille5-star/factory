#!/usr/bin/env python3
"""
Trading Indicator Factory - CLI
Unified command-line interface for generating trading indicators.
"""

import sys
import os
import json
import argparse
from pathlib import Path


# === CONSTANTS ===
ROOT_DIR = Path(__file__).parent.parent
PROJECTS_DIR = ROOT_DIR / "projects"
SKILLS_DIR = ROOT_DIR / "skills"

COLOR = {
    'reset': '\033[0m', 'green': '\033[32m', 'yellow': '\033[33m',
    'blue': '\033[34m', 'red': '\033[31m', 'cyan': '\033[36m'
}


def log(color: str, msg: str) -> None:
    print(f"{COLOR[color]}➜ {msg}{COLOR['reset']}")


# === SKILL REGISTRY ===
SKILLS = {
    '1-Foundation': ['rules_formalizer', 'mt5_doc_guard', 'mt4_doc_guard', 'pine_doc_guard', 'ninjatrader_doc_guard'],
    '2-Pipeline': ['brief_intake', 'architecture', 'test_design'],
    '3-Codegen': ['mt5_indicator_codegen', 'mt4_indicator_codegen', 'pine_indicator_codegen', 'ninjatrader_indicator_codegen'],
    '4-Optimization': ['code_optimizer', 'indicator_composer', 'backtest_validator'],
    '5-Advanced': ['pattern_detector', 'signal_generator', 'divergence_detector'],
    '6-Analysis': ['market_structure', 'volume_analyzer', 'risk_calculator'],
    '7-Session': ['session_analyzer', 'correlator'],
    '8-QC': ['mt5_review', 'mt4_review', 'pine_review', 'ninjatrader_review'],
    '9-Delivery': ['doc_sync', 'decision_logger', 'packaging']
}

# Import patterns from core
import sys
sys.path.insert(0, str(ROOT_DIR / 'lib'))
from core import PATTERNS as CORE_PATTERNS, PATTERN_ALIASES

# Map patterns to MQL5 function names
MQL5_FUNCTIONS = {
    'rsi': ('iRSI', 'PRICE_CLOSE'),
    'macd': ('iMACD', 'NULL'),
    'sma': ('iMA', 'PRICE_CLOSE'),
    'ema': ('iEMA', 'PRICE_CLOSE'),
    'bollinger': ('iBands', 'PRICE_CLOSE'),
    'atr': ('iATR', 'NULL'),
    'stochastic': ('iStochastic', 'NULL'),
    'adx': ('iADX', 'NULL'),
    'cci': ('iCCI', 'PRICE_CLOSE'),
    'vwap': ('iVWAP', 'NULL'),
    'williams_r': ('iWPR', 'NULL'),
    'mfi': ('iMFI', 'NULL'),
    'obv': ('iOBV', 'NULL'),
    'roc': ('iROC', 'PRICE_CLOSE'),
    'envelopes': ('iEnvelopes', 'PRICE_CLOSE'),
    'donchian': ('iDonchian', 'NULL'),
    'ichimoku': ('iIchimoku', 'NULL'),
    'stddev': ('iStdDev', 'PRICE_CLOSE'),
    'trix': ('iTRIX', 'NULL'),
    'ultimate': ('iUltimateOscillator', 'NULL'),
}

# Default template when pattern not found
DEFAULT_PATTERNS = {
    'rsi': {'name': 'RSI', 'params': {'period': 14, 'overbought': 70, 'oversold': 30}},
    'macd': {'name': 'MACD', 'params': {'fast': 12, 'slow': 26, 'signal': 9}},
    'sma': {'name': 'SMA', 'params': {'period': 20}},
    'ema': {'name': 'EMA', 'params': {'period': 20}},
    'bollinger': {'name': 'Bollinger', 'params': {'period': 20, 'std_dev': 2.0}},
    'atr': {'name': 'ATR', 'params': {'period': 14}},
    'stochastic': {'name': 'Stochastic', 'params': {'k': 14, 'd': 3}},
}

# Full patterns dict for CLI (merge default + core)
PATTERNS = {**DEFAULT_PATTERNS, **{k: {'name': v.name, 'params': v.params} for k, v in CORE_PATTERNS.items()}}


def get_pattern_code(pattern: str, name: str) -> dict:
    """Generate code for a specific pattern."""
    func_info = MQL5_FUNCTIONS.get(pattern, ('iRSI', 'PRICE_CLOSE'))
    func_name, price = func_info
    
    # Get params
    params = PATTERNS.get(pattern, PATTERNS['rsi'])['params']
    
    return {
        'mt5': f"""//+------------------------------------------------------------------+
//| {name}.mq5 - {PATTERNS.get(pattern, PATTERNS['rsi'])['name']}
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots 1

input int Period = {params.get('period', 14)};

int handle;
double buffer[];

int OnInit() {{
    handle = {func_name}(NULL, PERIOD_CURRENT, {', '.join(str(v) for v in params.values())});
    SetIndexBuffer(0, buffer);
    return INIT_SUCCEEDED;
}}

int OnCalculate(int rates, int prev, const double& open[], const double& close[]) {{
    double ind[];
    CopyBuffer(handle, 0, 0, rates, ind);
    for(int i = 0; i < rates; i++) buffer[i] = ind[i];
    return rates;
}}
""",
        'mt4': f"""//+------------------------------------------------------------------+
//| {name}.mq4 - {PATTERNS.get(pattern, PATTERNS['rsi'])['name']}
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots 1

extern int Period = {params.get('period', 14)};
double buffer[];

int init() {{
    SetIndexBuffer(0, buffer);
    return 0;
}}

int start() {{
    int limit = Bars - IndicatorCounted();
    for(int i = limit - 1; i >= 0; i--) buffer[i] = {func_name}(NULL, 0, {', '.join(str(v) for v in params.values())}, i);
    return 0;
}}
""",
        'pine': f"""//@version=5
indicator("{name}", overlay=false)
Period = input({params.get('period', 14)})
ind = ta.{pattern}(close, Period)
plot(ind, color=color.blue)
""",
        'ninjatrader': f"""namespace MyIndicator {{
    public class {name} : Indicator {{
        protected override void Initialize() {{ }}
        protected override void OnBarUpdate() {{ }}
    }}
}}
"""
    }


# Multi-pattern template
def generate_multi_pattern_code(name: str, patterns: list) -> dict:
    """Generate code for multiple patterns."""
    n = len(patterns)
    
    return {
        'mt5': f"""//+------------------------------------------------------------------+
//| {name}.mq5 - Multi Indicator ({', '.join(patterns)})
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots {n}

input int Period = 14;

{chr(10).join([f'int handle{i};' for i in range(n)])}
{chr(10).join([f'double buffer{i}[];' for i in range(n)])}

int OnInit() {{
{chr(10).join([f'    handle{i} = iRSI(NULL, PERIOD_CURRENT, Period, PRICE_CLOSE);' for i in range(n)])}
{chr(10).join([f'    SetIndexBuffer({i}, buffer{i});' for i in range(n)])}
    return INIT_SUCCEEDED;
}}

int OnCalculate(int rates, int prev, const double& open[], const double& close[]) {{
{chr(10).join([f'    double ind{i}[]; CopyBuffer(handle{i}, 0, 0, rates, ind{i});' for i in range(n)])}
{chr(10).join([f'    buffer{i}[i] = ind{i}[i];' for i in range(n)])}
    return rates;
}}
""",
        'mt4': f"""//+------------------------------------------------------------------+
//| {name}.mq4 - Multi Indicator ({', '.join(patterns)})
//+------------------------------------------------------------------+
#property indicator_chart_window
#property indicator_plots {n}

extern int Period = 14;
{chr(10).join([f'double buffer{i}[];' for i in range(n)])}

int init() {{
{chr(10).join([f'    SetIndexBuffer({i}, buffer{i});' for i in range(n)])}
    return 0;
}}

int start() {{
    int limit = Bars - IndicatorCounted();
{chr(10).join([f'    for(int i = limit - 1; i >= 0; i--) buffer{i}[i] = iRSI(NULL, 0, Period, PRICE_CLOSE, i);' for i in range(n)])}
    return 0;
}}
""",
        'pine': f"""//@version=5
indicator("{name}", overlay=false)
Period = input(14)
{chr(10).join([f'ind{i} = ta.{p}(close, Period)' for i, p in enumerate(patterns)])}
{chr(10).join([f'plot(ind{i}, title="{p}")' for i, p in enumerate(patterns)])}
""",
        'ninjatrader': f"""namespace MyIndicator {{
    public class {name} : Indicator {{
        protected override void Initialize() {{ }}
        protected override void OnBarUpdate() {{ }}
    }}
}}
"""
    }

# Legacy template (not used anymore)
PLATFORM_CODE = {
    'mt5': '',
    'mt4': '',
    'pine': '',
    'ninjatrader': ''
}


# === CORE FUNCTIONS ===
def detect_patterns(desc: str) -> list:
    """Detect indicator patterns from description."""
    found = []
    for p in PATTERNS:
        if p in desc.lower() or PATTERNS[p]['name'].lower() in desc.lower():
            found.append(p)
    return found


def generate_rules(desc: str) -> dict:
    """Generate rules specification from description."""
    patterns = detect_patterns(desc)
    params = []
    for p in patterns:
        for k, v in PATTERNS[p]['params'].items():
            params.append({'name': k, 'default': v, 'source': p})
    return {
        'patterns': patterns,
        'params': params,
        'confidence': 85 if patterns else 30
    }


def create_project(name: str, desc: str) -> int:
    """Create a new indicator project."""
    proj_dir = PROJECTS_DIR / name
    if proj_dir.exists():
        log('red', f"Project {name} already exists")
        return 1

    proj_dir.mkdir(parents=True)
    (proj_dir / 'mt5' / 'src').mkdir(parents=True)
    (proj_dir / 'mt4' / 'src').mkdir(parents=True)
    (proj_dir / 'pine' / 'src').mkdir(parents=True)
    (proj_dir / 'ninjatrader' / 'src').mkdir(parents=True)

    # Create spec file
    with open(proj_dir / '.spec.json', 'w') as f:
        json.dump({'name': name, 'description': desc}, f)

    # Create template files
    files = {
        'PRODUCT_SPEC.md': f"# {name}\n\n{desc}\n",
        'RULES_SPEC.md': "# RULES\n\nPending...",
        'ARCHITECTURE.md': "# Architecture\n\nMulti-platform indicator\n",
        'TEST_CASES.md': "# Tests\n\nTo be defined\n"
    }
    for fname, content in files.items():
        with open(proj_dir / fname, 'w') as f:
            f.write(content)

    log('green', f"Project {name} created")
    return 0


def run_skill(skill: str, project: str, desc: str = '') -> int:
    """Execute a skill on a project."""
    proj_dir = PROJECTS_DIR / project
    if not proj_dir.exists():
        log('red', f"Project {project} not found")
        return 1

    if skill == 'rules_formalizer':
        rules = generate_rules(desc)
        with open(proj_dir / 'RULES_SPEC.md', 'w') as f:
            f.write(f"# RULES - {project}\n\n")
            f.write(f"Patterns: {', '.join(rules['patterns']) or 'None'}\n\n")
            f.write("## Parameters\n")
            for p in rules['params']:
                f.write(f"- {p['name']} = {p['default']} ({p['source']})\n")
        log('green', f"Rules generated for {project}")
    else:
        log('yellow', f"Skill {skill} not implemented")
    return 0


def generate_code(project: str) -> int:
    """Generate code for all platforms based on description."""
    proj_dir = PROJECTS_DIR / project
    if not proj_dir.exists():
        log('red', f"Project {project} not found")
        return 1
    
    # Get description from spec
    spec_file = proj_dir / '.spec.json'
    if spec_file.exists():
        import json
        spec = json.loads(spec_file.read_text())
        desc = spec.get('description', '')
    else:
        desc = ''
    
    # Detect patterns
    patterns = detect_patterns(desc)
    
    if not patterns:
        # Use default RSI
        patterns = ['rsi']
    
    log('blue', f"Detected patterns: {', '.join(patterns)}")
    
    # Generate code
    exts = {'mt5': '.mq5', 'mt4': '.mq4', 'pine': '.pine', 'ninjatrader': '.cs'}
    
    if len(patterns) == 1:
        # Single pattern
        code = get_pattern_code(patterns[0], project)
    else:
        # Multi-pattern
        code = generate_multi_pattern_code(project, patterns)
    
    for plat, ext in exts.items():
        filepath = proj_dir / plat / 'src' / f"{project}{ext}"
        filepath.write_text(code[plat])
        log('green', f"  {plat}: {filepath.name}")
    
    return 0


def show_status(project: str) -> int:
    """Show project status."""
    proj_dir = PROJECTS_DIR / project
    if not proj_dir.exists():
        log('red', f"Project {project} not found")
        return 1

    log('blue', f"Project: {project}")
    for root, dirs, files in os.walk(proj_dir):
        level = root.replace(str(proj_dir), '').count(os.sep)
        indent = '  ' * level
        folder = Path(root).name
        if folder and not folder.startswith('.') and folder != project:
            print(f"{indent}{folder}/")
        for f in sorted(files):
            if not f.startswith('.'):
                print(f"{'  ' * (level + 1)}{f}")
    return 0


def list_skills() -> int:
    """List all available skills."""
    log('blue', 'Skills:')
    for phase, skills in SKILLS.items():
        print(f"\n{phase}:")
        for s in skills:
            print(f"  - {s}")
    print(f"\n{COLOR['cyan']}Total: {sum(len(v) for v in SKILLS.values())} skills{COLOR['reset']}")
    return 0


def validate_project(project: str) -> int:
    """Validate project structure and files."""
    proj_dir = PROJECTS_DIR / project
    if not proj_dir.exists():
        log('red', f"Project {project} not found")
        return 1
    
    required = ['PRODUCT_SPEC.md', 'RULES_SPEC.md', 'ARCHITECTURE.md', 'TEST_CASES.md']
    errors = []
    
    for f in required:
        if not (proj_dir / f).exists():
            errors.append(f"Missing: {f}")
    
    # Check platform dirs
    for plat in ['mt5', 'mt4', 'pine', 'ninjatrader']:
        if not (proj_dir / plat / 'src').exists():
            errors.append(f"Missing: {plat}/src/")
    
    if errors:
        log('red', f"Validation failed for {project}:")
        for e in errors:
            print(f"  - {e}")
        return 1
    
    log('green', f"Project {project} is valid ✓")
    return 0


def build_project(project: str) -> int:
    """Build and verify generated code."""
    proj_dir = PROJECTS_DIR / project
    if not proj_dir.exists():
        log('red', f"Project {project} not found")
        return 1
    
    log('blue', f"Building {project}...")
    
    # Check generated files
    built = 0
    for plat in ['mt5', 'mt4', 'pine', 'ninjatrader']:
        src_dir = proj_dir / plat / 'src'
        files = list(src_dir.glob('*')) if src_dir.exists() else []
        if files:
            log('green', f"  {plat}: {len(files)} file(s)")
            built += len(files)
        else:
            log('yellow', f"  {plat}: no files")
    
    log('green', f"Build complete: {built} files")
    return 0


# === CLI ===
def main():
    parser = argparse.ArgumentParser(description='Trading Indicator Factory CLI')
    sub = parser.add_subparsers(dest='cmd')

    sub.add_parser('list-skills', help='List all skills')
    sub.add_parser('detect', help='Detect patterns in description').add_argument('desc', nargs='?', default='')
    
    new_cmd = sub.add_parser('new', help='Create new project')
    new_cmd.add_argument('name')
    new_cmd.add_argument('description', nargs='?', default='')
    
    run_cmd = sub.add_parser('run-skill', help='Run a skill')
    run_cmd.add_argument('skill')
    run_cmd.add_argument('project')
    run_cmd.add_argument('--description', default='')
    
    sub.add_parser('generate', help='Generate code').add_argument('project')
    sub.add_parser('validate', help='Validate project').add_argument('project')
    sub.add_parser('build', help='Build project').add_argument('project')
    sub.add_parser('status', help='Show project status').add_argument('project')

    args = parser.parse_args()
    
    if args.cmd == 'list-skills':
        return list_skills()
    elif args.cmd == 'detect':
        print(f"Patterns: {detect_patterns(args.desc or '')}")
    elif args.cmd == 'new':
        return create_project(args.name, args.description)
    elif args.cmd == 'run-skill':
        return run_skill(args.skill, args.project, args.description)
    elif args.cmd == 'generate':
        return generate_code(args.project)
    elif args.cmd == 'validate':
        return validate_project(args.project)
    elif args.cmd == 'build':
        return build_project(args.project)
    elif args.cmd == 'status':
        return show_status(args.project)
    else:
        parser.print_help()
    return 0


if __name__ == '__main__':
    sys.exit(main())