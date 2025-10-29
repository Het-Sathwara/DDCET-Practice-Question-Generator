"""Question generators for Physics

NOTE: Mathematics uses JSON question banks (31,000 questions)
      Physics uses dynamic Python generators (unlimited questions)
      
Complete DDCET Physics Syllabus Coverage:
1. Physical Quantities & Units
2. Classical Mechanics
3. Electric Current (including Electrostatics)
4. Heat and Thermometry
5. Wave Motion and Optics
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

from .physics_generators_additional import (
    UnitsAndMeasurementGenerator,
    ElectrostaticsGenerator,
    OpticsGenerator
)

__all__ = [
    # Physics (11 generators) - Complete DDCET coverage - Dynamic generation
    'UnitsAndMeasurementGenerator',    # Topic 1: Physical Quantities & Units
    'KinematicsGenerator',              # Topic 2: Classical Mechanics
    'NewtonLawsGenerator',              # Topic 2: Classical Mechanics
    'CircularMotionGenerator',          # Topic 2: Classical Mechanics
    'WorkEnergyGenerator',              # Topic 2: Classical Mechanics
    'OhmsLawGenerator',                 # Topic 3: Electric Current
    'CapacitanceGenerator',             # Topic 3: Electric Current
    'ElectrostaticsGenerator',          # Topic 3: Electric Current (Electrostatics)
    'HeatTransferGenerator',            # Topic 4: Heat and Thermometry
    'WaveMotionGenerator',              # Topic 5: Wave Motion
    'OpticsGenerator'                   # Topic 5: Optics
]

