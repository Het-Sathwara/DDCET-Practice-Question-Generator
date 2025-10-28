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

# Only remaining legacy math generators
from .math_generators import (
    MatricesGenerator,
    LogarithmGenerator,
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
    # Mathematics - Remaining legacy generators (3 generators)
    # Note: Trigonometry, Vectors, Coordinate Geometry, Limits, Differentiation, Integration
    #       have comprehensive implementations in question_generator.maths module
    'MatricesGenerator',
    'LogarithmGenerator',
    'StatisticsGenerator'
]

