"""
Mathematics Question Generators Module
Individual generator files for each DDCET Math topic
"""

from .trigonometric_functions import generate_trigonometric_questions
from .vectors import generate_vector_questions
from .coordinate_geometry import generate_coordinate_geometry_questions
from .limits import generate_limit_questions
from .differentiation import generate_differentiation_questions
from .integration import generate_integration_questions

__all__ = [
    'generate_trigonometric_questions',
    'generate_vector_questions',
    'generate_coordinate_geometry_questions',
    'generate_limit_questions',
    'generate_differentiation_questions',
    'generate_integration_questions',
]

# Generator registry for easy access
ALL_GENERATORS = {
    "trigonometry": generate_trigonometric_questions,
    "vectors": generate_vector_questions,
    "coordinate_geometry": generate_coordinate_geometry_questions,
    "limits": generate_limit_questions,
    "differentiation": generate_differentiation_questions,
    "integration": generate_integration_questions,
}


def list_available_generators():
    """List all available question generators"""
    return list(ALL_GENERATORS.keys())


def get_generator(topic: str):
    """Get a specific generator by topic name"""
    return ALL_GENERATORS.get(topic)

