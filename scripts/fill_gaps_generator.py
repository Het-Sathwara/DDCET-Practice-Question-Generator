#!/usr/bin/env python3
"""
Generate questions for MISSING/LOW coverage areas
Based on DDCET syllabus analysis
"""

import json
import random
import math
import os

def generate_circle_questions(count=1000):
    """Circle questions - MISSING from Coordinate Geometry"""
    questions = []
    
    for i in range(count):
        q_type = random.choice([
            'standard_form', 'general_to_standard', 'find_center_radius',
            'equation_from_center_radius', 'diameter_form', 'intercepts'
        ])
        
        h, k, r = random.randint(-10, 10), random.randint(-10, 10), random.randint(1, 12)
        
        if q_type == 'standard_form':
            question = f"Write the equation of a circle with center ({h}, {k}) and radius {r}"
            answer = f"(x-{h})² + (y-{k})² = {r**2}"
            solution = f"Step 1: Use standard form (x-h)² + (y-k)² = r²\nStep 2: Substitute h={h}, k={k}, r={r}\nStep 3: (x-{h})² + (y-{k})² = {r}² = {r**2}\nAnswer: (x-{h})² + (y-{k})² = {r**2}"
        
        elif q_type == 'general_to_standard':
            # General form: x² + y² + 2gx + 2fy + c = 0
            g, f = random.randint(-8, 8), random.randint(-8, 8)
            c = random.randint(-20, 20)
            h_calc, k_calc = -g, -f
            r_sq = g**2 + f**2 - c
            question = f"Find center and radius of circle: x² + y² + {2*g}x + {2*f}y + {c} = 0"
            if r_sq > 0:
                r_calc = math.sqrt(r_sq)
                answer = f"Center: ({h_calc}, {k_calc}), Radius: {r_calc:.2f}"
                solution = f"Step 1: Compare with x² + y² + 2gx + 2fy + c = 0\nStep 2: 2g = {2*g}, so g = {g}; 2f = {2*f}, so f = {f}\nStep 3: Center = (-g, -f) = ({h_calc}, {k_calc})\nStep 4: Radius = √(g² + f² - c) = √({g}² + {f}² - {c}) = √{r_sq} = {r_calc:.2f}\nAnswer: Center ({h_calc}, {k_calc}), Radius {r_calc:.2f}"
            else:
                answer = "Not a valid circle (r² < 0)"
                solution = f"Step 1: Calculate r² = g² + f² - c = {g}² + {f}² - {c} = {r_sq}\nStep 2: Since r² < 0, this is not a valid circle\nAnswer: Not a valid circle"
        
        elif q_type == 'find_center_radius':
            question = f"From (x-{h})² + (y-{k})² = {r**2}, find the center and radius"
            answer = f"Center: ({h}, {k}), Radius: {r}"
            solution = f"Step 1: Compare with standard form (x-h)² + (y-k)² = r²\nStep 2: h = {h}, k = {k}, r² = {r**2}\nStep 3: r = √{r**2} = {r}\nAnswer: Center ({h}, {k}), Radius {r}"
        
        elif q_type == 'equation_from_center_radius':
            question = f"A circle has center ({h}, {k}) and radius {r}. Find its equation in general form"
            # Expand: (x-h)² + (y-k)² = r²
            # x² - 2hx + h² + y² - 2ky + k² = r²
            # x² + y² - 2hx - 2ky + (h² + k² - r²) = 0
            c_term = h**2 + k**2 - r**2
            answer = f"x² + y² - {2*h}x - {2*k}y + {c_term} = 0"
            solution = f"Step 1: Standard form (x-{h})² + (y-{k})² = {r}²\nStep 2: Expand: x² - {2*h}x + {h**2} + y² - {2*k}y + {k**2} = {r**2}\nStep 3: Rearrange: x² + y² - {2*h}x - {2*k}y + {h**2 + k**2 - r**2} = 0\nAnswer: x² + y² - {2*h}x - {2*k}y + {c_term} = 0"
        
        elif q_type == 'diameter_form':
            x1, y1 = random.randint(-8, 8), random.randint(-8, 8)
            x2, y2 = random.randint(-8, 8), random.randint(-8, 8)
            question = f"Find equation of circle with diameter endpoints ({x1}, {y1}) and ({x2}, {y2})"
            h_calc = (x1 + x2) / 2
            k_calc = (y1 + y2) / 2
            r_calc = math.sqrt((x2-x1)**2 + (y2-y1)**2) / 2
            answer = f"(x-{h_calc})² + (y-{k_calc})² = {r_calc**2:.2f}"
            solution = f"Step 1: Center = midpoint = (({x1}+{x2})/2, ({y1}+{y2})/2) = ({h_calc}, {k_calc})\nStep 2: Diameter = √[({x2}-{x1})² + ({y2}-{y1})²] = {2*r_calc:.2f}\nStep 3: Radius = diameter/2 = {r_calc:.2f}\nStep 4: Equation: (x-{h_calc})² + (y-{k_calc})² = {r_calc**2:.2f}\nAnswer: (x-{h_calc})² + (y-{k_calc})² = {r_calc**2:.2f}"
        
        else:  # intercepts
            question = f"For circle x² + y² = {r**2}, find x-intercepts and y-intercepts"
            answer = f"x-intercepts: (±{r}, 0), y-intercepts: (0, ±{r})"
            solution = f"Step 1: For x-intercepts, set y=0: x² = {r**2}, x = ±{r}\nStep 2: For y-intercepts, set x=0: y² = {r**2}, y = ±{r}\nAnswer: x-intercepts (±{r}, 0), y-intercepts (0, ±{r})"
        
        questions.append({
            'id': f'circle_{i+1}',
            'question': question,
            'answer': answer,
            'solution': solution,
            'source': 'DDCET Syllabus Gap - Circle Equations'
        })
    
    return questions


def generate_parametric_differentiation(count=500):
    """Parametric differentiation - MISSING"""
    questions = []
    
    for i in range(count):
        a, b, n, m = random.randint(1, 5), random.randint(1, 5), random.randint(2, 4), random.randint(2, 4)
        
        q_type = random.choice(['basic', 'trig', 'power'])
        
        if q_type == 'basic':
            question = f"If x = {a}t² and y = {b}t³, find dy/dx"
            dx_dt = f"{2*a}t"
            dy_dt = f"{3*b}t²"
            answer = f"({3*b}t²)/({2*a}t) = ({3*b}/{2*a})t"
            solution = f"Step 1: Find dx/dt = d({a}t²)/dt = {2*a}t\nStep 2: Find dy/dt = d({b}t³)/dt = {3*b}t²\nStep 3: dy/dx = (dy/dt)/(dx/dt) = ({3*b}t²)/({2*a}t)\nStep 4: Simplify = ({3*b}/{2*a})t\nAnswer: ({3*b}/{2*a})t"
        
        elif q_type == 'trig':
            question = f"If x = {a}cos(t) and y = {b}sin(t), find dy/dx"
            answer = f"-({b}/{a})cot(t)"
            solution = f"Step 1: dx/dt = -{a}sin(t)\nStep 2: dy/dt = {b}cos(t)\nStep 3: dy/dx = ({b}cos(t))/(-{a}sin(t))\nStep 4: = -({b}/{a}) × (cos(t)/sin(t)) = -({b}/{a})cot(t)\nAnswer: -({b}/{a})cot(t)"
        
        else:  # power
            question = f"For x = t^{n}, y = t^{m}, find dy/dx at t = 2"
            dx_dt = f"{n}t^{n-1}"
            dy_dt = f"{m}t^{m-1}"
            at_t2 = (m * (2**(m-1))) / (n * (2**(n-1)))
            answer = f"{at_t2:.2f}"
            solution = f"Step 1: dx/dt = {n}t^{n-1}\nStep 2: dy/dt = {m}t^{m-1}\nStep 3: dy/dx = ({m}t^{m-1})/({n}t^{n-1}) = ({m}/{n})t^{m-n}\nStep 4: At t=2: ({m}/{n}) × 2^{m-n} = {at_t2:.2f}\nAnswer: {at_t2:.2f}"
        
        questions.append({
            'id': f'param_{i+1}',
            'question': question,
            'answer': answer,
            'solution': solution,
            'source': 'DDCET Syllabus Gap - Parametric Differentiation'
        })
    
    return questions


def generate_velocity_acceleration(count=500):
    """Velocity/Acceleration applications - MISSING"""
    questions = []
    
    for i in range(count):
        a, b, c = random.randint(1, 10), random.randint(1, 15), random.randint(1, 20)
        t = random.randint(1, 5)
        
        q_type = random.choice(['velocity', 'acceleration', 'both'])
        
        if q_type == 'velocity':
            question = f"If displacement s = {a}t² + {b}t + {c}, find velocity at t = {t} seconds"
            velocity = 2*a*t + b
            answer = f"{velocity} m/s"
            solution = f"Step 1: Velocity v = ds/dt\nStep 2: v = d({a}t² + {b}t + {c})/dt = {2*a}t + {b}\nStep 3: At t = {t}: v = {2*a}×{t} + {b} = {velocity}\nAnswer: {velocity} m/s"
        
        elif q_type == 'acceleration':
            question = f"If velocity v = {a}t² + {b}t, find acceleration at t = {t} seconds"
            acceleration = 2*a*t
            answer = f"{acceleration} m/s²"
            solution = f"Step 1: Acceleration a = dv/dt\nStep 2: a = d({a}t² + {b}t)/dt = {2*a}t\nStep 3: At t = {t}: a = {2*a}×{t} = {acceleration}\nAnswer: {acceleration} m/s²"
        
        else:  # both
            question = f"If s = {a}t³ + {b}t² + {c}, find velocity and acceleration at t = {t}"
            velocity = 3*a*t**2 + 2*b*t
            acceleration = 6*a*t + 2*b
            answer = f"v = {velocity} m/s, a = {acceleration} m/s²"
            solution = f"Step 1: v = ds/dt = {3*a}t² + {2*b}t\nStep 2: a = dv/dt = {6*a}t + {2*b}\nStep 3: At t={t}: v = {3*a}×{t}² + {2*b}×{t} = {velocity} m/s\nStep 4: a = {6*a}×{t} + {2*b} = {acceleration} m/s²\nAnswer: v = {velocity} m/s, a = {acceleration} m/s²"
        
        questions.append({
            'id': f'physics_{i+1}',
            'question': question,
            'answer': answer,
            'solution': solution,
            'source': 'DDCET Syllabus Gap - Physics Applications'
        })
    
    return questions


def generate_logarithm_questions(count=1000):
    """Complete Logarithm topic - COMPLETELY MISSING"""
    questions = []
    
    for i in range(count):
        a, b, c = random.randint(2, 9), random.randint(2, 9), random.randint(2, 9)
        x, y = random.randint(2, 20), random.randint(2, 20)
        
        q_type = random.choice([
            'basic', 'laws', 'change_of_base', 'equation', 'exponential_eq'
        ])
        
        if q_type == 'basic':
            base = random.choice([2, 3, 5, 10])
            value = base ** random.randint(2, 4)
            question = f"Evaluate: log_{base}({value})"
            answer = str(int(math.log(value, base)))
            solution = f"Step 1: Find x such that {base}^x = {value}\nStep 2: {base}^{int(math.log(value, base))} = {value}\nAnswer: {int(math.log(value, base))}"
        
        elif q_type == 'laws':
            law = random.choice(['product', 'quotient', 'power'])
            if law == 'product':
                question = f"Simplify: log({a}) + log({b})"
                answer = f"log({a*b})"
                solution = f"Step 1: Use log(a) + log(b) = log(ab)\nStep 2: log({a}) + log({b}) = log({a}×{b})\nAnswer: log({a*b})"
            elif law == 'quotient':
                question = f"Simplify: log({a*b}) - log({b})"
                answer = f"log({a})"
                solution = f"Step 1: Use log(a) - log(b) = log(a/b)\nStep 2: log({a*b}) - log({b}) = log({a*b}/{b})\nAnswer: log({a})"
            else:  # power
                n = random.randint(2, 4)
                question = f"Simplify: {n}log({a})"
                answer = f"log({a**n})"
                solution = f"Step 1: Use n×log(a) = log(a^n)\nStep 2: {n}log({a}) = log({a}^{n})\nAnswer: log({a**n})"
        
        elif q_type == 'change_of_base':
            question = f"Express log_{a}({x}) in terms of natural logarithm"
            answer = f"ln({x})/ln({a})"
            solution = f"Step 1: Use change of base formula: log_a(x) = ln(x)/ln(a)\nStep 2: log_{a}({x}) = ln({x})/ln({a})\nAnswer: ln({x})/ln({a})"
        
        elif q_type == 'equation':
            question = f"Solve: log(x) = {a}"
            answer = f"x = 10^{a}"
            solution = f"Step 1: If log(x) = {a}, then x = 10^{a}\nStep 2: x = {10**a}\nAnswer: x = {10**a}"
        
        else:  # exponential_eq
            question = f"Solve: {a}^x = {a**3}"
            answer = f"x = 3"
            solution = f"Step 1: Take log of both sides: log({a}^x) = log({a**3})\nStep 2: x×log({a}) = 3×log({a})\nStep 3: x = 3\nAnswer: x = 3"
        
        questions.append({
            'id': f'log_{i+1}',
            'question': question,
            'answer': answer,
            'solution': solution,
            'source': 'DDCET Syllabus Gap - Logarithm Complete'
        })
    
    return questions


def generate_statistics_questions(count=1000):
    """Statistics - COMPLETELY MISSING"""
    questions = []
    
    for i in range(count):
        n = random.randint(5, 12)
        data = sorted([random.randint(10, 99) for _ in range(n)])
        
        q_type = random.choice(['mean', 'median', 'mode', 'all'])
        
        mean_val = sum(data) / len(data)
        
        if len(data) % 2 == 0:
            median_val = (data[len(data)//2 - 1] + data[len(data)//2]) / 2
        else:
            median_val = data[len(data)//2]
        
        # Find mode
        from collections import Counter
        freq = Counter(data)
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]
        mode_val = modes[0] if len(modes) == 1 else "No unique mode"
        
        data_str = ", ".join(map(str, data))
        
        if q_type == 'mean':
            question = f"Find the mean of: {data_str}"
            answer = f"{mean_val:.2f}"
            solution = f"Step 1: Mean = (Sum of all values) / (Number of values)\nStep 2: Sum = {sum(data)}\nStep 3: Number of values = {len(data)}\nStep 4: Mean = {sum(data)}/{len(data)} = {mean_val:.2f}\nAnswer: {mean_val:.2f}"
        
        elif q_type == 'median':
            question = f"Find the median of: {data_str}"
            answer = f"{median_val}"
            if len(data) % 2 == 0:
                solution = f"Step 1: Arrange in order (already sorted)\nStep 2: n = {len(data)} (even)\nStep 3: Median = (n/2 term + (n/2+1) term)/2\nStep 4: Median = ({data[len(data)//2-1]} + {data[len(data)//2]})/2 = {median_val}\nAnswer: {median_val}"
            else:
                solution = f"Step 1: Arrange in order (already sorted)\nStep 2: n = {len(data)} (odd)\nStep 3: Median = middle term = {len(data)//2 + 1}th term\nStep 4: Median = {median_val}\nAnswer: {median_val}"
        
        elif q_type == 'mode':
            question = f"Find the mode of: {data_str}"
            answer = str(mode_val)
            solution = f"Step 1: Mode is the most frequently occurring value\nStep 2: Count frequencies\nStep 3: Highest frequency value = {mode_val}\nAnswer: {mode_val}"
        
        else:  # all
            question = f"Find mean, median, and mode of: {data_str}"
            answer = f"Mean: {mean_val:.2f}, Median: {median_val}, Mode: {mode_val}"
            solution = f"Step 1: Mean = {sum(data)}/{len(data)} = {mean_val:.2f}\nStep 2: Median (middle value) = {median_val}\nStep 3: Mode (most frequent) = {mode_val}\nAnswer: Mean: {mean_val:.2f}, Median: {median_val}, Mode: {mode_val}"
        
        questions.append({
            'id': f'stats_{i+1}',
            'question': question,
            'answer': answer,
            'solution': solution,
            'source': 'DDCET Syllabus Gap - Statistics Complete'
        })
    
    return questions


def save_to_json(topic, questions):
    """Save or append to JSON file"""
    banks_dir = "../question_generator/data/question_banks"
    filepath = os.path.join(banks_dir, f"{topic}.json")
    
    if os.path.exists(filepath):
        # Append to existing
        with open(filepath, 'r') as f:
            existing = json.load(f)
            existing_questions = existing.get('questions', [])
        
        # Append new questions
        all_questions = existing_questions + questions
        
        data = {
            "chapter": topic.replace('_', ' ').title(),
            "questions": all_questions,
            "total_questions": len(all_questions),
            "source": "JEE/GUJCET/DDCET Patterns + Gap Fill"
        }
    else:
        # Create new
        data = {
            "chapter": topic.replace('_', ' ').title(),
            "questions": questions,
            "total_questions": len(questions),
            "source": "DDCET Syllabus Gap Fill"
        }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    size_kb = os.path.getsize(filepath) / 1024
    print(f"✅ {topic}: {len(questions)} NEW questions added ({size_kb:.0f} KB total)")


def main():
    print("\n" + "="*70)
    print("FILLING DDCET SYLLABUS GAPS")
    print("="*70 + "\n")
    
    print("📝 Generating Circle questions (Coordinate Geometry gap)...")
    circles = generate_circle_questions(1000)
    
    print("📝 Generating Parametric Differentiation questions...")
    parametric = generate_parametric_differentiation(500)
    
    print("📝 Generating Velocity/Acceleration questions...")
    physics_app = generate_velocity_acceleration(500)
    
    print("📝 Generating Logarithm questions (COMPLETE TOPIC)...")
    logarithm = generate_logarithm_questions(1000)
    
    print("📝 Generating Statistics questions (COMPLETE TOPIC)...")
    statistics = generate_statistics_questions(1000)
    
    print("\n" + "="*70)
    print("SAVING TO JSON FILES...")
    print("="*70 + "\n")
    
    # Append circles to coordinate_geometry
    coord_geom = circles
    save_to_json("coordinate_geometry", coord_geom)
    
    # Append parametric + physics to differentiation
    diff_additions = parametric + physics_app
    save_to_json("differentiation", diff_additions)
    
    # Create NEW logarithm file
    save_to_json("logarithm", logarithm)
    
    # Create NEW statistics file
    save_to_json("statistics", statistics)
    
    print("\n" + "="*70)
    print(f"🎉 DONE! Added {len(circles) + len(parametric) + len(physics_app) + len(logarithm) + len(statistics)} questions!")
    print("="*70)


if __name__ == "__main__":
    main()

