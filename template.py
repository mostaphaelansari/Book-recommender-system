"""
Project Setup Script.

This script creates a standardized data science project directory structure
with necessary folders and files.
"""
from pathlib import Path
import os
from typing import List, Dict, Any, Tuple

def create_project_structure():
    """Create the complete project directory structure."""
    # Define directory structure using a nested dictionary
    project_structure = {
        "data": ["raw", "processed", "interim", "external"],
        "notebooks": [],
        "src": ["data", "models", "utils"],
        "models": ["trained_models", "model_metrics"],
        "tests": [],
        "reports": ["figures"],
        "docs": [],
        "app": ["api", "static", "templates"]
    }
    
    # Create directories
    for parent_dir, sub_dirs in project_structure.items():
        parent_path = Path(parent_dir)
        # Create parent directory
        os.makedirs(parent_path, exist_ok=True)
        
        # Create subdirectories
        for sub_dir in sub_dirs:
            sub_path = parent_path / sub_dir
            os.makedirs(sub_path, exist_ok=True)
    
    # Create root-level files
    root_files = [
        "Makefile",
        "setup.py",
        "config.yml",
        "Dockerfile",
        ".gitignore",
        ".dockerignore",
        "README.md"  # Added README file
    ]
    
    for file_name in root_files:
        Path(file_name).touch(exist_ok=True)
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
