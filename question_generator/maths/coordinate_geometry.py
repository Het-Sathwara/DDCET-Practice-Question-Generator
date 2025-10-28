"""
Topic: Coordinate Geometry
Syllabus: DDCET Mathematics
Features: Lines (slope, equations, angles), Circles (equations, center, radius)
         Randomized MCQs, numerical questions, difficulty levels.
"""

import random
import math
from typing import List, Dict, Any


def generate_slope_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate slope calculation questions"""
    questions = []
    
    range_map = {
        'easy': (-5, 5),
        'medium': (-10, 10),
        'hard': (-20, 20)
    }
    
    val_range = range_map.get(difficulty, range_map['medium'])
    
    for _ in range(count):
        x1, y1 = random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1])
        x2, y2 = random.randint(val_range[0], val_range[1]), random.randint(val_range[0], val_range[1])
        
        # Ensure x1 != x2
        while x1 == x2:
            x2 = random.randint(val_range[0], val_range[1])
        
        slope = round((y2 - y1) / (x2 - x1), 2)
        
        questions.append({
            "topic": "Coordinate Geometry - Slope",
            "difficulty": difficulty,
            "question": f"Find the slope of the line passing through points ({x1}, {y1}) and ({x2}, {y2})",
            "answer": slope,
            "type": "numerical",
            "solution": f"m = (y₂-y₁)/(x₂-x₁) = ({y2}-{y1})/({x2}-{x1}) = {slope}"
        })
    
    return questions


def generate_distance_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate distance formula questions"""
    questions = []
    
    for _ in range(count):
        x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
        x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
        
        distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
        
        questions.append({
            "topic": "Coordinate Geometry - Distance",
            "difficulty": difficulty,
            "question": f"Find the distance between points ({x1}, {y1}) and ({x2}, {y2})",
            "answer": distance,
            "type": "numerical",
            "solution": f"d = √[(x₂-x₁)² + (y₂-y₁)²] = √[({x2}-{x1})² + ({y2}-{y1})²] = √{(x2-x1)**2 + (y2-y1)**2} = {distance}"
        })
    
    return questions


def generate_midpoint_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate midpoint formula questions"""
    questions = []
    
    for _ in range(count):
        x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
        x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
        
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        questions.append({
            "topic": "Coordinate Geometry - Midpoint",
            "difficulty": difficulty,
            "question": f"Find the midpoint of the line segment joining ({x1}, {y1}) and ({x2}, {y2})",
            "answer": f"({mid_x}, {mid_y})",
            "type": "conceptual",
            "solution": f"Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = (({x1}+{x2})/2, ({y1}+{y2})/2) = ({mid_x}, {mid_y})"
        })
    
    return questions


def generate_line_equation_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate questions on line equations (slope-point, two-point, intercept forms)"""
    questions = []
    
    for _ in range(count):
        form_type = random.choice(['slope_point', 'two_point', 'slope_intercept', 'intercept'])
        
        if form_type == 'slope_point':
            m = random.randint(-5, 5)
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            
            # y - y1 = m(x - x1)
            # y = mx - mx1 + y1
            c = y1 - m * x1
            
            questions.append({
                "topic": "Coordinate Geometry - Line Equation",
                "difficulty": difficulty,
                "question": f"Find the equation of a line with slope {m} passing through ({x1}, {y1}) in y = mx + c form",
                "answer": f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {abs(c)}",
                "type": "conceptual",
                "solution": f"Using y - y₁ = m(x - x₁): y - {y1} = {m}(x - {x1}), y = {m}x + {c}"
            })
        
        elif form_type == 'two_point':
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            x2, y2 = random.randint(-5, 5), random.randint(-5, 5)
            
            while x1 == x2:
                x2 = random.randint(-5, 5)
            
            m = (y2 - y1) / (x2 - x1)
            c = y1 - m * x1
            
            questions.append({
                "topic": "Coordinate Geometry - Line Equation",
                "difficulty": difficulty,
                "question": f"Find the slope of the line passing through ({x1}, {y1}) and ({x2}, {y2})",
                "answer": round(m, 2),
                "type": "numerical",
                "solution": f"m = (y₂-y₁)/(x₂-x₁) = ({y2}-{y1})/({x2}-{x1}) = {round(m, 2)}"
            })
        
        elif form_type == 'slope_intercept':
            m = random.randint(-5, 5)
            c = random.randint(-10, 10)
            
            questions.append({
                "topic": "Coordinate Geometry - Line Equation",
                "difficulty": difficulty,
                "question": f"What is the y-intercept of the line y = {m}x + {c}?",
                "answer": c,
                "type": "numerical",
                "solution": f"In y = mx + c form, c is the y-intercept = {c}"
            })
        
        else:  # intercept form
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            
            questions.append({
                "topic": "Coordinate Geometry - Intercept Form",
                "difficulty": difficulty,
                "question": f"A line has x-intercept {a} and y-intercept {b}. Write the equation in intercept form",
                "answer": f"x/{a} + y/{b} = 1",
                "type": "conceptual",
                "solution": f"Intercept form: x/a + y/b = 1, so x/{a} + y/{b} = 1"
            })
    
    return questions


def generate_parallel_perpendicular_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate questions on parallel and perpendicular lines"""
    questions = []
    
    for _ in range(count):
        m1 = random.randint(-5, 5)
        
        if random.choice([True, False]):
            # Parallel lines (same slope)
            m2 = m1
            relation = "parallel"
            condition = "m₁ = m₂"
        else:
            # Perpendicular lines (m1 * m2 = -1)
            if m1 != 0:
                m2 = round(-1 / m1, 2)
            else:
                m2 = "undefined"
            relation = "perpendicular"
            condition = "m₁ × m₂ = -1"
        
        questions.append({
            "topic": f"Coordinate Geometry - {relation.capitalize()} Lines",
            "difficulty": difficulty,
            "question": f"A line has slope {m1}. What is the slope of a line {relation} to it?",
            "answer": str(m2),
            "type": "numerical" if isinstance(m2, (int, float)) else "conceptual",
            "solution": f"For {relation} lines, {condition}. So m₂ = {m2}"
        })
    
    return questions


def generate_angle_between_lines_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate questions on angle between two lines"""
    questions = []
    
    for _ in range(count):
        m1 = random.randint(-3, 3)
        m2 = random.randint(-3, 3)
        
        # tan(θ) = |(m2 - m1) / (1 + m1*m2)|
        if 1 + m1 * m2 != 0:
            tan_theta = abs((m2 - m1) / (1 + m1 * m2))
            angle = round(math.degrees(math.atan(tan_theta)), 2)
            
            questions.append({
                "topic": "Coordinate Geometry - Angle Between Lines",
                "difficulty": difficulty,
                "question": f"Find the acute angle between lines with slopes {m1} and {m2} (in degrees)",
                "answer": angle,
                "type": "numerical",
                "solution": f"tan(θ) = |({m2}-{m1})/(1+{m1}×{m2})| = {round(tan_theta, 3)}, θ = {angle}°"
            })
    
    return questions


def generate_circle_equation_questions(difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
    """Generate questions on circle equations"""
    questions = []
    
    for _ in range(count):
        h, k = random.randint(-5, 5), random.randint(-5, 5)
        r = random.randint(1, 10)
        
        question_type = random.choice(['standard', 'center', 'radius', 'general'])
        
        if question_type == 'standard':
            questions.append({
                "topic": "Coordinate Geometry - Circle Equation",
                "difficulty": difficulty,
                "question": f"Write the equation of a circle with center ({h}, {k}) and radius {r}",
                "answer": f"(x - {h})² + (y - {k})² = {r**2}",
                "type": "conceptual",
                "solution": f"Standard form: (x - h)² + (y - k)² = r², so (x - {h})² + (y - {k})² = {r**2}"
            })
        
        elif question_type == 'center':
            # Given equation, find center
            questions.append({
                "topic": "Coordinate Geometry - Circle Center",
                "difficulty": difficulty,
                "question": f"Find the center of the circle (x - {h})² + (y - {k})² = {r**2}",
                "answer": f"({h}, {k})",
                "type": "conceptual",
                "solution": f"From (x - h)² + (y - k)² = r², center is (h, k) = ({h}, {k})"
            })
        
        elif question_type == 'radius':
            # Given equation, find radius
            questions.append({
                "topic": "Coordinate Geometry - Circle Radius",
                "difficulty": difficulty,
                "question": f"Find the radius of the circle (x - {h})² + (y - {k})² = {r**2}",
                "answer": r,
                "type": "numerical",
                "solution": f"From (x - h)² + (y - k)² = r², r² = {r**2}, so r = {r}"
            })
        
        else:  # general form
            # x² + y² + 2gx + 2fy + c = 0
            # center = (-g, -f), radius = √(g² + f² - c)
            g, f = -h, -k
            c = h**2 + k**2 - r**2
            
            questions.append({
                "topic": "Coordinate Geometry - Circle General Form",
                "difficulty": difficulty,
                "question": f"Convert (x - {h})² + (y - {k})² = {r**2} to general form",
                "answer": f"x² + y² + {2*g}x + {2*f}y + {c} = 0",
                "type": "conceptual",
                "solution": f"Expanding: x² - {2*h}x + {h**2} + y² - {2*k}y + {k**2} = {r**2}"
            })
    
    return questions


def generate_coordinate_geometry_questions(difficulty: str = "medium", count: int = 10,
                                          question_type: str = "all") -> List[Dict[str, Any]]:
    """
    Main function to generate coordinate geometry questions
    
    Args:
        difficulty: "easy", "medium", or "hard"
        count: Number of questions to generate
        question_type: "slope", "distance", "midpoint", "line_equation", "parallel_perpendicular",
                      "angle_between_lines", "circle", or "all"
    
    Returns:
        List of question dictionaries
    """
    if question_type == "slope":
        return generate_slope_questions(difficulty, count)
    elif question_type == "distance":
        return generate_distance_questions(difficulty, count)
    elif question_type == "midpoint":
        return generate_midpoint_questions(difficulty, count)
    elif question_type == "line_equation":
        return generate_line_equation_questions(difficulty, count)
    elif question_type == "parallel_perpendicular":
        return generate_parallel_perpendicular_questions(difficulty, count)
    elif question_type == "angle_between_lines":
        return generate_angle_between_lines_questions(difficulty, count)
    elif question_type == "circle":
        return generate_circle_equation_questions(difficulty, count)
    else:  # all
        questions = []
        per_type = count // 7
        questions.extend(generate_slope_questions(difficulty, per_type))
        questions.extend(generate_distance_questions(difficulty, per_type))
        questions.extend(generate_midpoint_questions(difficulty, per_type))
        questions.extend(generate_line_equation_questions(difficulty, per_type))
        questions.extend(generate_parallel_perpendicular_questions(difficulty, per_type))
        questions.extend(generate_angle_between_lines_questions(difficulty, per_type))
        questions.extend(generate_circle_equation_questions(difficulty, per_type))
        return questions[:count]


# Test block
if __name__ == "__main__":
    print("="*80)
    print("COORDINATE GEOMETRY QUESTION GENERATOR TEST")
    print("="*80)
    
    print("\n1. SLOPE:")
    sample = generate_coordinate_geometry_questions("medium", 2, "slope")
    for q in sample:
        print(f"Q: {q['question']}")
        print(f"A: {q['answer']}\n")
    
    print("2. CIRCLE:")
    sample = generate_coordinate_geometry_questions("medium", 2, "circle")
    for q in sample:
        print(f"Q: {q['question']}")
        print(f"A: {q['answer']}\n")
    
    print("="*80)
    print("✓ Coordinate geometry generator working!")
    print("="*80)

