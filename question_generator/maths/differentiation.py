"""
Topic: Differentiation (COMPREHENSIVE - ALL FORMULAS)
Syllabus: DDCET Mathematics
Source: formula.pdf - ALL derivative formulas included
Features: 20+ derivative formulas, all rules (product, quotient, chain)
         Randomized MCQs, numerical questions, difficulty levels.
"""

import random
import math
from typing import List, Dict, Any
import sympy as sp
from sympy import symbols, diff, sin, cos, tan, sec, csc, cot, exp, log, sqrt, asin, acos, atan, simplify


class DifferentiationQuestionGenerator:
    """Comprehensive Differentiation Generator - ALL 20+ FORMULAS"""
    
    def __init__(self):
        self.x = symbols('x')
    
    def generate_constant_rule_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 1: d/dx(k) = 0
        """
        questions = []
        
        for _ in range(count):
            k = random.randint(1, 100)
            
            questions.append({
                "topic": "Differentiation - Constant Rule",
                "difficulty": difficulty,
                "question": f"Find d/dx({k})",
                "answer": "0",
                "type": "numerical",
                "solution": f"Derivative of constant is 0: d/dx({k}) = 0"
            })
        
        return questions
    
    def generate_sum_difference_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 2: d/dx[f(x) ± g(x)] = f'(x) ± g'(x)
        """
        questions = []
        
        for _ in range(count):
            a = random.randint(2, 5)
            n = random.randint(2, 4)
            b = random.randint(2, 8)
            m = random.randint(1, n-1)
            
            f = a * self.x**n
            g = b * self.x**m
            
            expr = f + g
            derivative = diff(expr, self.x)
            
            questions.append({
                "topic": "Differentiation - Sum/Difference Rule",
                "difficulty": difficulty,
                "question": f"Differentiate: y = {expr}",
                "answer": str(derivative),
                "type": "conceptual",
                "solution": f"d/dx[f ± g] = f' ± g', so d/dx = {derivative}"
            })
        
        return questions
    
    def generate_constant_multiple_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 3: d/dx[k·f(x)] = k·f'(x)
        """
        questions = []
        
        for _ in range(count):
            k = random.randint(2, 10)
            n = random.randint(2, 5)
            
            expr = k * self.x**n
            derivative = diff(expr, self.x)
            
            questions.append({
                "topic": "Differentiation - Constant Multiple",
                "difficulty": difficulty,
                "question": f"Differentiate: y = {k}x^{n}",
                "answer": str(derivative),
                "type": "conceptual",
                "solution": f"d/dx[k·f] = k·f', so d/dx({k}x^{n}) = {k}×{n}x^{n-1} = {derivative}"
            })
        
        return questions
    
    def generate_product_rule_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 4: d/dx[f(x)g(x)] = f(x)g'(x) + g(x)f'(x)
        """
        questions = []
        
        for _ in range(count):
            # Generate two functions
            f = random.choice([self.x, self.x**2, 2*self.x, 3*self.x])
            g = random.choice([self.x + 1, self.x**2, self.x**2 + 1])
            
            expr = f * g
            derivative = diff(expr, self.x)
            
            questions.append({
                "topic": "Differentiation - Product Rule",
                "difficulty": difficulty,
                "question": f"Differentiate using product rule: y = ({f})({g})",
                "answer": str(sp.expand(derivative)),
                "type": "conceptual",
                "solution": f"d/dx[fg] = f·g' + g·f' = {sp.expand(derivative)}"
            })
        
        return questions
    
    def generate_quotient_rule_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 5: d/dx[f(x)/g(x)] = [g(x)f'(x) - f(x)g'(x)] / [g(x)]²
        """
        questions = []
        
        for _ in range(count):
            # Numerator and denominator
            f = random.choice([self.x, self.x**2, self.x + 1])
            g = random.choice([self.x + 1, self.x, 2*self.x + 1])
            
            expr = f / g
            derivative = diff(expr, self.x)
            
            questions.append({
                "topic": "Differentiation - Quotient Rule",
                "difficulty": difficulty,
                "question": f"Differentiate using quotient rule: y = ({f})/({g})",
                "answer": str(sp.simplify(derivative)),
                "type": "conceptual",
                "solution": f"d/dx[f/g] = (g·f' - f·g')/g² = {sp.simplify(derivative)}"
            })
        
        return questions
    
    def generate_chain_rule_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 6: d/dx[f(g(x))] = f'(g(x))·g'(x)
        """
        questions = []
        
        for _ in range(count):
            inner = random.choice([self.x**2, 2*self.x + 1, self.x**2 + 1, 3*self.x - 2])
            power = random.randint(2, 4)
            
            expr = inner**power
            derivative = diff(expr, self.x)
            
            questions.append({
                "topic": "Differentiation - Chain Rule",
                "difficulty": difficulty,
                "question": f"Differentiate: y = ({inner})^{power}",
                "answer": str(sp.simplify(derivative)),
                "type": "conceptual",
                "solution": f"Using chain rule: d/dx[f(g)] = f'(g)·g' = {sp.simplify(derivative)}"
            })
        
        return questions
    
    def generate_power_rule_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 7: d/dx(x^n) = n·x^(n-1)
        """
        questions = []
        
        for _ in range(count):
            n = random.randint(2, 8)
            
            questions.append({
                "topic": "Differentiation - Power Rule",
                "difficulty": difficulty,
                "question": f"Differentiate: y = x^{n}",
                "answer": f"{n}x^{n-1}",
                "type": "conceptual",
                "solution": f"d/dx(x^n) = nx^(n-1) = {n}x^{n-1}"
            })
        
        return questions
    
    def generate_trig_derivative_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 8-13: Trigonometric derivatives
        d/dx(sin x) = cos x
        d/dx(cos x) = -sin x
        d/dx(tan x) = sec²x
        d/dx(cot x) = -csc²x
        d/dx(sec x) = sec x tan x
        d/dx(csc x) = -csc x cot x
        """
        questions = []
        
        trig_derivatives = [
            ("sin(x)", "cos(x)", "d/dx(sin x) = cos x"),
            ("cos(x)", "-sin(x)", "d/dx(cos x) = -sin x"),
            ("tan(x)", "sec²(x)", "d/dx(tan x) = sec²x"),
            ("cot(x)", "-csc²(x)", "d/dx(cot x) = -csc²x"),
            ("sec(x)", "sec(x)tan(x)", "d/dx(sec x) = sec x tan x"),
            ("csc(x)", "-csc(x)cot(x)", "d/dx(csc x) = -csc x cot x"),
        ]
        
        # Shuffle to ensure variety, then cycle through
        shuffled_derivatives = trig_derivatives.copy()
        random.shuffle(shuffled_derivatives)
        
        for i in range(count):
            # Cycle through all derivatives to ensure variety
            func_name, derivative_str, explanation = shuffled_derivatives[i % len(shuffled_derivatives)]
            
            if difficulty == "easy":
                # Direct formula
                questions.append({
                    "topic": "Differentiation - Trigonometric Functions",
                    "difficulty": difficulty,
                    "question": f"Find d/dx[{func_name}]",
                    "answer": derivative_str,
                    "type": "conceptual",
                    "solution": explanation
                })
            else:
                # With coefficient - ensure ALL 6 functions are handled
                coef = random.randint(2, 5)
                
                if func_name == "sin(x)":
                    expr = coef * sin(self.x)
                elif func_name == "cos(x)":
                    expr = coef * cos(self.x)
                elif func_name == "tan(x)":
                    expr = coef * tan(self.x)
                elif func_name == "cot(x)":
                    expr = coef * cot(self.x)
                elif func_name == "sec(x)":
                    expr = coef * sec(self.x)
                else:  # csc(x)
                    expr = coef * csc(self.x)
                
                derivative = diff(expr, self.x)
                
                questions.append({
                    "topic": "Differentiation - Trigonometric Functions",
                    "difficulty": difficulty,
                    "question": f"Differentiate: y = {expr}",
                    "answer": str(derivative),
                    "type": "conceptual",
                    "solution": f"d/dx = {derivative}"
                })
        
        return questions
    
    def generate_exponential_derivative_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 14-15: Exponential derivatives
        d/dx(e^x) = e^x
        d/dx(a^x) = a^x ln(a)
        """
        questions = []
        
        for _ in range(count):
            if random.choice([True, False]):
                # e^x derivative
                if difficulty == "easy":
                    questions.append({
                        "topic": "Differentiation - Exponential Functions",
                        "difficulty": difficulty,
                        "question": "Find d/dx[e^x]",
                        "answer": "e^x",
                        "type": "conceptual",
                        "solution": "d/dx(e^x) = e^x"
                    })
                else:
                    k = random.randint(2, 5)
                    expr = exp(k * self.x)
                    derivative = diff(expr, self.x)
                    
                    questions.append({
                        "topic": "Differentiation - Exponential Functions",
                        "difficulty": difficulty,
                        "question": f"Differentiate: y = e^({k}x)",
                        "answer": str(derivative),
                        "type": "conceptual",
                        "solution": f"Using chain rule: d/dx(e^({k}x)) = {k}e^({k}x)"
                    })
            else:
                # a^x derivative
                a = random.randint(2, 10)
                
                questions.append({
                    "topic": "Differentiation - Exponential Functions",
                    "difficulty": difficulty,
                    "question": f"Find d/dx[{a}^x]",
                    "answer": f"{a}^x × ln({a})",
                    "type": "conceptual",
                    "solution": f"d/dx(a^x) = a^x ln(a) = {a}^x × ln({a})"
                })
        
        return questions
    
    def generate_logarithmic_derivative_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formula 16: d/dx[ln|x|] = 1/x
        """
        questions = []
        
        for _ in range(count):
            if difficulty == "easy":
                questions.append({
                    "topic": "Differentiation - Logarithmic Functions",
                    "difficulty": difficulty,
                    "question": "Find d/dx[ln(x)]",
                    "answer": "1/x",
                    "type": "conceptual",
                    "solution": "d/dx(ln x) = 1/x"
                })
            else:
                # ln(ax + b)
                a = random.randint(2, 5)
                b = random.randint(1, 10)
                
                expr = log(a * self.x + b)
                derivative = diff(expr, self.x)
                
                questions.append({
                    "topic": "Differentiation - Logarithmic Functions",
                    "difficulty": difficulty,
                    "question": f"Differentiate: y = ln({a}x + {b})",
                    "answer": str(derivative),
                    "type": "conceptual",
                    "solution": f"Using chain rule: d/dx = {derivative}"
                })
        
        return questions
    
    def generate_inverse_trig_derivative_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """
        Formulas 17-22: Inverse trigonometric derivatives
        d/dx(sin⁻¹x) = 1/√(1-x²)
        d/dx(cos⁻¹x) = -1/√(1-x²)
        d/dx(tan⁻¹x) = 1/(1+x²)
        d/dx(cot⁻¹x) = -1/(1+x²)
        d/dx(sec⁻¹x) = 1/(|x|√(x²-1))
        d/dx(csc⁻¹x) = -1/(|x|√(x²-1))
        """
        questions = []
        
        inverse_trig = [
            ("sin⁻¹(x)", "1/√(1-x²)"),
            ("cos⁻¹(x)", "-1/√(1-x²)"),
            ("tan⁻¹(x)", "1/(1+x²)"),
            ("cot⁻¹(x)", "-1/(1+x²)"),
            ("sec⁻¹(x)", "1/(|x|√(x²-1))"),
            ("csc⁻¹(x)", "-1/(|x|√(x²-1))"),
        ]
        
        for _ in range(count):
            func_name, derivative_str = random.choice(inverse_trig)
            
            options = [derivative_str]
            other_derivatives = [d[1] for d in inverse_trig if d != (func_name, derivative_str)]
            options.extend(random.sample(other_derivatives, min(3, len(other_derivatives))))
            random.shuffle(options)
            
            questions.append({
                "topic": "Differentiation - Inverse Trigonometric",
                "difficulty": difficulty,
                "question": f"Find d/dx[{func_name}]",
                "answer": derivative_str,
                "options": options[:4],
                "type": "mcq",
                "solution": f"d/dx({func_name}) = {derivative_str}"
            })
        
        return questions
    
    def generate_polynomial_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate polynomial differentiation questions"""
        questions = []
        
        for _ in range(count):
            if difficulty == "easy":
                a = random.randint(1, 10)
                n = random.randint(2, 4)
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
                d = random.randint(1, 20)
                expr = a * self.x**n + b * self.x**m + c * self.x + d
            
            derivative = diff(expr, self.x)
            
            questions.append({
                "topic": "Differentiation - Polynomial",
                "difficulty": difficulty,
                "question": f"Find dy/dx if y = {expr}",
                "answer": str(derivative),
                "type": "conceptual",
                "solution": f"dy/dx = {derivative}"
            })
        
        return questions
    
    def generate_parametric_derivative_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate parametric differentiation questions"""
        questions = []
        
        t = symbols('t')
        
        for _ in range(count):
            # x = f(t), y = g(t)
            # dy/dx = (dy/dt) / (dx/dt)
            
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            
            x_t = a * t**2
            y_t = b * t**3
            
            dx_dt = diff(x_t, t)
            dy_dt = diff(y_t, t)
            
            questions.append({
                "topic": "Differentiation - Parametric",
                "difficulty": difficulty,
                "question": f"If x = {x_t} and y = {y_t}, find dy/dx",
                "answer": f"({dy_dt})/({dx_dt})",
                "type": "conceptual",
                "solution": f"dy/dx = (dy/dt)/(dx/dt) = ({dy_dt})/({dx_dt}) = {sp.simplify(dy_dt/dx_dt)}"
            })
        
        return questions
    
    def generate_implicit_derivative_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate implicit differentiation questions"""
        questions = []
        
        for _ in range(count):
            # x² + y² = r²
            r = random.randint(1, 10)
            
            questions.append({
                "topic": "Differentiation - Implicit",
                "difficulty": difficulty,
                "question": f"Find dy/dx if x² + y² = {r**2}",
                "answer": "-x/y",
                "type": "conceptual",
                "solution": f"Differentiating: 2x + 2y(dy/dx) = 0, dy/dx = -x/y"
            })
        
        return questions
    
    def generate_logarithmic_differentiation_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate logarithmic differentiation questions"""
        questions = []
        
        for _ in range(count):
            # y = x^x type
            questions.append({
                "topic": "Differentiation - Logarithmic",
                "difficulty": difficulty,
                "question": "Differentiate y = x^x using logarithmic differentiation",
                "answer": "x^x(1 + ln(x))",
                "type": "conceptual",
                "solution": "Taking log: ln(y) = x·ln(x), (1/y)dy/dx = ln(x) + 1, dy/dx = x^x(1 + ln(x))"
            })
        
        return questions
    
    def generate_successive_differentiation_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate second derivative questions"""
        questions = []
        
        for _ in range(count):
            a = random.randint(1, 5)
            b = random.randint(1, 8)
            
            expr = a * self.x**3 + b * self.x**2
            
            first_derivative = diff(expr, self.x)
            second_derivative = diff(first_derivative, self.x)
            
            questions.append({
                "topic": "Differentiation - Successive (Second Derivative)",
                "difficulty": difficulty,
                "question": f"Find d²y/dx² if y = {expr}",
                "answer": str(second_derivative),
                "type": "conceptual",
                "solution": f"dy/dx = {first_derivative}, d²y/dx² = {second_derivative}"
            })
        
        return questions
    
    def generate_application_questions(self, difficulty: str = "medium", count: int = 10) -> List[Dict[str, Any]]:
        """Generate application questions (velocity, acceleration)"""
        questions = []
        
        t = symbols('t')
        
        for _ in range(count):
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            
            s = a * t**2 + b * t + c
            v = diff(s, t)
            a_accel = diff(v, t)
            
            t_val = random.randint(1, 5)
            v_at_t = v.subs(t, t_val)
            
            if random.choice([True, False]):
                questions.append({
                    "topic": "Differentiation - Applications (Velocity)",
                    "difficulty": difficulty,
                    "question": f"If displacement s = {s} meters, find velocity at t = {t_val} seconds",
                    "answer": float(v_at_t),
                    "type": "numerical",
                    "solution": f"v = ds/dt = {v}, at t={t_val}: v = {v_at_t} m/s"
                })
            else:
                a_at_t = a_accel.subs(t, t_val)
                questions.append({
                    "topic": "Differentiation - Applications (Acceleration)",
                    "difficulty": difficulty,
                    "question": f"If displacement s = {s} meters, find acceleration at t = {t_val} seconds",
                    "answer": float(a_at_t),
                    "type": "numerical",
                    "solution": f"v = {v}, a = dv/dt = {a_accel}, at t={t_val}: a = {a_at_t} m/s²"
                })
        
        return questions
    
    def generate_all_questions(self, difficulty: str = "medium", count: int = 100) -> List[Dict[str, Any]]:
        """Generate comprehensive set using ALL 20+ derivative formulas"""
        all_questions = []
        
        per_type = count // 12
        
        all_questions.extend(self.generate_constant_rule_questions(difficulty, per_type))
        all_questions.extend(self.generate_sum_difference_questions(difficulty, per_type))
        all_questions.extend(self.generate_constant_multiple_questions(difficulty, per_type))
        all_questions.extend(self.generate_product_rule_questions(difficulty, per_type))
        all_questions.extend(self.generate_quotient_rule_questions(difficulty, per_type))
        all_questions.extend(self.generate_chain_rule_questions(difficulty, per_type))
        all_questions.extend(self.generate_power_rule_questions(difficulty, per_type))
        all_questions.extend(self.generate_trig_derivative_questions(difficulty, per_type))
        all_questions.extend(self.generate_exponential_derivative_questions(difficulty, per_type))
        all_questions.extend(self.generate_logarithmic_derivative_questions(difficulty, per_type))
        all_questions.extend(self.generate_inverse_trig_derivative_questions(difficulty, per_type))
        all_questions.extend(self.generate_parametric_derivative_questions(difficulty, per_type))
        all_questions.extend(self.generate_successive_differentiation_questions(difficulty, per_type))
        all_questions.extend(self.generate_application_questions(difficulty, per_type))
        
        return all_questions[:count]


# Main function
def generate_differentiation_questions(difficulty: str = "medium", count: int = 10,
                                       question_type: str = "all") -> List[Dict[str, Any]]:
    """
    Generate differentiation questions using ALL formulas from PDF
    
    Args:
        difficulty: "easy", "medium", or "hard"
        count: Number of questions
        question_type: "constant", "sum", "product", "quotient", "chain", "power",
                      "trig", "exp", "log", "inverse_trig", "parametric", 
                      "implicit", "logarithmic_diff", "successive", "application", or "all"
    """
    generator = DifferentiationQuestionGenerator()
    
    if question_type == "constant":
        return generator.generate_constant_rule_questions(difficulty, count)
    elif question_type == "sum":
        return generator.generate_sum_difference_questions(difficulty, count)
    elif question_type == "product":
        return generator.generate_product_rule_questions(difficulty, count)
    elif question_type == "quotient":
        return generator.generate_quotient_rule_questions(difficulty, count)
    elif question_type == "chain":
        return generator.generate_chain_rule_questions(difficulty, count)
    elif question_type == "power":
        return generator.generate_power_rule_questions(difficulty, count)
    elif question_type == "trig":
        return generator.generate_trig_derivative_questions(difficulty, count)
    elif question_type == "exp":
        return generator.generate_exponential_derivative_questions(difficulty, count)
    elif question_type == "log":
        return generator.generate_logarithmic_derivative_questions(difficulty, count)
    elif question_type == "inverse_trig":
        return generator.generate_inverse_trig_derivative_questions(difficulty, count)
    elif question_type == "parametric":
        return generator.generate_parametric_derivative_questions(difficulty, count)
    elif question_type == "implicit":
        return generator.generate_implicit_derivative_questions(difficulty, count)
    elif question_type == "logarithmic_diff":
        return generator.generate_logarithmic_differentiation_questions(difficulty, count)
    elif question_type == "successive":
        return generator.generate_successive_differentiation_questions(difficulty, count)
    elif question_type == "application":
        return generator.generate_application_questions(difficulty, count)
    else:  # all
        return generator.generate_all_questions(difficulty, count)


# Test block
if __name__ == "__main__":
    print("="*80)
    print("COMPREHENSIVE DIFFERENTIATION GENERATOR TEST - ALL 20+ FORMULAS")
    print("="*80)
    
    print("\n1. CONSTANT RULE (d/dx k = 0):")
    qs = generate_differentiation_questions("easy", 2, "constant")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n2. POWER RULE (d/dx x^n = nx^(n-1)):")
    qs = generate_differentiation_questions("medium", 2, "power")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n3. PRODUCT RULE:")
    qs = generate_differentiation_questions("medium", 2, "product")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n4. QUOTIENT RULE:")
    qs = generate_differentiation_questions("medium", 2, "quotient")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n5. CHAIN RULE:")
    qs = generate_differentiation_questions("medium", 2, "chain")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n6. TRIGONOMETRIC (sin, cos, tan, cot, sec, csc):")
    qs = generate_differentiation_questions("medium", 3, "trig")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n7. EXPONENTIAL (e^x, a^x):")
    qs = generate_differentiation_questions("medium", 2, "exp")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n8. LOGARITHMIC (ln x):")
    qs = generate_differentiation_questions("medium", 2, "log")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n9. INVERSE TRIGONOMETRIC (sin⁻¹, cos⁻¹, tan⁻¹, etc.):")
    qs = generate_differentiation_questions("medium", 2, "inverse_trig")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n10. APPLICATIONS (Velocity, Acceleration):")
    qs = generate_differentiation_questions("medium", 2, "application")
    for i, q in enumerate(qs, 1):
        print(f"{i}. {q['question']} → {q['answer']}")
    
    print("\n" + "="*80)
    print("✓ ALL 20+ DIFFERENTIATION FORMULAS IMPLEMENTED!")
    print("="*80)

