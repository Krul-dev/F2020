#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-26
Description: 
"""

import tomllib
from pathlib import Path

def get_project_scripts():
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    toml_path = project_root / "pyproject.toml"
    toml_file = Path(toml_path)
    if not toml_file.exists():
        raise FileNotFoundError(f"{toml_path} not found.")
    
    with open(toml_file, "rb") as f:
        data = tomllib.load(f)
    
    # Extract scripts if available
    try:
        scripts = data["project"]["scripts"]
        return scripts
    except KeyError:
        print("No scripts found in pyproject.toml.")
        return {}

# Example usage
scripts = get_project_scripts()
script_names = list(scripts.keys())
print("Project Scripts:", script_names)

