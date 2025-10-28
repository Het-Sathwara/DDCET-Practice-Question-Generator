#!/usr/bin/env python3
"""
Main entry point for the DDCET Question Generator
Run this file to start the CLI application
"""

import sys
import os

# Add parent directory to path to enable imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from question_generator.cli import main

if __name__ == "__main__":
    main()

