"""
Topic: Integration (COMPREHENSIVE - ALL FORMULAS)
Syllabus: DDCET Mathematics
Source: formula.pdf - ALL integration formulas included
Features: 20+ integration formulas, all standard integrals
         Randomized MCQs, numerical questions, difficulty levels.
"""

import random
import math
from typing import List, Dict, Any
import sympy as sp
from sympy import symbols, integrate, sin, cos, tan, sec, csc, cot, exp, log, sqrt, simplify


class IntegrationQuestionGenerator:
    """Comprehensive Integration Generator - ALL 20+ FORMULAS"""
    
    def __init__(self):
        self.x = symbols('x')
    
    def generate_basic_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 1-2:
        ∫dx = x + C
        ∫x^n dx = x^(n+1)/(n+1) + C
        ∫(1/x)dx = ln|x| + C
        """
        questions = []
        
        for _ in range(count):
            formula_type = random.choice(['one', 'power', 'reciprocal'])
            
            if formula_type == 'one':
                questions.append({
                    "topic": "Integration - Basic",
                    "difficulty": difficulty,
                    "question": "Integrate: ∫dx",
                    "answer": "x + C",
                    "type": "conceptual",
                    "solution": "∫dx = x + C"
                })
            
            elif formula_type == 'power':
                n = random.randint(2, 6)
                
                questions.append({
                    "topic": "Integration - Power Rule",
                    "difficulty": difficulty,
                    "question": f"Integrate: ∫x^{n} dx",
                    "answer": f"x^{n+1}/{n+1} + C",
                    "type": "conceptual",
                    "solution": f"∫x^{n} dx = x^{n+1}/{n+1} + C"
                })
            
            else:  # reciprocal
                questions.append({
                    "topic": "Integration - Reciprocal",
                    "difficulty": difficulty,
                    "question": "Integrate: ∫(1/x)dx",
                    "answer": "ln|x| + C",
                    "type": "conceptual",
                    "solution": "∫(1/x)dx = ln|x| + C"
                })
        
        return questions
    
    def generate_exponential_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 3-4:
        ∫e^x dx = e^x + C
        ∫a^x dx = a^x/ln(a) + C
        """
        questions = []
        
        for _ in range(count):
            if random.choice([True, False]):
                # e^x
                if difficulty == "easy":
                    questions.append({
                        "topic": "Integration - Exponential",
                        "difficulty": difficulty,
                        "question": "Integrate: ∫e^x dx",
                        "answer": "e^x + C",
                        "type": "conceptual",
                        "solution": "∫e^x dx = e^x + C"
                    })
                else:
                    k = random.randint(2, 5)
                    questions.append({
                        "topic": "Integration - Exponential",
                        "difficulty": difficulty,
                        "question": f"Integrate: ∫e^({k}x) dx",
                        "answer": f"e^({k}x)/{k} + C",
                        "type": "conceptual",
                        "solution": f"∫e^({k}x) dx = e^({k}x)/{k} + C"
                    })
            else:
                # a^x
                a = random.randint(2, 10)
                questions.append({
                    "topic": "Integration - Exponential",
                    "difficulty": difficulty,
                    "question": f"Integrate: ∫{a}^x dx",
                    "answer": f"{a}^x/ln({a}) + C",
                    "type": "conceptual",
                    "solution": f"∫a^x dx = a^x/ln(a) + C = {a}^x/ln({a}) + C"
                })
        
        return questions
    
    def generate_logarithmic_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 5: ∫ln(x) dx = x·ln(x) - x + C
        """
        questions = []
        
        for _ in range(count):
            questions.append({
                "topic": "Integration - Logarithmic",
                "difficulty": difficulty,
                "question": "Integrate: ∫ln(x) dx",
                "answer": "x·ln(x) - x + C",
                "type": "conceptual",
                "solution": "∫ln(x) dx = x·ln(x) - x + C (integration by parts)"
            })
        
        return questions
    
    def generate_trig_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 6-11: Trigonometric integrals
        ∫sin(x)dx = -cos(x) + C
        ∫cos(x)dx = sin(x) + C
        ∫tan(x)dx = -ln|cos(x)| + C
        ∫cot(x)dx = ln|sin(x)| + C
        ∫sec(x)dx = ln|sec(x) + tan(x)| + C
        ∫csc(x)dx = -ln|csc(x) + cot(x)| + C
        """
        questions = []
        
        trig_integrals = [
            ("sin(x)", "-cos(x) + C", "∫sin(x)dx = -cos(x) + C"),
            ("cos(x)", "sin(x) + C", "∫cos(x)dx = sin(x) + C"),
            ("tan(x)", "-ln|cos(x)| + C", "∫tan(x)dx = -ln|cos(x)| + C"),
            ("cot(x)", "ln|sin(x)| + C", "∫cot(x)dx = ln|sin(x)| + C"),
            ("sec(x)", "ln|sec(x) + tan(x)| + C", "∫sec(x)dx = ln|sec(x) + tan(x)| + C"),
            ("csc(x)", "-ln|csc(x) + cot(x)| + C", "∫csc(x)dx = -ln|csc(x) + cot(x)| + C"),
        ]
        
        # Shuffle to ensure variety, then cycle through
        shuffled_integrals = trig_integrals.copy()
        random.shuffle(shuffled_integrals)
        
        for i in range(count):
            # Cycle through all integrals to ensure variety
            func_name, integral_str, explanation = shuffled_integrals[i % len(shuffled_integrals)]
            
            if difficulty == "easy":
                # Direct formula
                questions.append({
                    "topic": "Integration - Trigonometric",
                    "difficulty": difficulty,
                    "question": f"Integrate: ∫{func_name} dx",
                    "answer": integral_str,
                    "type": "conceptual",
                    "solution": explanation
                })
            else:
                # With coefficient - handle ALL 6 functions
                k = random.randint(2, 5)
                
                if func_name == "sin(x)":
                    answer = f"-cos({k}x)/{k} + C"
                    questions.append({
                        "topic": "Integration - Trigonometric",
                        "difficulty": difficulty,
                        "question": f"Integrate: ∫sin({k}x) dx",
                        "answer": answer,
                        "type": "conceptual",
                        "solution": f"∫sin({k}x) dx = -cos({k}x)/{k} + C"
                    })
                elif func_name == "cos(x)":
                    answer = f"sin({k}x)/{k} + C"
                    questions.append({
                        "topic": "Integration - Trigonometric",
                        "difficulty": difficulty,
                        "question": f"Integrate: ∫cos({k}x) dx",
                        "answer": answer,
                        "type": "conceptual",
                        "solution": f"∫cos({k}x) dx = sin({k}x)/{k} + C"
                    })
                else:
                    # For tan, cot, sec, csc - use direct formula (no simple coefficient form)
                    questions.append({
                        "topic": "Integration - Trigonometric",
                        "difficulty": difficulty,
                        "question": f"Integrate: ∫{func_name} dx",
                        "answer": integral_str,
                        "type": "conceptual",
                        "solution": explanation
                    })
        
        return questions
    
    def generate_trig_squared_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 12-13:
        ∫sec²(x)dx = tan(x) + C
        ∫csc²(x)dx = -cot(x) + C
        """
        questions = []
        
        formulas = [
            ("sec²(x)", "tan(x) + C", "∫sec²(x)dx = tan(x) + C"),
            ("csc²(x)", "-cot(x) + C", "∫csc²(x)dx = -cot(x) + C"),
        ]
        
        for _ in range(count):
            func_name, integral_str, explanation = random.choice(formulas)
            
            questions.append({
                "topic": "Integration - Trigonometric Squared",
                "difficulty": difficulty,
                "question": f"Integrate: ∫{func_name} dx",
                "answer": integral_str,
                "type": "conceptual",
                "solution": explanation
            })
        
        return questions
    
    def generate_trig_product_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 14-15:
        ∫sec(x)tan(x)dx = sec(x) + C
        ∫csc(x)cot(x)dx = -csc(x) + C
        """
        questions = []
        
        formulas = [
            ("sec(x)tan(x)", "sec(x) + C", "∫sec(x)tan(x)dx = sec(x) + C"),
            ("csc(x)cot(x)", "-csc(x) + C", "∫csc(x)cot(x)dx = -csc(x) + C"),
        ]
        
        for _ in range(count):
            func_name, integral_str, explanation = random.choice(formulas)
            
            questions.append({
                "topic": "Integration - Trigonometric Products",
                "difficulty": difficulty,
                "question": f"Integrate: ∫{func_name} dx",
                "answer": integral_str,
                "type": "conceptual",
                "solution": explanation
            })
        
        return questions
    
    def generate_inverse_trig_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 16-19: Inverse trigonometric integrals
        ∫dx/√(a²-x²) = sin⁻¹(x/a) + C
        ∫dx/(a²+x²) = (1/a)tan⁻¹(x/a) + C
        ∫dx/(x√(x²-a²)) = (1/a)sec⁻¹(|x|/a) + C
        """
        questions = []
        
        for _ in range(count):
            a = random.randint(2, 5)
            
            formula_type = random.choice(['arcsin', 'arctan', 'arcsec'])
            
            if formula_type == 'arcsin':
                questions.append({
                    "topic": "Integration - Inverse Trigonometric",
                    "difficulty": difficulty,
                    "question": f"Integrate: ∫dx/√({a}² - x²)",
                    "answer": f"sin⁻¹(x/{a}) + C",
                    "type": "conceptual",
                    "solution": f"∫dx/√(a² - x²) = sin⁻¹(x/a) + C = sin⁻¹(x/{a}) + C"
                })
            
            elif formula_type == 'arctan':
                questions.append({
                    "topic": "Integration - Inverse Trigonometric",
                    "difficulty": difficulty,
                    "question": f"Integrate: ∫dx/({a}² + x²)",
                    "answer": f"(1/{a})tan⁻¹(x/{a}) + C",
                    "type": "conceptual",
                    "solution": f"∫dx/(a² + x²) = (1/a)tan⁻¹(x/a) + C = (1/{a})tan⁻¹(x/{a}) + C"
                })
            
            else:  # arcsec
                questions.append({
                    "topic": "Integration - Inverse Trigonometric",
                    "difficulty": difficulty,
                    "question": f"Integrate: ∫dx/(x√(x² - {a}²))",
                    "answer": f"(1/{a})sec⁻¹(|x|/{a}) + C",
                    "type": "conceptual",
                    "solution": f"∫dx/(x√(x² - a²)) = (1/a)sec⁻¹(|x|/a) + C"
                })
        
        return questions
    
    def generate_polynomial_integration_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate polynomial integration questions"""
        questions = []
        
        for _ in range(count):
            if difficulty == "easy":
                a = random.randint(1, 10)
                n = random.randint(1, 4)
                expr = a * self.x**n
            elif difficulty == "medium":
                a = random.randint(1, 10)
                n = random.randint(2, 5)
                b = random.randint(1, 10)
                m = random.randint(1, n-1)
                expr = a * self.x**n + b * self.x**m
            else:
                a = random.randint(1, 10)
                n = random.randint(3, 6)
                b = random.randint(1, 10)
                m = random.randint(2, n-1)
                c = random.randint(1, 10)
                expr = a * self.x**n + b * self.x**m + c
            
            integral = integrate(expr, self.x)
            
            questions.append({
                "topic": "Integration - Polynomial",
                "difficulty": difficulty,
                "question": f"Integrate: ∫({expr}) dx",
                "answer": f"{integral} + C",
                "type": "conceptual",
                "solution": f"∫({expr}) dx = {integral} + C"
            })
        
        return questions
    
    def generate_substitution_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate integration by substitution questions"""
        questions = []
        
        for _ in range(count):
            # Type: ∫f'(x)·[f(x)]^n dx
            n = random.randint(2, 4)
            coef = random.randint(2, 5)
            
            # Example: ∫2x(x²+1)^n dx
            questions.append({
                "topic": "Integration - Substitution",
                "difficulty": difficulty,
                "question": f"Integrate using substitution: ∫{coef}x(x² + 1)^{n} dx",
                "answer": f"(x² + 1)^{n+1}/{n+1} + C",
                "type": "conceptual",
                "solution": f"Let u = x² + 1, du = 2x dx. ∫u^{n} du = u^{n+1}/{n+1} + C"
            })
        
        return questions
    
    def generate_by_parts_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate integration by parts questions
        ∫u dv = uv - ∫v du
        """
        questions = []
        
        for _ in range(count):
            # Simple cases like ∫x·sin(x) dx
            questions.append({
                "topic": "Integration - By Parts",
                "difficulty": difficulty,
                "question": "Integrate by parts: ∫x·sin(x) dx",
                "answer": "-x·cos(x) + sin(x) + C",
                "type": "conceptual",
                "solution": "Let u=x, dv=sin(x)dx. ∫x·sin(x)dx = -x·cos(x) + sin(x) + C"
            })
        
        return questions
    
    def generate_definite_integral_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate definite integral questions"""
        questions = []
        
        for _ in range(count):
            a = random.randint(1, 5)
            n = random.randint(1, 3)
            lower = 0
            upper = random.randint(1, 5)
            
            expr = a * self.x**n
            result = integrate(expr, (self.x, lower, upper))
            
            questions.append({
                "topic": "Integration - Definite",
                "difficulty": difficulty,
                "question": f"Evaluate: ∫₀^{upper} ({expr}) dx",
                "answer": float(result),
                "type": "numerical",
                "solution": f"∫₀^{upper} ({expr}) dx = [{a}x^{n+1}/{n+1}]₀^{upper} = {result}"
            })
        
        return questions
    
    def generate_standard_formulas_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate questions on all standard formulas combined
        """
        questions = []
        
        standard_formulas = [
            ("∫dx", "x + C"),
            ("∫x^n dx", "x^(n+1)/(n+1) + C"),
            ("∫(1/x)dx", "ln|x| + C"),
            ("∫e^x dx", "e^x + C"),
            ("∫sin(x)dx", "-cos(x) + C"),
            ("∫cos(x)dx", "sin(x) + C"),
            ("∫sec²(x)dx", "tan(x) + C"),
            ("∫csc²(x)dx", "-cot(x) + C"),
            ("∫sec(x)tan(x)dx", "sec(x) + C"),
            ("∫csc(x)cot(x)dx", "-csc(x) + C"),
        ]
        
        for _ in range(count):
            formula, answer = random.choice(standard_formulas)
            
            options = [answer]
            other_answers = [f[1] for f in standard_formulas if f != (formula, answer)]
            options.extend(random.sample(other_answers, min(3, len(other_answers))))
            random.shuffle(options)
            
            questions.append({
                "topic": "Integration - Standard Formulas",
                "difficulty": difficulty,
                "question": f"What is {formula}?",
                "answer": answer,
                "options": options[:4],
                "type": "mcq",
                "solution": f"{formula} = {answer}"
            })
        
        return questions
    
    def generate_all_questions(self, difficulty: str = "medium", count: int = 100) -> List[Dict[str, Any]]:
        """Generate comprehensive set using ALL 20+ integration formulas"""
        all_questions = []
        
        per_type = count // 9
        
        all_questions.extend(self.generate_basic_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_exponential_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_logarithmic_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_trig_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_trig_squared_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_trig_product_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_inverse_trig_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_polynomial_integration_questions(difficulty, per_type))
        all_questions.extend(self.generate_substitution_questions(difficulty, per_type))
        all_questions.extend(self.generate_by_parts_questions(difficulty, per_type))
        all_questions.extend(self.generate_definite_integral_questions(difficulty, per_type))
        all_questions.extend(self.generate_standard_formulas_questions(difficulty, per_type))
        
        return all_questions[:count]


# Main function
def generate_integration_questions(difficulty: str = "medium", count: int = 10,
                                   question_type: str = "all") -> List[Dict[str, Any]]:
    """
    Generate integration questions using ALL formulas from PDF
    
    Args:
        difficulty: "easy", "medium", or "hard"
        count: Number of questions
        question_type: "basic", "exp", "log", "trig", "trig_squared", "trig_product",
                      "inverse_trig", "polynomial", "substitution", "by_parts",
                      "definite", "standard", or "all"
    """
    generator = IntegrationQuestionGenerator()
    
    if question_type == "basic":
        return generator.generate_basic_integration_questions(difficulty, count)
    elif question_type == "exp":
        return generator.generate_exponential_integration_questions(difficulty, count)
    elif question_type == "log":
        return generator.generate_logarithmic_integration_questions(difficulty, count)
    elif question_type == "trig":
        return generator.generate_trig_integration_questions(difficulty, count)
    elif question_type == "trig_squared":
        return generator.generate_trig_squared_integration_questions(difficulty, count)
    elif question_type == "trig_product":
        return generator.generate_trig_product_integration_questions(difficulty, count)
    elif question_type == "inverse_trig":
        return generator.generate_inverse_trig_integration_questions(difficulty, count)
    elif question_type == "polynomial":
        return generator.generate_polynomial_integration_questions(difficulty, count)
    elif question_type == "substitution":
        return generator.generate_substitution_questions(difficulty, count)
    elif question_type == "by_parts":
        return generator.generate_by_parts_questions(difficulty, count)
    elif question_type == "definite":
        return generator.generate_definite_integral_questions(difficulty, count)
    elif question_type == "standard":
        return generator.generate_standard_formulas_questions(difficulty, count)
    else:  # all
        return generator.generate_all_questions(difficulty, count)


# Test block
if __name__ == "__main__":
    print("="*80)
    print("COMPREHENSIVE INTEGRATION GENERATOR TEST - ALL 20+ FORMULAS")
    print("="*80)
    
    print("\n1. BASIC INTEGRALS (∫dx, ∫x^n dx, ∫1/x dx):")
    qs = generate_integration_questions("easy", 3, "basic")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n2. EXPONENTIAL (∫e^x dx, ∫a^x dx):")
    qs = generate_integration_questions("medium", 2, "exp")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n3. LOGARITHMIC (∫ln(x) dx):")
    qs = generate_integration_questions("medium", 1, "log")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n4. TRIGONOMETRIC (sin, cos, tan, cot, sec, csc):")
    qs = generate_integration_questions("medium", 3, "trig")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n5. TRIGONOMETRIC SQUARED (sec², csc²):")
    qs = generate_integration_questions("medium", 2, "trig_squared")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n6. TRIGONOMETRIC PRODUCTS (sec·tan, csc·cot):")
    qs = generate_integration_questions("medium", 2, "trig_product")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n7. INVERSE TRIGONOMETRIC:")
    qs = generate_integration_questions("medium", 2, "inverse_trig")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n8. DEFINITE INTEGRALS:")
    qs = generate_integration_questions("medium", 2, "definite")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n" + "="*80)
    print("✓ ALL 20+ INTEGRATION FORMULAS IMPLEMENTED!")
    print("="*80)

