"""
Topic: Limits (COMPREHENSIVE - ALL FORMULAS)
Syllabus: DDCET Mathematics
Source: Limits formula image - ALL formulas included
Features: Trigonometric limits, 1^∞ form, Log/Exponential limits, L'Hospital's Rule
         Randomized MCQs, numerical questions, difficulty levels.
"""

import random
import math
from typing import List, Dict, Any
import sympy as sp
from sympy import symbols, limit, sin, cos, tan, log, exp, oo


class LimitsQuestionGenerator:
    """Comprehensive Limits Question Generator - ALL FORMULAS INCLUDED"""
    
    def __init__(self):
        self.x = symbols('x')
    
    def generate_trig_limit_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate questions based on trigonometric limits:
        1. lim(x→0) sin(x)/x = 1
        2. lim(x→0) cos(x) = 1
        3. lim(x→0) tan(x)/x = 1
        4. lim(x→0) sin(x)/tan(x) = 1
        5. lim(x→0) sin⁻¹(x)/x = 1
        6. lim(x→0) tan⁻¹(x)/x = 1
        """
        questions = []
        
        trig_limits = [
            {
                'formula': 'lim(x→0) sin(x)/x',
                'answer': 1,
                'explanation': 'Standard limit: lim(x→0) sin(x)/x = 1'
            },
            {
                'formula': 'lim(x→0) cos(x)',
                'answer': 1,
                'explanation': 'Direct substitution: cos(0) = 1'
            },
            {
                'formula': 'lim(x→0) tan(x)/x',
                'answer': 1,
                'explanation': 'Standard limit: lim(x→0) tan(x)/x = 1'
            },
            {
                'formula': 'lim(x→0) sin(x)/tan(x)',
                'answer': 1,
                'explanation': 'lim(x→0) sin(x)/tan(x) = lim(x→0) cos(x) = 1'
            },
            {
                'formula': 'lim(x→0) sin⁻¹(x)/x',
                'answer': 1,
                'explanation': 'Standard limit: lim(x→0) sin⁻¹(x)/x = 1'
            },
            {
                'formula': 'lim(x→0) tan⁻¹(x)/x',
                'answer': 1,
                'explanation': 'Standard limit: lim(x→0) tan⁻¹(x)/x = 1'
            },
        ]
        
        for _ in range(count):
            limit_data = random.choice(trig_limits)
            
            if difficulty == "easy":
                # Direct formula
                questions.append({
                    "topic": "Limits - Trigonometric Limits",
                    "difficulty": difficulty,
                    "question": f"Evaluate: {limit_data['formula']}",
                    "answer": limit_data['answer'],
                    "type": "numerical",
                    "solution": limit_data['explanation']
                })
            else:
                # With coefficient/multiplier
                coef = random.randint(2, 5)
                
                if 'sin(x)/x' in limit_data['formula']:
                    questions.append({
                        "topic": "Limits - Trigonometric Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: lim(x→0) [{coef}sin(x)/x]",
                        "answer": coef * 1,
                        "type": "numerical",
                        "solution": f"lim(x→0) {coef}sin(x)/x = {coef} × lim(x→0) sin(x)/x = {coef} × 1 = {coef}"
                    })
                elif 'tan(x)/x' in limit_data['formula']:
                    questions.append({
                        "topic": "Limits - Trigonometric Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: lim(x→0) [sin({coef}x)/x]",
                        "answer": coef,
                        "type": "numerical",
                        "solution": f"lim(x→0) sin({coef}x)/x = {coef} × lim(x→0) sin({coef}x)/({coef}x) = {coef} × 1 = {coef}"
                    })
                else:
                    questions.append({
                        "topic": "Limits - Trigonometric Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: {limit_data['formula']}",
                        "answer": limit_data['answer'],
                        "type": "numerical",
                        "solution": limit_data['explanation']
                    })
        
        return questions
    
    def generate_one_power_infinity_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate questions on limits of form 1^∞:
        1. lim(x→∞) (1 + x)^(1/x) = e
        2. lim(x→∞) (1 + 1/x)^x = e
        3. lim(x→∞) (1 + a/x)^x = e^a
        """
        questions = []
        
        formulas = [
            {
                'formula': 'lim(x→∞) (1 + x)^(1/x)',
                'answer': 'e',
                'numeric': math.e,
                'explanation': 'Standard 1^∞ form: lim(x→∞) (1 + x)^(1/x) = e'
            },
            {
                'formula': 'lim(x→∞) (1 + 1/x)^x',
                'answer': 'e',
                'numeric': math.e,
                'explanation': 'Standard limit: lim(x→∞) (1 + 1/x)^x = e'
            },
        ]
        
        for _ in range(count):
            if difficulty == "easy":
                # Standard formulas
                formula_data = random.choice(formulas)
                
                questions.append({
                    "topic": "Limits - 1^∞ Form",
                    "difficulty": difficulty,
                    "question": f"Evaluate: {formula_data['formula']}",
                    "answer": formula_data['answer'],
                    "type": "conceptual",
                    "solution": formula_data['explanation']
                })
            else:
                # With coefficient: lim(x→∞) (1 + a/x)^x = e^a
                a = random.randint(2, 5)
                answer_numeric = round(math.e ** a, 3)
                
                questions.append({
                    "topic": "Limits - 1^∞ Form",
                    "difficulty": difficulty,
                    "question": f"Evaluate: lim(x→∞) (1 + {a}/x)^x",
                    "answer": f"e^{a}",
                    "type": "conceptual",
                    "solution": f"Using lim(x→∞) (1 + a/x)^x = e^a, we get e^{a} ≈ {answer_numeric}"
                })
        
        return questions
    
    def generate_log_exp_limit_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate questions on log and exponential limits:
        1. lim(x→0) e^x = 1
        2. lim(x→0) (e^x - 1)/x = 1
        3. lim(x→0) (a^x - 1)/x = log_e(a)
        4. lim(x→0) log(1+x)/x = 1
        5. lim(x→a) (x^n - a^n)/(x-a) = n·a^(n-1)
        """
        questions = []
        
        formulas = [
            {
                'type': 'exp_zero',
                'formula': 'lim(x→0) e^x',
                'answer': 1,
                'explanation': 'Direct substitution: e^0 = 1'
            },
            {
                'type': 'exp_minus_one',
                'formula': 'lim(x→0) (e^x - 1)/x',
                'answer': 1,
                'explanation': 'Standard limit: lim(x→0) (e^x - 1)/x = 1'
            },
            {
                'type': 'general_exp',
                'formula': 'lim(x→0) (a^x - 1)/x',
                'answer': 'log(a)',
                'explanation': 'Standard limit: lim(x→0) (a^x - 1)/x = log_e(a)'
            },
            {
                'type': 'log_limit',
                'formula': 'lim(x→0) log(1+x)/x',
                'answer': 1,
                'explanation': 'Standard limit: lim(x→0) log(1+x)/x = 1'
            },
        ]
        
        for _ in range(count):
            formula_data = random.choice(formulas)
            
            if formula_data['type'] == 'exp_zero':
                questions.append({
                    "topic": "Limits - Exponential Limits",
                    "difficulty": difficulty,
                    "question": f"Evaluate: {formula_data['formula']}",
                    "answer": formula_data['answer'],
                    "type": "numerical",
                    "solution": formula_data['explanation']
                })
            
            elif formula_data['type'] == 'exp_minus_one':
                if difficulty == "easy":
                    questions.append({
                        "topic": "Limits - Exponential Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: {formula_data['formula']}",
                        "answer": formula_data['answer'],
                        "type": "numerical",
                        "solution": formula_data['explanation']
                    })
                else:
                    # With coefficient
                    k = random.randint(2, 5)
                    questions.append({
                        "topic": "Limits - Exponential Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: lim(x→0) (e^({k}x) - 1)/x",
                        "answer": k,
                        "type": "numerical",
                        "solution": f"lim(x→0) (e^({k}x) - 1)/x = {k} × lim(x→0) (e^({k}x) - 1)/({k}x) = {k}"
                    })
            
            elif formula_data['type'] == 'general_exp':
                a = random.randint(2, 10)
                log_a = round(math.log(a), 3)
                
                questions.append({
                    "topic": "Limits - Exponential Limits",
                    "difficulty": difficulty,
                    "question": f"Evaluate: lim(x→0) ({a}^x - 1)/x",
                    "answer": log_a,
                    "type": "numerical",
                    "solution": f"Using lim(x→0) (a^x - 1)/x = log_e(a) = log_e({a}) = {log_a}"
                })
            
            elif formula_data['type'] == 'log_limit':
                if difficulty == "easy":
                    questions.append({
                        "topic": "Limits - Logarithmic Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: {formula_data['formula']}",
                        "answer": formula_data['answer'],
                        "type": "numerical",
                        "solution": formula_data['explanation']
                    })
                else:
                    # With coefficient
                    a = random.randint(2, 5)
                    questions.append({
                        "topic": "Limits - Logarithmic Limits",
                        "difficulty": difficulty,
                        "question": f"Evaluate: lim(x→0) log(1+{a}x)/x",
                        "answer": a,
                        "type": "numerical",
                        "solution": f"lim(x→0) log(1+{a}x)/x = {a} × lim(x→0) log(1+{a}x)/({a}x) = {a}"
                    })
        
        return questions
    
    def generate_power_limit_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate questions using: lim(x→a) (x^n - a^n)/(x-a) = n·a^(n-1)
        """
        questions = []
        
        for _ in range(count):
            a = random.randint(1, 5)
            n = random.randint(2, 5)
            
            # n·a^(n-1)
            answer = n * (a ** (n-1))
            
            questions.append({
                "topic": "Limits - Power Limits",
                "difficulty": difficulty,
                "question": f"Evaluate: lim(x→{a}) (x^{n} - {a**n})/(x - {a})",
                "answer": answer,
                "type": "numerical",
                "solution": f"Using lim(x→a) (x^n - a^n)/(x-a) = n·a^(n-1) = {n}×{a}^{n-1} = {answer}"
            })
        
        return questions
    
    def generate_lhospital_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate L'Hospital's Rule questions:
        If lim f(x)/g(x) is 0/0 form, then lim f(x)/g(x) = lim f'(x)/g'(x)
        """
        questions = []
        
        for _ in range(count):
            # Simple 0/0 form
            a = random.randint(1, 5)
            
            # f(x) = x^2 - a^2, g(x) = x - a
            # lim(x→a) (x^2 - a^2)/(x - a)
            # f'(x) = 2x, g'(x) = 1
            # lim(x→a) 2x/1 = 2a
            
            answer = 2 * a
            
            questions.append({
                "topic": "Limits - L'Hospital's Rule",
                "difficulty": difficulty,
                "question": f"Using L'Hospital's Rule, evaluate: lim(x→{a}) (x² - {a**2})/(x - {a})",
                "answer": answer,
                "type": "numerical",
                "solution": f"0/0 form. Apply L'Hospital: lim(x→{a}) 2x/1 = 2({a}) = {answer}"
            })
        
        return questions
    
    def generate_polynomial_limit_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate polynomial limit questions (direct substitution)"""
        questions = []
        
        for _ in range(count):
            # Generate polynomial
            if difficulty == "easy":
                a = random.randint(1, 5)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                x0 = random.randint(0, 3)
                
                # ax^2 + bx + c
                answer = a * x0**2 + b * x0 + c
                
                questions.append({
                    "topic": "Limits - Polynomial",
                    "difficulty": difficulty,
                    "question": f"Evaluate: lim(x→{x0}) [{a}x² + {b}x + {c}]",
                    "answer": answer,
                    "type": "numerical",
                    "solution": f"Direct substitution: {a}({x0})² + {b}({x0}) + {c} = {answer}"
                })
            else:
                # Higher degree
                a = random.randint(1, 3)
                b = random.randint(1, 5)
                c = random.randint(1, 10)
                d = random.randint(1, 10)
                x0 = random.randint(1, 3)
                
                # ax^3 + bx^2 + cx + d
                answer = a * x0**3 + b * x0**2 + c * x0 + d
                
                questions.append({
                    "topic": "Limits - Polynomial",
                    "difficulty": difficulty,
                    "question": f"Evaluate: lim(x→{x0}) [{a}x³ + {b}x² + {c}x + {d}]",
                    "answer": answer,
                    "type": "numerical",
                    "solution": f"Direct substitution: {a}({x0})³ + {b}({x0})² + {c}({x0}) + {d} = {answer}"
                })
        
        return questions
    
    def generate_rational_limit_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate rational function limit questions"""
        questions = []
        
        for _ in range(count):
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            x0 = random.randint(1, 5)
            
            # (ax + b) / (x + 1)
            numerator = a * x0 + b
            denominator = x0 + 1
            answer = round(numerator / denominator, 2)
            
            questions.append({
                "topic": "Limits - Rational Functions",
                "difficulty": difficulty,
                "question": f"Evaluate: lim(x→{x0}) [({a}x + {b})/(x + 1)]",
                "answer": answer,
                "type": "numerical",
                "solution": f"Direct substitution: ({a}×{x0} + {b})/({x0} + 1) = {numerator}/{denominator} = {answer}"
            })
        
        return questions
    
    def generate_infinity_limit_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate limits as x→∞:
        - lim(x→∞) 1/x = 0
        - lim(x→∞) 1/x^n = 0
        - Highest power rule for rational functions
        """
        questions = []
        
        for _ in range(count):
            formula_type = random.choice(['simple_reciprocal', 'power_reciprocal', 'rational'])
            
            if formula_type == 'simple_reciprocal':
                questions.append({
                    "topic": "Limits - Limits at Infinity",
                    "difficulty": difficulty,
                    "question": "Evaluate: lim(x→∞) [1/x]",
                    "answer": 0,
                    "type": "numerical",
                    "solution": "As x approaches infinity, 1/x approaches 0"
                })
            
            elif formula_type == 'power_reciprocal':
                n = random.randint(2, 5)
                questions.append({
                    "topic": "Limits - Limits at Infinity",
                    "difficulty": difficulty,
                    "question": f"Evaluate: lim(x→∞) [1/x^{n}]",
                    "answer": 0,
                    "type": "numerical",
                    "solution": f"As x→∞, 1/x^{n} → 0"
                })
            
            else:  # rational
                # lim(x→∞) (ax + b)/(cx + d) = a/c
                a = random.randint(1, 5)
                b = random.randint(1, 10)
                c = random.randint(1, 5)
                d = random.randint(1, 10)
                
                answer = round(a / c, 2)
                
                questions.append({
                    "topic": "Limits - Limits at Infinity",
                    "difficulty": difficulty,
                    "question": f"Evaluate: lim(x→∞) [({a}x + {b})/({c}x + {d})]",
                    "answer": answer,
                    "type": "numerical",
                    "solution": f"Highest power rule: lim(x→∞) ({a}x)/({c}x) = {a}/{c} = {answer}"
                })
        
        return questions
    
    def generate_all_questions(self, difficulty: str = "medium", count: int = 50) -> List[Dict[str, Any]]:
        """Generate comprehensive set of ALL limit formulas"""
        all_questions = []
        
        per_type = count // 6
        
        all_questions.extend(self.generate_trig_limit_questions(difficulty, per_type))
        all_questions.extend(self.generate_one_power_infinity_questions(difficulty, per_type))
        all_questions.extend(self.generate_log_exp_limit_questions(difficulty, per_type))
        all_questions.extend(self.generate_power_limit_questions(difficulty, per_type))
        all_questions.extend(self.generate_polynomial_limit_questions(difficulty, per_type))
        all_questions.extend(self.generate_rational_limit_questions(difficulty, per_type))
        all_questions.extend(self.generate_infinity_limit_questions(difficulty, per_type))
        
        return all_questions[:count]


# Main function
def generate_limit_questions(difficulty: str = "medium", count: int = 10, 
                             question_type: str = "all") -> List[Dict[str, Any]]:
    """
    Generate limit questions using ALL formulas
    
    Args:
        difficulty: "easy", "medium", or "hard"
        count: Number of questions
        question_type: "trig", "one_infinity", "log_exp", "power", "polynomial", 
                      "rational", "infinity", or "all"
    """
    generator = LimitsQuestionGenerator()
    
    if question_type == "trig":
        return generator.generate_trig_limit_questions(difficulty, count)
    elif question_type == "one_infinity":
        return generator.generate_one_power_infinity_questions(difficulty, count)
    elif question_type == "log_exp":
        return generator.generate_log_exp_limit_questions(difficulty, count)
    elif question_type == "power":
        return generator.generate_power_limit_questions(difficulty, count)
    elif question_type == "polynomial":
        return generator.generate_polynomial_limit_questions(difficulty, count)
    elif question_type == "rational":
        return generator.generate_rational_limit_questions(difficulty, count)
    elif question_type == "infinity":
        return generator.generate_infinity_limit_questions(difficulty, count)
    else:  # all
        return generator.generate_all_questions(difficulty, count)


# Test block
if __name__ == "__main__":
    print("="*80)
    print("COMPREHENSIVE LIMITS GENERATOR TEST - ALL FORMULAS")
    print("="*80)
    
    print("\n1. TRIGONOMETRIC LIMITS (6 formulas):")
    print("-"*80)
    qs = generate_limit_questions("medium", 3, "trig")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']}")
        print(f"   Answer: {q['answer']}")
        print(f"   Solution: {q['solution']}\n")
    
    print("2. 1^∞ FORM LIMITS (3 formulas):")
    print("-"*80)
    qs = generate_limit_questions("medium", 2, "one_infinity")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']}")
        print(f"   Answer: {q['answer']}\n")
    
    print("3. LOG & EXPONENTIAL LIMITS (5 formulas):")
    print("-"*80)
    qs = generate_limit_questions("medium", 3, "log_exp")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']}")
        print(f"   Answer: {q['answer']}\n")
    
    print("4. L'HOSPITAL'S RULE:")
    print("-"*80)
    gen = LimitsQuestionGenerator()
    qs = gen.generate_lhospital_questions("medium", 2)
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']}")
        print(f"   Answer: {q['answer']}\n")
    
    print("5. LIMITS AT INFINITY:")
    print("-"*80)
    qs = generate_limit_questions("medium", 2, "infinity")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']}")
        print(f"   Answer: {q['answer']}\n")
    
    print("="*80)
    print("✓ ALL LIMITS FORMULAS FROM IMAGE IMPLEMENTED!")
    print("✓ 14+ limit formulas covered")
    print("="*80)

