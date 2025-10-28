"""
Mathematics Question Generators - ADVANCED & BALANCED
Matrix generator with proper equations and difficulty scaling
"""

import random
import math
from typing import List, Dict, Any
from collections import Counter
import sympy as sp
from sympy import symbols, solve, Matrix, eye, simplify
from sympy import log as sp_log, ln as sp_ln

from ..core.question_engine import Question, QuestionTemplate


# ==================== MATRICES & DETERMINANTS ====================

class MatricesGenerator(QuestionTemplate):
    """Advanced matrices generator with proper difficulty and balance"""
    
    def __init__(self):
        super().__init__("Mathematics", "Determinant and Matrices", "Matrices")
        self.used_questions = set()  # Track to avoid repeats
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        self.used_questions = set()  # Reset for each batch
        
        # BALANCED question type distribution
        if difficulty == "easy":
            types = {
                'determinant_2x2': 3,
                'addition': 2,
                'scalar_mult': 2,
                'subtraction': 2,
                'transpose': 1
            }
        elif difficulty == "medium":
            types = {
                'determinant_2x2': 2,
                'determinant_3x3': 2,
                'multiplication_2x2': 2,
                'transpose': 2,
                'inverse_2x2': 2
            }
        else:  # hard - REAL ADVANCED QUESTIONS
            types = {
                'matrix_equation_simple': 3,  # AX = B
                'matrix_equation_inverse': 3,  # AX = I
                'determinant_3x3': 2,
                'system_equations': 2
            }
        
        # Generate balanced questions
        for q_type, num in types.items():
            for _ in range(num):
                if len(questions) >= count:
                    break
                q = self._generate_single(q_type, difficulty)
                if q:
                    questions.append(q)
        
        return questions[:count]
    
    def _generate_single(self, q_type: str, difficulty: str) -> Question:
        """Generate a single non-repeating question"""
        max_attempts = 10
        for _ in range(max_attempts):
            q = self._create_question(q_type, difficulty)
            q_hash = hash(q.question_text)
            if q_hash not in self.used_questions:
                self.used_questions.add(q_hash)
                return q
        return self._create_question(q_type, difficulty)  # Fallback
    
    def _create_question(self, q_type: str, difficulty: str) -> Question:
        """Create specific question type"""
        
        if q_type == 'determinant_2x2':
            a, b = random.randint(-5, 10), random.randint(-5, 10)
            c, d = random.randint(-5, 10), random.randint(-5, 10)
            det = a * d - b * c
            
            question_text = f"Find |A| if A = [{a:3d}  {b:3d}]\n                   [{c:3d}  {d:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=question_text, answer=det,
                solution=f"|A| = ({a})({d}) - ({b})({c}) = {a*d} - {b*c} = {det}",
                tags=["determinant", "2x2"]
            )
        
        elif q_type == 'determinant_3x3':
            a11, a12, a13 = random.randint(-3, 5), random.randint(-3, 5), random.randint(-3, 5)
            a21, a22, a23 = random.randint(-3, 5), random.randint(-3, 5), random.randint(-3, 5)
            a31, a32, a33 = random.randint(-3, 5), random.randint(-3, 5), random.randint(-3, 5)
            
            det = a11*(a22*a33 - a23*a32) - a12*(a21*a33 - a23*a31) + a13*(a21*a32 - a22*a31)
            
            question_text = f"Find |A| if A = [{a11:3d}  {a12:3d}  {a13:3d}]\n                   [{a21:3d}  {a22:3d}  {a23:3d}]\n                   [{a31:3d}  {a32:3d}  {a33:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=question_text, answer=det,
                solution=f"Expand along R1: |A| = {det}",
                tags=["determinant", "3x3"]
            )
        
        elif q_type == 'addition':
            a1, b1 = random.randint(-5, 10), random.randint(-5, 10)
            c1, d1 = random.randint(-5, 10), random.randint(-5, 10)
            a2, b2 = random.randint(-5, 10), random.randint(-5, 10)
            c2, d2 = random.randint(-5, 10), random.randint(-5, 10)
            
            question_text = f"If A = [{a1:3d}  {b1:3d}] and B = [{a2:3d}  {b2:3d}], find A+B\n       [{c1:3d}  {d1:3d}]         [{c2:3d}  {d2:3d}]"
            answer = f"[{a1+a2:3d}  {b1+b2:3d}]\n[{c1+c2:3d}  {d1+d2:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"A+B = {answer}", tags=["matrix", "addition"]
            )
        
        elif q_type == 'subtraction':
            a1, b1 = random.randint(-5, 10), random.randint(-5, 10)
            c1, d1 = random.randint(-5, 10), random.randint(-5, 10)
            a2, b2 = random.randint(-5, 10), random.randint(-5, 10)
            c2, d2 = random.randint(-5, 10), random.randint(-5, 10)
            
            question_text = f"If A = [{a1:3d}  {b1:3d}] and B = [{a2:3d}  {b2:3d}], find A-B\n       [{c1:3d}  {d1:3d}]         [{c2:3d}  {d2:3d}]"
            answer = f"[{a1-a2:3d}  {b1-b2:3d}]\n[{c1-c2:3d}  {d1-d2:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"A-B = {answer}", tags=["matrix", "subtraction"]
            )
        
        elif q_type == 'scalar_mult':
            k = random.randint(2, 5)
            a, b = random.randint(-5, 10), random.randint(-5, 10)
            c, d = random.randint(-5, 10), random.randint(-5, 10)
            
            question_text = f"If A = [{a:3d}  {b:3d}], find {k}A\n       [{c:3d}  {d:3d}]"
            answer = f"[{k*a:3d}  {k*b:3d}]\n[{k*c:3d}  {k*d:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"{k}A = {answer}", tags=["matrix", "scalar"]
            )
        
        elif q_type == 'multiplication_2x2':
            a1, b1 = random.randint(-3, 5), random.randint(-3, 5)
            c1, d1 = random.randint(-3, 5), random.randint(-3, 5)
            a2, b2 = random.randint(-3, 5), random.randint(-3, 5)
            c2, d2 = random.randint(-3, 5), random.randint(-3, 5)
            
            r11, r12 = a1*a2 + b1*c2, a1*b2 + b1*d2
            r21, r22 = c1*a2 + d1*c2, c1*b2 + d1*d2
            
            question_text = f"If A = [{a1:3d}  {b1:3d}] and B = [{a2:3d}  {b2:3d}], find AB\n       [{c1:3d}  {d1:3d}]         [{c2:3d}  {d2:3d}]"
            answer = f"[{r11:3d}  {r12:3d}]\n[{r21:3d}  {r22:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"AB = {answer}", tags=["matrix", "multiplication"]
            )
        
        elif q_type == 'transpose':
            a, b = random.randint(-5, 10), random.randint(-5, 10)
            c, d = random.randint(-5, 10), random.randint(-5, 10)
            
            question_text = f"If A = [{a:3d}  {b:3d}], find A^T\n       [{c:3d}  {d:3d}]"
            answer = f"[{a:3d}  {c:3d}]\n[{b:3d}  {d:3d}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"A^T = {answer}", tags=["matrix", "transpose"]
            )
        
        elif q_type == 'inverse_2x2':
            while True:
                a, b = random.randint(-3, 5), random.randint(-3, 5)
                c, d = random.randint(-3, 5), random.randint(-3, 5)
                det = a*d - b*c
                if det != 0:
                    break
            
            question_text = f"If A = [{a:3d}  {b:3d}], find A^(-1)\n       [{c:3d}  {d:3d}]"
            answer = f"(1/{det})[{d:3d}  {-b:3d}] = [{d/det:.2f}  {-b/det:.2f}]\n      [{-c:3d}  {a:3d}]   [{-c/det:.2f}  {a/det:.2f}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"A^(-1) = (1/|A|)adj(A), |A|={det}\n{answer}",
                tags=["matrix", "inverse"]
            )
        
        elif q_type == 'matrix_equation_simple':
            # Solve AX = B for X, where X = A^(-1)B
            while True:
                a, b = random.randint(1, 4), random.randint(-2, 2)
                c, d = random.randint(-2, 2), random.randint(1, 4)
                det = a*d - b*c
                if det != 0:
                    break
            
            b1, b2 = random.randint(-5, 5), random.randint(-5, 5)
            
            # Calculate X = A^(-1)B
            x1 = (d*b1 - b*b2) / det
            x2 = (-c*b1 + a*b2) / det
            
            question_text = f"Solve for X in AX = B where:\nA = [{a:3d}  {b:3d}], B = [{b1:3d}]\n    [{c:3d}  {d:3d}]       [{b2:3d}]"
            answer = f"X = [{x1:.1f}]\n    [{x2:.1f}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"X = A^(-1)B\n{answer}",
                tags=["matrix", "equation", "advanced"]
            )
        
        elif q_type == 'matrix_equation_inverse':
            # Solve AX = I for X (finding inverse)
            while True:
                a, b = random.randint(1, 4), random.randint(-2, 2)
                c, d = random.randint(-2, 2), random.randint(1, 4)
                det = a*d - b*c
                if det != 0:
                    break
            
            question_text = f"Solve for X in AX = I where:\nA = [{a:3d}  {b:3d}]\n    [{c:3d}  {d:3d}]\n(I is identity matrix)"
            answer = f"X = [{d/det:.2f}  {-b/det:.2f}]\n    [{-c/det:.2f}  {a/det:.2f}]"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"X = A^(-1) (since AX = I means X = A^(-1))\n{answer}",
                tags=["matrix", "equation", "inverse", "advanced"]
            )
        
        elif q_type == 'system_equations':
            # System: ax + by = e, cx + dy = f
            a, b = random.randint(1, 4), random.randint(1, 4)
            c, d = random.randint(1, 4), random.randint(1, 4)
            det = a*d - b*c
            
            if det == 0:
                a, b, c, d = 2, 1, 1, 3  # Fallback
                det = a*d - b*c
            
            x_val, y_val = random.randint(1, 5), random.randint(1, 5)
            e, f = a*x_val + b*y_val, c*x_val + d*y_val
            
            question_text = f"Solve using matrix method:\n{a}x + {b}y = {e}\n{c}x + {d}y = {f}"
            answer = f"x = {x_val}, y = {y_val}"
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=question_text, answer=answer,
                solution=f"[{a} {b}][x] = [{e}]\n[{c} {d}][y]   [{f}]\nSolving: {answer}",
                tags=["matrix", "system", "advanced"]
            )


# ==================== LOGARITHM ====================

class LogarithmGenerator(QuestionTemplate):
    """Logarithm with proper difficulty and no repeats"""
    
    def __init__(self):
        super().__init__("Mathematics", "Logarithm", "Laws and Equations")
        self.used_questions = set()
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        self.used_questions = set()
        
        # Balanced distribution
        if difficulty == "easy":
            types = {'basic_law': 3, 'simple_eval': 3, 'basic_properties': 4}
        elif difficulty == "medium":
            types = {'expand': 3, 'condense': 2, 'solve_simple': 3, 'change_base': 2}
        else:  # hard
            types = {'solve_equation': 4, 'word_problem': 3, 'complex_solve': 3}
        
        for q_type, num in types.items():
            for _ in range(num):
                if len(questions) >= count:
                    break
                q = self._generate_single(q_type, difficulty)
                if q:
                    questions.append(q)
        
        return questions[:count]
    
    def _generate_single(self, q_type: str, difficulty: str) -> Question:
        max_attempts = 10
        for _ in range(max_attempts):
            q = self._create_question(q_type, difficulty)
            q_hash = hash(q.question_text)
            if q_hash not in self.used_questions:
                self.used_questions.add(q_hash)
                return q
        return self._create_question(q_type, difficulty)
    
    def _create_question(self, q_type: str, difficulty: str) -> Question:
        # [Previous logarithm code remains the same, just wrapped in _create_question]
        # I'll keep the same logic as before for logarithm since it was working
        
        if q_type == 'basic_law':
            law_type = random.choice(['product', 'quotient', 'power'])
            if law_type == 'product':
                a, b = random.randint(2, 10), random.randint(2, 10)
                return Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=f"Simplify: log({a}) + log({b})",
                    answer=f"log({a*b})",
                    solution=f"log(a) + log(b) = log(ab) = log({a*b})",
                    tags=["logarithm", "laws"]
                )
            elif law_type == 'quotient':
                a, b = random.randint(2, 10), random.randint(2, 10)
                return Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=f"Simplify: log({a*b}) - log({b})",
                    answer=f"log({a})",
                    solution=f"log(a) - log(b) = log(a/b) = log({a})",
                    tags=["logarithm", "laws"]
                )
            else:  # power
                a, n = random.randint(2, 10), random.randint(2, 4)
                return Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="conceptual",
                    question_text=f"Simplify: log({a}^{n})",
                    answer=f"{n}log({a})",
                    solution=f"log(a^n) = n·log(a) = {n}log({a})",
                    tags=["logarithm", "laws"]
                )
        
        elif q_type == 'simple_eval':
            base = random.choice([2, 3, 5, 10])
            power = random.randint(2, 4)
            value = base ** power
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=f"Evaluate: log_{base}({value})",
                answer=power,
                solution=f"log_{base}({value}) = log_{base}({base}^{power}) = {power}",
                tags=["logarithm", "evaluation"]
            )
        
        elif q_type == 'expand':
            a, b = random.randint(2, 10), random.randint(2, 10)
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=f"Expand: log({a}×{b})",
                answer=f"log({a}) + log({b})",
                solution=f"log(ab) = log(a) + log(b)",
                tags=["logarithm", "expand"]
            )
        
        elif q_type == 'condense':
            a, b = random.randint(2, 10), random.randint(2, 10)
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=f"Write as single log: log({a}) + log({b})",
                answer=f"log({a*b})",
                solution=f"log({a}) + log({b}) = log({a*b})",
                tags=["logarithm", "condense"]
            )
        
        elif q_type == 'solve_simple':
            base = random.choice([2, 3, 5])
            power = random.randint(2, 4)
            value = base ** power
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=f"Solve: log_{base}(x) = {power}",
                answer=value,
                solution=f"x = {base}^{power} = {value}",
                tags=["logarithm", "solve"]
            )
        
        elif q_type == 'change_base':
            old_base = random.choice([2, 3, 5])
            val = random.randint(5, 20)
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="conceptual",
                question_text=f"Convert log_{old_base}({val}) to base 10",
                answer=f"log({val})/log({old_base})",
                solution=f"log_a(b) = log(b)/log(a)",
                tags=["logarithm", "change_base"]
            )
        
        elif q_type == 'solve_equation':
            a = random.randint(1, 4)
            product = random.choice([10, 12, 15, 20])
            x = symbols('x')
            equation = x * (x + a) - product
            solutions = solve(equation, x)
            positive_sol = [s for s in solutions if s > 0][0]
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=f"Solve: log(x) + log(x+{a}) = log({product})",
                answer=int(positive_sol),
                solution=f"x(x+{a}) = {product}, x = {int(positive_sol)}",
                tags=["logarithm", "equations"]
            )
        
        elif q_type == 'word_problem':
            initial = random.choice([100, 200, 500])
            rate = random.choice([2, 3, 5])
            years = random.randint(2, 4)
            final = initial * (rate ** years)
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=f"Population grows from {initial} to {final} in {years} years. If P = {initial}×r^{years}, find r",
                answer=rate,
                solution=f"r^{years} = {rate**years}, r = {rate}",
                tags=["logarithm", "word_problem"]
            )
        
        elif q_type == 'complex_solve':
            base = random.choice([2, 3])
            k = random.randint(2, 4)
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text=f"Solve: log_{base}(x) = {k}",
                answer=base ** k,
                solution=f"x = {base}^{k} = {base**k}",
                tags=["logarithm", "solve"]
            )
        
        else:  # basic_properties
            return Question(
                subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                difficulty=difficulty, question_type="integer",
                question_text="Evaluate: log₁₀(1000)",
                answer=3,
                solution="log₁₀(1000) = log₁₀(10³) = 3",
                tags=["logarithm", "properties"]
            )


# ==================== STATISTICS ====================

class StatisticsGenerator(QuestionTemplate):
    """Statistics - unchanged"""
    
    def __init__(self):
        super().__init__("Mathematics", "Statistics", "Mean, Median, Mode")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        for _ in range(count):
            data_size = random.randint(5, 8) if difficulty == "easy" else random.randint(8, 12)
            data = [random.randint(1, 50) for _ in range(data_size)]
            q_type = random.choice(['mean', 'median', 'mode'])
            
            if q_type == 'mean':
                mean = round(sum(data) / len(data), 2)
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="numerical",
                    question_text=f"Find mean: {data}",
                    answer=mean,
                    solution=f"Mean = {sum(data)}/{len(data)} = {mean}",
                    tags=["statistics", "mean"]
                ))
            elif q_type == 'median':
                sorted_data = sorted(data)
                n = len(sorted_data)
                median = (sorted_data[n//2-1] + sorted_data[n//2])/2 if n%2==0 else sorted_data[n//2]
                median = round(median, 2)
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="numerical",
                    question_text=f"Find median: {data}",
                    answer=median,
                    solution=f"Sorted: {sorted_data}, Median = {median}",
                    tags=["statistics", "median"]
                ))
            else:  # mode
                mode = Counter(data).most_common(1)[0][0]
                questions.append(Question(
                    subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
                    difficulty=difficulty, question_type="numerical",
                    question_text=f"Find mode: {data}",
                    answer=mode,
                    solution=f"Mode = {mode}",
                    tags=["statistics", "mode"]
                ))
        
        return questions
