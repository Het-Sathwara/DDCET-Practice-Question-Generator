"""
Mathematics Question Generators (Legacy Generators)

NOTE: Most math generators have been moved to comprehensive individual files
      in question_generator/maths/ with much more formulas and features.

NEW Comprehensive Generators (in question_generator/maths/):
- Trigonometry (50+ formulas) - trigonometric_functions.py
- Vectors (6 formulas) - vectors.py
- Coordinate Geometry (10 formulas) - coordinate_geometry.py
- Limits (14+ formulas) - limits.py ⭐ NEW!
- Differentiation (20+ formulas) - differentiation.py ⭐ NEW!
- Integration (20+ formulas) - integration.py ⭐ NEW!

REMAINING Generators in this file:
- Matrices & Determinants
- Logarithm
- Statistics

These are kept here until they get comprehensive individual files.
"""

import random
import math
from typing import List, Dict, Any
import sympy as sp
from sympy import symbols, solve, diff, integrate, simplify, expand

from ..core.question_engine import Question, QuestionTemplate


# ==================== MATRICES ====================

class MatricesGenerator(QuestionTemplate):
    """Generate matrices and determinant questions"""
    
    def __init__(self):
        super().__init__("Mathematics", "Determinant and Matrices", "Matrices")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['determinant', 'addition', 'multiplication', 'inverse'])
            
            mult = self._get_difficulty_multiplier(difficulty)
            
            if q_type == 'determinant':
                # Generate 2x2 matrix
                a = random.randint(1, mult["range"][1] // 10)
                b = random.randint(1, mult["range"][1] // 10)
                c = random.randint(1, mult["range"][1] // 10)
                d = random.randint(1, mult["range"][1] // 10)
                
                det = a * d - b * c
                
                question_text = f"Find the determinant of the matrix:\n|{a}  {b}|\n|{c}  {d}|"
                
                distractors = self._generate_distractor_options(det, 3)
                options = [str(det)] + [str(int(d)) for d in distractors]
                random.shuffle(options)
                
                questions.append(Question(
                    subject=self.subject,
                    chapter=self.chapter,
                    subtopic=self.subtopic,
                    difficulty=difficulty,
                    question_type="mcq",
                    question_text=question_text,
                    answer=str(det),
                    options=options,
                    solution=f"det = ({a})({d}) - ({b})({c}) = {det}",
                    tags=["matrices", "determinant"]
                ))
            
            elif q_type == 'addition':
                # Matrix addition
                a1, b1 = random.randint(1, 10), random.randint(1, 10)
                c1, d1 = random.randint(1, 10), random.randint(1, 10)
                a2, b2 = random.randint(1, 10), random.randint(1, 10)
                c2, d2 = random.randint(1, 10), random.randint(1, 10)
                
                a_sum = a1 + a2
                
                question_text = f"Add the matrices and find element (1,1):\n|{a1}  {b1}|   |{a2}  {b2}|\n|{c1}  {d1}| + |{c2}  {d2}|"
                
                questions.append(Question(
                    subject=self.subject,
                    chapter=self.chapter,
                    subtopic=self.subtopic,
                    difficulty=difficulty,
                    question_type="integer",
                    question_text=question_text,
                    answer=a_sum,
                    solution=f"(1,1) element = {a1} + {a2} = {a_sum}",
                    tags=["matrices", "addition"]
                ))
        
        return questions


# ==================== LOGARITHM ====================

class LogarithmGenerator(QuestionTemplate):
    """Generate logarithm questions"""
    
    def __init__(self):
        super().__init__("Mathematics", "Logarithm", "Laws of Logarithm")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            # Simple log law questions
            laws = [
                ("log(ab)", "log(a) + log(b)"),
                ("log(a/b)", "log(a) - log(b)"),
                ("log(a^n)", "n·log(a)"),
                ("log_a(a)", "1"),
                ("log_a(1)", "0"),
            ]
            
            law = random.choice(laws)
            
            questions.append(Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="conceptual",
                question_text=f"Simplify: {law[0]}",
                answer=law[1],
                solution=f"{law[0]} = {law[1]}",
                tags=["logarithm", "laws"]
            ))
        
        return questions


# ==================== STATISTICS ====================

class StatisticsGenerator(QuestionTemplate):
    """Generate statistics questions (mean, median, mode)"""
    
    def __init__(self):
        super().__init__("Mathematics", "Statistics", "Mean, Median, Mode")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            # Generate ungrouped data
            data_size = random.randint(5, 10) if difficulty == "easy" else random.randint(8, 15)
            data = [random.randint(1, 50) for _ in range(data_size)]
            
            q_type = random.choice(['mean', 'median', 'mode'])
            
            if q_type == 'mean':
                mean = sum(data) / len(data)
                mean = round(mean, 2)
                
                questions.append(Question(
                    subject=self.subject,
                    chapter=self.chapter,
                    subtopic=self.subtopic,
                    difficulty=difficulty,
                    question_type="numerical",
                    question_text=f"Find the mean of: {data}",
                    answer=mean,
                    solution=f"Mean = sum/n = {sum(data)}/{len(data)} = {mean}",
                    tags=["statistics", "mean"]
                ))
            
            elif q_type == 'median':
                sorted_data = sorted(data)
                n = len(sorted_data)
                if n % 2 == 0:
                    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
                else:
                    median = sorted_data[n//2]
                median = round(median, 2)
                
                questions.append(Question(
                    subject=self.subject,
                    chapter=self.chapter,
                    subtopic=self.subtopic,
                    difficulty=difficulty,
                    question_type="numerical",
                    question_text=f"Find the median of: {data}",
                    answer=median,
                    solution=f"Sorted: {sorted_data}, Median = {median}",
                    tags=["statistics", "median"]
                ))
            
            else:  # mode
                from collections import Counter
                counts = Counter(data)
                mode = counts.most_common(1)[0][0]
                
                questions.append(Question(
                    subject=self.subject,
                    chapter=self.chapter,
                    subtopic=self.subtopic,
                    difficulty=difficulty,
                    question_type="numerical",
                    question_text=f"Find the mode of: {data}",
                    answer=mode,
                    solution=f"Most frequent value = {mode}",
                    tags=["statistics", "mode"]
                ))
        
        return questions

