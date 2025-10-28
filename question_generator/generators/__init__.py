"""Question generators for Physics and Mathematics

NOTE: Most math generators have moved to question_generator.maths module
      This module now only contains Physics generators and remaining math generators.
"""

from .physics_generators import (
    KinematicsGenerator,
    NewtonLawsGenerator,
    CircularMotionGenerator,
    WorkEnergyGenerator,
    OhmsLawGenerator,
    CapacitanceGenerator,
    HeatTransferGenerator,
    WaveMotionGenerator
)

# Math generators - NEW: Bank-based system for better variety
from .math_bank_generator import (
    MatricesBankGenerator,
    LogarithmBankGenerator
)

# Legacy generators
from .math_generators import (
    StatisticsGenerator
)

__all__ = [
    # Physics (8 generators)
    'KinematicsGenerator',
    'NewtonLawsGenerator',
    'CircularMotionGenerator',
    'WorkEnergyGenerator',
    'OhmsLawGenerator',
    'CapacitanceGenerator',
    'HeatTransferGenerator',
    'WaveMotionGenerator',
    # Mathematics - Bank-based generators (better variety!)
    'MatricesBankGenerator',
    'LogarithmBankGenerator',
    # Legacy
    'StatisticsGenerator'
]

