#!/usr/bin/env python3
"""
Tests de génération réelle - vérifie que les fichiers sont créés correctement.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

sys.path.insert(0, 'src')
from gsd.cli import create_project, generate_code, validate_project


def test_create_project_structure():
    """Test 1: Création de projet avec structure complète."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        
        # Mock PROJECTS_DIR
        import gsd.cli
        orig = gsd.cli.PROJECTS_DIR
        gsd.cli.PROJECTS_DIR = Path(tmpdir) / "projects"
        
        result = create_project("test-rsi", "RSI indicator")
        
        # Restore
        gsd.cli.PROJECTS_DIR = orig
        
        assert result == 0, "create_project should return 0"
        assert (Path(tmpdir)/"projects"/"test-rsi"/"PRODUCT_SPEC.md").exists()
        assert (Path(tmpdir)/"projects"/"test-rsi"/"mt5"/"src").exists()
        print("✓ Test 1: Création de projet OK")


def test_generate_4_files():
    """Test 2: Génération des 4 fichiers."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        
        import gsd.cli
        orig = gsd.cli.PROJECTS_DIR
        gsd.cli.PROJECTS_DIR = Path(tmpdir) / "projects"
        
        create_project("test-ind", "Test")
        result = generate_code("test-ind")
        
        gsd.cli.PROJECTS_DIR = orig
        
        assert result == 0, "generate_code should return 0"
        
        base = Path(tmpdir)/"projects"/"test-ind"
        assert (base/"mt5"/"src"/"test-ind.mq5").exists()
        assert (base/"mt4"/"src"/"test-ind.mq4").exists()
        assert (base/"pine"/"src"/"test-ind.pine").exists()
        assert (base/"ninjatrader"/"src"/"test-ind.cs").exists()
        print("✓ Test 2: 4 fichiers générés OK")


def test_validate_existing_project():
    """Test 3: Validation de projet existant."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        
        import gsd.cli
        orig = gsd.cli.PROJECTS_DIR
        gsd.cli.PROJECTS_DIR = Path(tmpdir) / "projects"
        
        create_project("valid-proj", "Valid project")
        result = validate_project("valid-proj")
        
        gsd.cli.PROJECTS_DIR = orig
        
        assert result == 0, "validate_project should return 0 for valid project"
        print("✓ Test 3: Validation projet OK")


if __name__ == "__main__":
    test_create_project_structure()
    test_generate_4_files()
    test_validate_existing_project()
    print("\n✅ Tous les tests de génération passent!")
