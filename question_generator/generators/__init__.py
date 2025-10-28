"""Question generators for Physics

NOTE: Mathematics uses JSON question banks (31,000 questions)
      Physics uses dynamic Python generators (unlimited questions)
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

__all__ = [
    # Physics (8 generators) - Dynamic generation
    'KinematicsGenerator',
    'NewtonLawsGenerator',
    'CircularMotionGenerator',
    'WorkEnergyGenerator',
    'OhmsLawGenerator',
    'CapacitanceGenerator',
    'HeatTransferGenerator',
    'WaveMotionGenerator'
]

