"""
Topic: Vectors
Syllabus: DDCET Mathematics
Features: Direction, Magnitude, Types, Addition/Subtraction, Dot/Cross Product
         Randomized MCQs, numerical questions, difficulty levels.
"""

import random
import math
from typing import List, Dict, Any, Tuple


def generate_magnitude_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate vector magnitude calculation questions"""
    questions = []
    
    range_map = {
        'easy': (1, 5),
        'medium': (1, 10),
        'hard': (5, 20)
    }
    
    val_range = range_map.get(difficulty, range_map['medium'])
    
    for _ in range(count):
        dimensions = 3 if difficulty != 'easy' else 2
        
        if dimensions == 2:
            i = random.randint(val_range[0], val_range[1])
            j = random.randint(val_range[0], val_range[1])
            
            magnitude = round(math.sqrt(i**2 + j**2), 2)
            
            questions.append({
                "topic": "Vectors - Magnitude",
                "difficulty": difficulty,
                "question": f"Find the magnitude of vector v = {i}i + {j}j",
                "answer": magnitude,
                "type": "numerical",
                "solution": f"|v| = √({i}² + {j}²) = √{i**2 + j**2} = {magnitude}"
            })
        else:
            i = random.randint(val_range[0], val_range[1])
            j = random.randint(val_range[0], val_range[1])
            k = random.randint(val_range[0], val_range[1])
            
            magnitude = round(math.sqrt(i**2 + j**2 + k**2), 2)
            
            questions.append({
                "topic": "Vectors - Magnitude",
                "difficulty": difficulty,
                "question": f"Find the magnitude of vector v = {i}i + {j}j + {k}k",
                "answer": magnitude,
                "type": "numerical",
                "solution": f"|v| = √({i}² + {j}² + {k}²) = √{i**2 + j**2 + k**2} = {magnitude}"
            })
    
    return questions


def generate_unit_vector_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate unit vector questions"""
    questions = []
    
    for _ in range(count):
        i = random.randint(1, 10)
        j = random.randint(1, 10)
        
        magnitude = math.sqrt(i**2 + j**2)
        unit_i = round(i / magnitude, 3)
        unit_j = round(j / magnitude, 3)
        
        questions.append({
            "topic": "Vectors - Unit Vector",
            "difficulty": difficulty,
            "question": f"Find the unit vector in the direction of v = {i}i + {j}j",
            "answer": f"{unit_i}i + {unit_j}j",
            "type": "conceptual",
            "solution": f"|v| = √({i}² + {j}²) = {round(magnitude, 2)}, û = v/|v| = {unit_i}i + {unit_j}j"
        })
    
    return questions


def generate_addition_subtraction_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate vector addition and subtraction questions"""
    questions = []
    
    for _ in range(count):
        # Generate two vectors
        v1_i, v1_j = random.randint(1, 10), random.randint(1, 10)
        v2_i, v2_j = random.randint(1, 10), random.randint(1, 10)
        
        operation = random.choice(['+', '-'])
        
        if operation == '+':
            result_i = v1_i + v2_i
            result_j = v1_j + v2_j
            op_name = "sum"
        else:
            result_i = v1_i - v2_i
            result_j = v1_j - v2_j
            op_name = "difference"
        
        questions.append({
            "topic": f"Vectors - {op_name.capitalize()}",
            "difficulty": difficulty,
            "question": f"Find v₁ {operation} v₂ where v₁ = {v1_i}i + {v1_j}j and v₂ = {v2_i}i + {v2_j}j",
            "answer": f"{result_i}i + {result_j}j",
            "type": "conceptual",
            "solution": f"v₁ {operation} v₂ = ({v1_i}{operation}{v2_i})i + ({v1_j}{operation}{v2_j})j = {result_i}i + {result_j}j"
        })
    
    return questions


def generate_dot_product_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate dot product (scalar product) questions"""
    questions = []
    
    range_map = {
        'easy': (1, 5),
        'medium': (1, 10),
        'hard': (5, 15)
    }
    
    val_range = range_map.get(difficulty, range_map['medium'])
    
    for _ in range(count):
        dimensions = 3 if difficulty == 'hard' else 2
        
        if dimensions == 2:
            v1_i, v1_j = random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1])
            v2_i, v2_j = random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1])
            
            dot_product = v1_i * v2_i + v1_j * v2_j
            
            questions.append({
                "topic": "Vectors - Dot Product",
                "difficulty": difficulty,
                "question": f"Find v₁ · v₂ where v₁ = {v1_i}i + {v1_j}j and v₂ = {v2_i}i + {v2_j}j",
                "answer": dot_product,
                "type": "numerical",
                "solution": f"v₁ · v₂ = ({v1_i})({v2_i}) + ({v1_j})({v2_j}) = {v1_i*v2_i} + {v1_j*v2_j} = {dot_product}"
            })
        else:
            v1_i, v1_j, v1_k = random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1])
            v2_i, v2_j, v2_k = random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1])
            
            dot_product = v1_i * v2_i + v1_j * v2_j + v1_k * v2_k
            
            questions.append({
                "topic": "Vectors - Dot Product",
                "difficulty": difficulty,
                "question": f"Find v₁ · v₂ where v₁ = {v1_i}i + {v1_j}j + {v1_k}k and v₂ = {v2_i}i + {v2_j}j + {v2_k}k",
                "answer": dot_product,
                "type": "numerical",
                "solution": f"v₁ · v₂ = {v1_i}×{v2_i} + {v1_j}×{v2_j} + {v1_k}×{v2_k} = {dot_product}"
            })
    
    return questions


def generate_cross_product_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate cross product (vector product) questions for 3D vectors"""
    questions = []
    
    for _ in range(count):
        v1_i, v1_j, v1_k = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
        v2_i, v2_j, v2_k = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
        
        # Cross product formula: (a₂b₃ - a₃b₂)i + (a₃b₁ - a₁b₃)j + (a₁b₂ - a₂b₁)k
        cross_i = v1_j * v2_k - v1_k * v2_j
        cross_j = v1_k * v2_i - v1_i * v2_k
        cross_k = v1_i * v2_j - v1_j * v2_i
        
        questions.append({
            "topic": "Vectors - Cross Product",
            "difficulty": difficulty,
            "question": f"Find v₁ × v₂ where v₁ = {v1_i}i + {v1_j}j + {v1_k}k and v₂ = {v2_i}i + {v2_j}j + {v2_k}k",
            "answer": f"{cross_i}i + {cross_j}j + {cross_k}k",
            "type": "conceptual",
            "solution": f"v₁ × v₂ = |i  j  k |\n          |{v1_i} {v1_j} {v1_k}|\n          |{v2_i} {v2_j} {v2_k}| = {cross_i}i + {cross_j}j + {cross_k}k"
        })
    
    return questions


def generate_angle_between_vectors_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate questions on angle between two vectors"""
    questions = []
    
    for _ in range(count):
        v1_i, v1_j = random.randint(1, 5), random.randint(1, 5)
        v2_i, v2_j = random.randint(1, 5), random.randint(1, 5)
        
        # cos(θ) = (v1·v2) / (|v1||v2|)
        dot_product = v1_i * v2_i + v1_j * v2_j
        mag_v1 = math.sqrt(v1_i**2 + v1_j**2)
        mag_v2 = math.sqrt(v2_i**2 + v2_j**2)
        
        cos_theta = dot_product / (mag_v1 * mag_v2)
        angle_rad = math.acos(cos_theta)
        angle_deg = round(math.degrees(angle_rad), 2)
        
        questions.append({
            "topic": "Vectors - Angle Between Vectors",
            "difficulty": difficulty,
            "question": f"Find the angle between v₁ = {v1_i}i + {v1_j}j and v₂ = {v2_i}i + {v2_j}j (in degrees)",
            "answer": angle_deg,
            "type": "numerical",
            "solution": f"cos(θ) = (v₁·v₂)/(|v₁||v₂|) = {dot_product}/({round(mag_v1,2)}×{round(mag_v2,2)}) = {round(cos_theta,3)}, θ = {angle_deg}°"
        })
    
    return questions


def generate_vector_types_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate questions on vector types (null, unit, parallel, perpendicular)"""
    questions = []
    
    vector_types = [
        ("null vector", "A vector with zero magnitude", "0"),
        ("unit vector", "A vector with magnitude 1", "1"),
        ("position vector", "A vector representing position from origin", "varies"),
        ("equal vectors", "Vectors with same magnitude and direction", "same"),
    ]
    
    for _ in range(count):
        vtype = random.choice(vector_types)
        
        # Generate MCQ
        options = [vtype[1]]
        other_types = [v[1] for v in vector_types if v != vtype]
        options.extend(random.sample(other_types, min(3, len(other_types))))
        random.shuffle(options)
        
        questions.append({
            "topic": "Vectors - Types",
            "difficulty": difficulty,
            "question": f"What is a {vtype[0]}?",
            "answer": vtype[1],
            "options": options[:4],
            "type": "mcq",
            "solution": f"A {vtype[0]} is {vtype[1]}"
        })
    
    return questions


def generate_vector_questions(difficulty: str = "medium", count: int = 10, 
                              question_type: str = "all") -> List[Dict[str, Any]]:
    """
    Main function to generate vector questions
    
    Args:
        difficulty: "easy", "medium", or "hard"
        count: Number of questions to generate
        question_type: "magnitude", "unit", "addition", "dot", "cross", "angle", "types", or "all"
    
    Returns:
        List of question dictionaries
    """
    if question_type == "magnitude":
        return generate_magnitude_questions(difficulty, count)
    elif question_type == "unit":
        return generate_unit_vector_questions(difficulty, count)
    elif question_type == "addition":
        return generate_addition_subtraction_questions(difficulty, count)
    elif question_type == "dot":
        return generate_dot_product_questions(difficulty, count)
    elif question_type == "cross":
        return generate_cross_product_questions(difficulty, count)
    elif question_type == "angle":
        return generate_angle_between_vectors_questions(difficulty, count)
    elif question_type == "types":
        return generate_vector_types_questions(difficulty, count)
    else:  # all
        questions = []
        per_type = count // 7
        questions.extend(generate_magnitude_questions(difficulty, per_type))
        questions.extend(generate_unit_vector_questions(difficulty, per_type))
        questions.extend(generate_addition_subtraction_questions(difficulty, per_type))
        questions.extend(generate_dot_product_questions(difficulty, per_type))
        questions.extend(generate_cross_product_questions(difficulty, per_type))
        questions.extend(generate_angle_between_vectors_questions(difficulty, per_type))
        questions.extend(generate_vector_types_questions(difficulty, per_type))
        return questions[:count]


# Test block
if __name__ == "__main__":
    print("="*80)
    print("VECTORS QUESTION GENERATOR TEST")
    print("="*80)
    
    # Test different question types
    print("\n1. MAGNITUDE:")
    sample = generate_vector_questions("medium", 2, "magnitude")
    for q in sample:
        print(f"Q: {q['question']}")
        print(f"A: {q['answer']}\n")
    
    print("2. DOT PRODUCT:")
    sample = generate_vector_questions("medium", 2, "dot")
    for q in sample:
        print(f"Q: {q['question']}")
        print(f"A: {q['answer']}\n")
    
    print("3. CROSS PRODUCT:")
    sample = generate_vector_questions("hard", 1, "cross")
    for q in sample:
        print(f"Q: {q['question']}")
        print(f"A: {q['answer']}\n")
    
    print("="*80)
    print("✓ Vector generator working!")
    print("="*80)

