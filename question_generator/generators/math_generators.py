"""
Mathematics Question Generators (Legacy Generators) - IMPROVED

Matrices & Logarithm now match actual DDCET exam patterns with proper difficulty scaling.
"""

import random
import math
from typing import List, Dict, Any
from collections import Counter
import sympy as sp
from sympy import symbols, solve, diff, integrate, simplify, expand, log, ln

from ..core.question_engine import Question, QuestionTemplate


# ==================== MATRICES & DETERMINANTS ====================

class MatricesGenerator(QuestionTemplate):
    """Generate matrices and determinant questions - Realistic exam-style"""
    
    def __init__(self):
        super().__init__("Mathematics", "Determinant and Matrices", "Matrices")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            # Difficulty-based question types
            if difficulty == "easy":
                q_types = ['determinant_2x2', 'addition', 'scalar_mult']
            elif difficulty == "medium":
                q_types = ['determinant_2x2', 'determinant_3x3', 'addition', 'subtraction', 'multiplication_2x2', 'transpose']
            else:  # hard
                q_types = ['determinant_3x3', 'inverse_2x2', 'multiplication_2x2', 'properties']
            
            q_type = random.choice(q_types)
            
            if q_type == 'determinant_2x2':
                a, b = random.randint(-5, 10), random.randint(-5, 10)
                c, d = random.randint(-5, 10), random.randint(-5, 10)
                det = a * d - b * c
                
                question_text = f"Find the determinant:\n|{a:3d}  {b:3d}|\n|{c:3d}  {d:3d}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=det,
                    solution=f"|A| = ({a})×({d}) - ({b})×({c}) = {a*d} - {b*c} = {det}",
                    tags=["determinant", "2x2"]
                ))
            
            elif q_type == 'determinant_3x3':
                a11, a12, a13 = random.randint(-3, 5), random.randint(-3, 5), random.randint(-3, 5)
                a21, a22, a23 = random.randint(-3, 5), random.randint(-3, 5), random.randint(-3, 5)
                a31, a32, a33 = random.randint(-3, 5), random.randint(-3, 5), random.randint(-3, 5)
                
                det = a11*(a22*a33 - a23*a32) - a12*(a21*a33 - a23*a31) + a13*(a21*a32 - a22*a31)
                
                question_text = f"Find the determinant (expand along Row 1):\n|{a11:3d}  {a12:3d}  {a13:3d}|\n|{a21:3d}  {a22:3d}  {a23:3d}|\n|{a31:3d}  {a32:3d}  {a33:3d}|"
                solution = f"Expanding along R1:\n|A| = {a11}×(minor) - {a12}×(minor) + {a13}×(minor) = {det}"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=det, solution=solution,
                    tags=["determinant", "3x3"]
                ))
            
            elif q_type == 'addition':
                a1, b1 = random.randint(-5, 10), random.randint(-5, 10)
                c1, d1 = random.randint(-5, 10), random.randint(-5, 10)
                a2, b2 = random.randint(-5, 10), random.randint(-5, 10)
                c2, d2 = random.randint(-5, 10), random.randint(-5, 10)
                
                question_text = f"If A = |{a1:3d}  {b1:3d}| and B = |{a2:3d}  {b2:3d}|, find A + B\n     |{c1:3d}  {d1:3d}|         |{c2:3d}  {d2:3d}|"
                answer_matrix = f"|{a1+a2:3d}  {b1+b2:3d}|\n|{c1+c2:3d}  {d1+d2:3d}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer_matrix,
                    solution=f"A + B = {answer_matrix}",
                    tags=["matrix", "addition"]
                ))
            
            elif q_type == 'subtraction':
                a1, b1 = random.randint(-5, 10), random.randint(-5, 10)
                c1, d1 = random.randint(-5, 10), random.randint(-5, 10)
                a2, b2 = random.randint(-5, 10), random.randint(-5, 10)
                c2, d2 = random.randint(-5, 10), random.randint(-5, 10)
                
                question_text = f"If A = |{a1:3d}  {b1:3d}| and B = |{a2:3d}  {b2:3d}|, find A - B\n     |{c1:3d}  {d1:3d}|         |{c2:3d}  {d2:3d}|"
                answer_matrix = f"|{a1-a2:3d}  {b1-b2:3d}|\n|{c1-c2:3d}  {d1-d2:3d}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer_matrix,
                    solution=f"A - B = {answer_matrix}",
                    tags=["matrix", "subtraction"]
                ))
            
            elif q_type == 'scalar_mult':
                k = random.randint(2, 5)
                a, b = random.randint(-5, 10), random.randint(-5, 10)
                c, d = random.randint(-5, 10), random.randint(-5, 10)
                
                question_text = f"If A = |{a:3d}  {b:3d}|, find {k}A\n     |{c:3d}  {d:3d}|"
                answer_matrix = f"|{k*a:3d}  {k*b:3d}|\n|{k*c:3d}  {k*d:3d}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer_matrix,
                    solution=f"{k}A = {answer_matrix}",
                    tags=["matrix", "scalar"]
                ))
            
            elif q_type == 'multiplication_2x2':
                a1, b1 = random.randint(-3, 5), random.randint(-3, 5)
                c1, d1 = random.randint(-3, 5), random.randint(-3, 5)
                a2, b2 = random.randint(-3, 5), random.randint(-3, 5)
                c2, d2 = random.randint(-3, 5), random.randint(-3, 5)
                
                r11 = a1*a2 + b1*c2
                r12 = a1*b2 + b1*d2
                r21 = c1*a2 + d1*c2
                r22 = c1*b2 + d1*d2
                
                question_text = f"If A = |{a1:3d}  {b1:3d}| and B = |{a2:3d}  {b2:3d}|, find AB\n     |{c1:3d}  {d1:3d}|         |{c2:3d}  {d2:3d}|"
                answer_matrix = f"|{r11:3d}  {r12:3d}|\n|{r21:3d}  {r22:3d}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer_matrix,
                    solution=f"AB = {answer_matrix}",
                    tags=["matrix", "multiplication"]
                ))
            
            elif q_type == 'inverse_2x2':
                while True:
                    a, b = random.randint(-3, 5), random.randint(-3, 5)
                    c, d = random.randint(-3, 5), random.randint(-3, 5)
                    det = a*d - b*c
                    if det != 0:
                        break
                
                question_text = f"Find the inverse of A = |{a:3d}  {b:3d}|\n                        |{c:3d}  {d:3d}|"
                answer_text = f"(1/{det})|{d:3d}  {-b:3d}| = |{d/det:.2f}  {-b/det:.2f}|\n      |{-c:3d}  {a:3d}|   |{-c/det:.2f}  {a/det:.2f}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer_text,
                    solution=f"A⁻¹ = (1/|A|)×adj(A), |A| = {det}\nA⁻¹ = {answer_text}",
                    tags=["matrix", "inverse"]
                ))
            
            elif q_type == 'transpose':
                a, b = random.randint(-5, 10), random.randint(-5, 10)
                c, d = random.randint(-5, 10), random.randint(-5, 10)
                
                question_text = f"Find the transpose of A = |{a:3d}  {b:3d}|\n                           |{c:3d}  {d:3d}|"
                answer_matrix = f"|{a:3d}  {c:3d}|\n|{b:3d}  {d:3d}|"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer_matrix,
                    solution=f"Aᵀ = {answer_matrix}",
                    tags=["matrix", "transpose"]
                ))
            
            elif q_type == 'properties':
                prop_type = random.choice(['identity', 'symmetric', 'diagonal'])
                
                if prop_type == 'identity':
                    question_text = "What is the determinant of the 2×2 identity matrix I?"
                    questions.append(Question(
                        subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                        difficulty=difficulty, question_type="integer",
                        question_text=question_text, answer=1,
                        solution="|I| = |1 0| = (1)(1) - (0)(0) = 1\n    |0 1|",
                        tags=["matrix", "properties"]
                    ))
                elif prop_type == 'symmetric':
                    a = random.randint(1, 5)
                    b = random.randint(1, 5)
                    c = random.randint(1, 5)
                    question_text = f"Is the matrix |{a}  {b}| symmetric?\n                |{b}  {c}|"
                    questions.append(Question(
                        subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                        difficulty=difficulty, question_type="conceptual",
                        question_text=question_text, answer="Yes",
                        solution=f"A = Aᵀ since a₁₂ = a₂₁ = {b}",
                        tags=["matrix", "properties"]
                    ))
                else:  # diagonal
                    a = random.randint(1, 5)
                    b = random.randint(1, 5)
                    question_text = f"Find the determinant of diagonal matrix |{a}  0|\n                                              |0  {b}|"
                    questions.append(Question(
                        subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                        difficulty=difficulty, question_type="integer",
                        question_text=question_text, answer=a*b,
                        solution=f"|A| = {a}×{b} = {a*b} (product of diagonal elements)",
                        tags=["matrix", "properties"]
                    ))
        
        return questions


# ==================== LOGARITHM ====================

class LogarithmGenerator(QuestionTemplate):
    """Generate logarithm questions - With actual equations and problem-solving"""
    
    def __init__(self):
        super().__init__("Mathematics", "Logarithm", "Laws and Equations")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            # Difficulty-based question types
            if difficulty == "easy":
                q_types = ['basic_law', 'simple_eval', 'basic_properties']
            elif difficulty == "medium":
                q_types = ['expand', 'condense', 'solve_simple', 'change_base']
            else:  # hard
                q_types = ['solve_equation', 'solve_complex', 'word_problem']
            
            q_type = random.choice(q_types)
            
            if q_type == 'basic_law':
                law_type = random.choice(['product', 'quotient', 'power', 'one', 'base'])
                
                if law_type == 'product':
                    a, b = random.randint(2, 10), random.randint(2, 10)
                    question_text = f"Simplify: log({a}) + log({b})"
                    answer = f"log({a*b})"
                    solution = f"log(a) + log(b) = log(ab) = log({a*b})"
                elif law_type == 'quotient':
                    a, b = random.randint(2, 10), random.randint(2, 10)
                    question_text = f"Simplify: log({a*b}) - log({b})"
                    answer = f"log({a})"
                    solution = f"log(a) - log(b) = log(a/b) = log({a})"
                elif law_type == 'power':
                    a, n = random.randint(2, 10), random.randint(2, 4)
                    question_text = f"Simplify: log({a}^{n})"
                    answer = f"{n}log({a})"
                    solution = f"log(aⁿ) = n·log(a) = {n}log({a})"
                elif law_type == 'one':
                    base = random.randint(2, 10)
                    question_text = f"Evaluate: log_{base}(1)"
                    answer = "0"
                    solution = "logₐ(1) = 0 for any base a"
                else:  # base
                    base = random.randint(2, 10)
                    question_text = f"Evaluate: log_{base}({base})"
                    answer = "1"
                    solution = f"logₐ(a) = 1"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "laws"]
                ))
            
            elif q_type == 'simple_eval':
                base = random.choice([2, 3, 5, 10])
                power = random.randint(2, 4)
                value = base ** power
                
                question_text = f"Evaluate: log_{base}({value})"
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=power,
                    solution=f"log_{base}({value}) = log_{base}({base}^{power}) = {power}",
                    tags=["logarithm", "evaluation"]
                ))
            
            elif q_type == 'expand':
                a, b = random.randint(2, 10), random.randint(2, 10)
                question_text = f"Expand: log({a}×{b})"
                answer = f"log({a}) + log({b})"
                solution = f"log(ab) = log(a) + log(b) = log({a}) + log({b})"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "expand"]
                ))
            
            elif q_type == 'condense':
                a, b = random.randint(2, 10), random.randint(2, 10)
                question_text = f"Write as a single logarithm: log({a}) + log({b})"
                answer = f"log({a*b})"
                solution = f"log({a}) + log({b}) = log({a}×{b}) = log({a*b})"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "condense"]
                ))
            
            elif q_type == 'solve_simple':
                base = random.choice([2, 3, 5])
                power = random.randint(2, 4)
                value = base ** power
                
                question_text = f"Solve for x: log_{base}(x) = {power}"
                answer = value
                solution = f"log_{base}(x) = {power}\nx = {base}^{power} = {value}"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "solve"]
                ))
            
            elif q_type == 'change_base':
                old_base = random.choice([2, 3, 5])
                new_base = random.choice([10, 'e'])
                val = random.randint(2, 20)
                
                question_text = f"Convert log_{old_base}({val}) to base {new_base}"
                if new_base == 10:
                    answer = f"log({val})/log({old_base})"
                    solution = f"logₐ(b) = log₁₀(b)/log₁₀(a) = log({val})/log({old_base})"
                else:
                    answer = f"ln({val})/ln({old_base})"
                    solution = f"logₐ(b) = ln(b)/ln(a) = ln({val})/ln({old_base})"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "change_base"]
                ))
            
            elif q_type == 'solve_equation':
                # log(x) + log(x+3) = log(10)
                # x(x+3) = 10
                # x² + 3x - 10 = 0
                # (x+5)(x-2) = 0, x = 2 (x>0)
                a = random.randint(1, 4)
                product = random.choice([10, 12, 15, 20])
                
                question_text = f"Solve: log(x) + log(x+{a}) = log({product})"
                x = symbols('x')
                equation = x * (x + a) - product
                solutions = solve(equation, x)
                positive_sol = [s for s in solutions if s > 0][0]
                
                answer = int(positive_sol)
                solution = f"log(x) + log(x+{a}) = log({product})\nlog(x(x+{a})) = log({product})\nx(x+{a}) = {product}\nx = {answer}"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "equations"]
                ))
            
            elif q_type == 'solve_complex':
                base = random.choice([2, 3])
                k = random.randint(1, 3)
                
                question_text = f"Solve: log_{base}(x) = {k}"
                answer = base ** k
                solution = f"log_{base}(x) = {k}\nx = {base}^{k} = {answer}"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "solve"]
                ))
            
            elif q_type == 'word_problem':
                initial = random.choice([100, 200, 500, 1000])
                rate = random.choice([2, 3, 5])
                years = random.randint(2, 4)
                final = initial * (rate ** years)
                
                question_text = f"A population grows from {initial} to {final} in {years} years at rate r per year. If P = {initial}×r^{years}, solve for the yearly growth rate r."
                answer = rate
                solution = f"{final} = {initial}×r^{years}\nr^{years} = {final}/{initial} = {rate**years}\nr = {rate}"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "word_problem"]
                ))
            
            elif q_type == 'basic_properties':
                prop_type = random.choice(['log10_100', 'log10_1000', 'ln_e', 'ln_1'])
                
                if prop_type == 'log10_100':
                    question_text = "Evaluate: log₁₀(100)"
                    answer = 2
                    solution = "log₁₀(100) = log₁₀(10²) = 2"
                elif prop_type == 'log10_1000':
                    question_text = "Evaluate: log₁₀(1000)"
                    answer = 3
                    solution = "log₁₀(1000) = log₁₀(10³) = 3"
                elif prop_type == 'ln_e':
                    question_text = "Evaluate: ln(e)"
                    answer = 1
                    solution = "ln(e) = logₑ(e) = 1"
                else:  # ln_1
                    question_text = "Evaluate: ln(1)"
                    answer = 0
                    solution = "ln(1) = 0"
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="integer",
                    question_text=question_text, answer=answer, solution=solution,
                    tags=["logarithm", "properties"]
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
            data_size = random.randint(5, 8) if difficulty == "easy" else random.randint(8, 12)
            data = [random.randint(1, 50) for _ in range(data_size)]
            
            q_type = random.choice(['mean', 'median', 'mode'])
            
            if q_type == 'mean':
                mean = sum(data) / len(data)
                mean = round(mean, 2)
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="numerical",
                    question_text=f"Find the mean of: {data}",
                    answer=mean,
                    solution=f"Mean = Σx/n = {sum(data)}/{len(data)} = {mean}",
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
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="numerical",
                    question_text=f"Find the median of: {data}",
                    answer=median,
                    solution=f"Sorted: {sorted_data}\nMedian = {median}",
                    tags=["statistics", "median"]
                ))
            
            else:  # mode
                counts = Counter(data)
                mode = counts.most_common(1)[0][0]
                
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="numerical",
                    question_text=f"Find the mode of: {data}",
                    answer=mode,
                    solution=f"Most frequent value = {mode}",
                    tags=["statistics", "mode"]
                ))
        
        return questions
