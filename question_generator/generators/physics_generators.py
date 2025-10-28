"""
Physics Question Generators
Generates questions for all DDCET Physics topics
"""

import random
import math
from typing import List
import sympy as sp
from sympy import symbols, solve, sqrt

from ..core.question_engine import (
    Question, QuestionTemplate, FormulaBasedTemplate, 
    TextMutator, NumericalMutator
)


# ==================== MECHANICS ====================

class KinematicsGenerator(QuestionTemplate):
    """Generate kinematics questions - Linear Motion"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Kinematics")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['velocity', 'acceleration', 'displacement', 'time'])
            
            if q_type == 'velocity':
                questions.append(self._generate_velocity_question(difficulty))
            elif q_type == 'acceleration':
                questions.append(self._generate_acceleration_question(difficulty))
            elif q_type == 'displacement':
                questions.append(self._generate_displacement_question(difficulty))
            else:
                questions.append(self._generate_time_question(difficulty))
        
        return questions
    
    def _generate_velocity_question(self, difficulty: str) -> Question:
        """Generate velocity-related questions"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        u = random.uniform(0, mult["range"][1] / 10)
        a = random.uniform(1, mult["range"][1] / 20)
        t = random.uniform(1, mult["range"][1] / 10)
        
        u = round(u, mult["decimal"])
        a = round(a, mult["decimal"])
        t = round(t, mult["decimal"])
        
        # v = u + at
        v = u + a * t
        v = round(v, 2)
        
        objects = ["car", "train", "vehicle", "object", "particle"]
        actions = ["accelerates", "speeds up", "gains velocity"]
        
        obj = random.choice(objects)
        action = random.choice(actions)
        
        question_text = f"A {obj} {action} uniformly from {u} m/s at {a} m/s². Find the final velocity after {t} seconds."
        
        # Generate MCQ options or numerical answer
        if random.random() < 0.6:  # 60% MCQ
            distractors = self._generate_distractor_options(v, 3)
            options = [f"{v} m/s"] + [f"{d} m/s" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{v} m/s",
                options=options,
                solution=f"Using v = u + at = {u} + {a} × {t} = {v} m/s",
                tags=["kinematics", "velocity", "uniform_acceleration"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in m/s)",
                answer=v,
                solution=f"Using v = u + at = {u} + {a} × {t} = {v} m/s",
                tags=["kinematics", "velocity", "uniform_acceleration"]
            )
    
    def _generate_displacement_question(self, difficulty: str) -> Question:
        """Generate displacement questions using s = ut + 0.5at²"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        u = random.uniform(0, mult["range"][1] / 10)
        a = random.uniform(1, mult["range"][1] / 20)
        t = random.uniform(1, mult["range"][1] / 10)
        
        u = round(u, mult["decimal"])
        a = round(a, mult["decimal"])
        t = round(t, mult["decimal"])
        
        # s = ut + 0.5at²
        s = u * t + 0.5 * a * t**2
        s = round(s, 2)
        
        question_text = f"A particle starts with an initial velocity of {u} m/s and accelerates at {a} m/s². Calculate the distance traveled in {t} seconds."
        
        if random.random() < 0.5:
            distractors = self._generate_distractor_options(s, 3)
            options = [f"{s} m"] + [f"{d} m" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{s} m",
                options=options,
                solution=f"Using s = ut + ½at² = {u}×{t} + 0.5×{a}×{t}² = {s} m",
                tags=["kinematics", "displacement", "equations_of_motion"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text,
                answer=s,
                solution=f"Using s = ut + ½at² = {u}×{t} + 0.5×{a}×{t}² = {s} m",
                tags=["kinematics", "displacement", "equations_of_motion"]
            )
    
    def _generate_acceleration_question(self, difficulty: str) -> Question:
        """Generate acceleration calculation questions"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        u = random.uniform(0, mult["range"][1] / 10)
        v = random.uniform(u + 5, mult["range"][1] / 5)
        t = random.uniform(1, mult["range"][1] / 10)
        
        u = round(u, mult["decimal"])
        v = round(v, mult["decimal"])
        t = round(t, mult["decimal"])
        
        # a = (v - u) / t
        a = (v - u) / t
        a = round(a, 2)
        
        question_text = f"An object's velocity changes from {u} m/s to {v} m/s in {t} seconds. Find the acceleration."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text,
            answer=a,
            solution=f"a = (v - u) / t = ({v} - {u}) / {t} = {a} m/s²",
            tags=["kinematics", "acceleration"]
        )
    
    def _generate_time_question(self, difficulty: str) -> Question:
        """Generate time calculation questions"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        u = random.uniform(0, mult["range"][1] / 10)
        v = random.uniform(u + 5, mult["range"][1] / 5)
        a = random.uniform(1, mult["range"][1] / 20)
        
        u = round(u, mult["decimal"])
        v = round(v, mult["decimal"])
        a = round(a, mult["decimal"])
        
        # t = (v - u) / a
        t = (v - u) / a
        t = round(t, 2)
        
        question_text = f"How long will it take for an object to accelerate from {u} m/s to {v} m/s at {a} m/s²?"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in seconds)",
            answer=t,
            solution=f"t = (v - u) / a = ({v} - {u}) / {a} = {t} s",
            tags=["kinematics", "time"]
        )


class NewtonLawsGenerator(QuestionTemplate):
    """Generate questions on Newton's Laws of Motion"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Newton's Laws")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['force', 'mass', 'momentum', 'impulse'])
            
            if q_type == 'force':
                questions.append(self._generate_force_question(difficulty))
            elif q_type == 'mass':
                questions.append(self._generate_mass_question(difficulty))
            elif q_type == 'momentum':
                questions.append(self._generate_momentum_question(difficulty))
            else:
                questions.append(self._generate_impulse_question(difficulty))
        
        return questions
    
    def _generate_force_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, mult["range"][1] / 10)
        a = random.uniform(1, mult["range"][1] / 20)
        
        m = round(m, mult["decimal"])
        a = round(a, mult["decimal"])
        
        # F = ma
        F = m * a
        F = round(F, 2)
        
        question_text = f"Calculate the force required to accelerate a mass of {m} kg at {a} m/s²."
        
        if random.random() < 0.6:
            distractors = self._generate_distractor_options(F, 3)
            options = [f"{F} N"] + [f"{d} N" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{F} N",
                options=options,
                solution=f"F = ma = {m} × {a} = {F} N",
                tags=["newton_laws", "force", "second_law"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text,
                answer=F,
                solution=f"F = ma = {m} × {a} = {F} N",
                tags=["newton_laws", "force", "second_law"]
            )
    
    def _generate_momentum_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, mult["range"][1] / 10)
        v = random.uniform(1, mult["range"][1] / 10)
        
        m = round(m, mult["decimal"])
        v = round(v, mult["decimal"])
        
        # p = mv
        p = m * v
        p = round(p, 2)
        
        question_text = f"A body of mass {m} kg moves with velocity {v} m/s. Calculate its linear momentum."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in kg·m/s)",
            answer=p,
            solution=f"p = mv = {m} × {v} = {p} kg·m/s",
            tags=["momentum", "linear_momentum"]
        )
    
    def _generate_impulse_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, mult["range"][1] / 10)
        u = random.uniform(0, mult["range"][1] / 10)
        v = random.uniform(u + 5, mult["range"][1] / 5)
        
        m = round(m, mult["decimal"])
        u = round(u, mult["decimal"])
        v = round(v, mult["decimal"])
        
        # Impulse = change in momentum = m(v - u)
        impulse = m * (v - u)
        impulse = round(impulse, 2)
        
        question_text = f"A {m} kg object's velocity changes from {u} m/s to {v} m/s. Calculate the impulse."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in N·s)",
            answer=impulse,
            solution=f"Impulse = m(v - u) = {m}×({v} - {u}) = {impulse} N·s",
            tags=["impulse", "momentum", "change_in_momentum"]
        )
    
    def _generate_mass_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        F = random.uniform(10, mult["range"][1])
        a = random.uniform(1, mult["range"][1] / 20)
        
        F = round(F, mult["decimal"])
        a = round(a, mult["decimal"])
        
        # m = F / a
        m = F / a
        m = round(m, 2)
        
        question_text = f"A force of {F} N produces an acceleration of {a} m/s². Find the mass of the object."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in kg)",
            answer=m,
            solution=f"m = F / a = {F} / {a} = {m} kg",
            tags=["newton_laws", "mass", "second_law"]
        )


class CircularMotionGenerator(QuestionTemplate):
    """Generate circular motion questions"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Circular Motion")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['centripetal_force', 'angular_velocity', 'centripetal_acceleration'])
            
            if q_type == 'centripetal_force':
                questions.append(self._generate_centripetal_force_question(difficulty))
            elif q_type == 'angular_velocity':
                questions.append(self._generate_angular_velocity_question(difficulty))
            else:
                questions.append(self._generate_centripetal_acceleration_question(difficulty))
        
        return questions
    
    def _generate_centripetal_force_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, mult["range"][1] / 10)
        v = random.uniform(5, mult["range"][1] / 5)
        r = random.uniform(1, mult["range"][1] / 10)
        
        m = round(m, mult["decimal"])
        v = round(v, mult["decimal"])
        r = round(r, mult["decimal"])
        
        # F = mv²/r
        F = m * v**2 / r
        F = round(F, 2)
        
        question_text = f"A {m} kg object moves in a circular path of radius {r} m with speed {v} m/s. Calculate the centripetal force."
        
        if random.random() < 0.6:
            distractors = self._generate_distractor_options(F, 3)
            options = [f"{F} N"] + [f"{d} N" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{F} N",
                options=options,
                solution=f"F = mv²/r = {m} × {v}² / {r} = {F} N",
                tags=["circular_motion", "centripetal_force"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text,
                answer=F,
                solution=f"F = mv²/r = {m} × {v}² / {r} = {F} N",
                tags=["circular_motion", "centripetal_force"]
            )
    
    def _generate_angular_velocity_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        v = random.uniform(5, mult["range"][1] / 5)
        r = random.uniform(1, mult["range"][1] / 10)
        
        v = round(v, mult["decimal"])
        r = round(r, mult["decimal"])
        
        # ω = v/r
        omega = v / r
        omega = round(omega, 2)
        
        question_text = f"An object moves with speed {v} m/s in a circle of radius {r} m. Find the angular velocity."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in rad/s)",
            answer=omega,
            solution=f"ω = v/r = {v} / {r} = {omega} rad/s",
            tags=["circular_motion", "angular_velocity"]
        )
    
    def _generate_centripetal_acceleration_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        v = random.uniform(5, mult["range"][1] / 5)
        r = random.uniform(1, mult["range"][1] / 10)
        
        v = round(v, mult["decimal"])
        r = round(r, mult["decimal"])
        
        # a = v²/r
        a = v**2 / r
        a = round(a, 2)
        
        question_text = f"Calculate the centripetal acceleration of an object moving at {v} m/s in a circular path of radius {r} m."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in m/s²)",
            answer=a,
            solution=f"a = v²/r = {v}² / {r} = {a} m/s²",
            tags=["circular_motion", "centripetal_acceleration"]
        )


class WorkEnergyGenerator(QuestionTemplate):
    """Generate work, energy, and power questions"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Work and Energy")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['work', 'kinetic_energy', 'potential_energy', 'power'])
            
            if q_type == 'work':
                questions.append(self._generate_work_question(difficulty))
            elif q_type == 'kinetic_energy':
                questions.append(self._generate_ke_question(difficulty))
            elif q_type == 'potential_energy':
                questions.append(self._generate_pe_question(difficulty))
            else:
                questions.append(self._generate_power_question(difficulty))
        
        return questions
    
    def _generate_work_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        F = random.uniform(10, mult["range"][1])
        d = random.uniform(1, mult["range"][1] / 10)
        
        F = round(F, mult["decimal"])
        d = round(d, mult["decimal"])
        
        # W = F × d
        W = F * d
        W = round(W, 2)
        
        question_text = f"A force of {F} N displaces an object by {d} m in the direction of force. Calculate the work done."
        
        if random.random() < 0.6:
            distractors = self._generate_distractor_options(W, 3)
            options = [f"{W} J"] + [f"{d} J" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{W} J",
                options=options,
                solution=f"W = F × d = {F} × {d} = {W} J",
                tags=["work", "energy", "work_energy"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text,
                answer=W,
                solution=f"W = F × d = {F} × {d} = {W} J",
                tags=["work", "energy", "work_energy"]
            )
    
    def _generate_ke_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, mult["range"][1] / 10)
        v = random.uniform(5, mult["range"][1] / 5)
        
        m = round(m, mult["decimal"])
        v = round(v, mult["decimal"])
        
        # KE = 0.5 × m × v²
        KE = 0.5 * m * v**2
        KE = round(KE, 2)
        
        question_text = f"Find the kinetic energy of a {m} kg object moving at {v} m/s."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in J)",
            answer=KE,
            solution=f"KE = ½mv² = 0.5 × {m} × {v}² = {KE} J",
            tags=["kinetic_energy", "energy"]
        )
    
    def _generate_pe_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, mult["range"][1] / 10)
        h = random.uniform(1, mult["range"][1] / 10)
        g = 9.8  # Standard gravity
        
        m = round(m, mult["decimal"])
        h = round(h, mult["decimal"])
        
        # PE = mgh
        PE = m * g * h
        PE = round(PE, 2)
        
        question_text = f"Calculate the potential energy of a {m} kg object at height {h} m. (Take g = 9.8 m/s²)"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in J)",
            answer=PE,
            solution=f"PE = mgh = {m} × 9.8 × {h} = {PE} J",
            tags=["potential_energy", "energy", "gravitational_pe"]
        )
    
    def _generate_power_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        W = random.uniform(100, mult["range"][1] * 10)
        t = random.uniform(1, mult["range"][1] / 10)
        
        W = round(W, mult["decimal"])
        t = round(t, mult["decimal"])
        
        # P = W / t
        P = W / t
        P = round(P, 2)
        
        question_text = f"If {W} J of work is done in {t} seconds, calculate the power."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in W)",
            answer=P,
            solution=f"P = W / t = {W} / {t} = {P} W",
            tags=["power", "energy", "work_power"]
        )


# ==================== ELECTRICITY & MAGNETISM ====================

class OhmsLawGenerator(QuestionTemplate):
    """Generate Ohm's Law and resistance questions"""
    
    def __init__(self):
        super().__init__("Physics", "Electric Current", "Ohm's Law")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['current', 'voltage', 'resistance', 'power'])
            
            if q_type == 'current':
                questions.append(self._generate_current_question(difficulty))
            elif q_type == 'voltage':
                questions.append(self._generate_voltage_question(difficulty))
            elif q_type == 'resistance':
                questions.append(self._generate_resistance_question(difficulty))
            else:
                questions.append(self._generate_power_question(difficulty))
        
        return questions
    
    def _generate_current_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        V = random.uniform(1, mult["range"][1] / 10)
        R = random.uniform(1, mult["range"][1] / 10)
        
        V = round(V, mult["decimal"])
        R = round(R, mult["decimal"])
        
        # I = V / R
        I = V / R
        I = round(I, 2)
        
        question_text = f"A voltage of {V} V is applied across a resistance of {R} Ω. Calculate the current."
        
        if random.random() < 0.6:
            distractors = self._generate_distractor_options(I, 3)
            options = [f"{I} A"] + [f"{d} A" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{I} A",
                options=options,
                solution=f"I = V / R = {V} / {R} = {I} A",
                tags=["ohms_law", "current", "electricity"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in A)",
                answer=I,
                solution=f"I = V / R = {V} / {R} = {I} A",
                tags=["ohms_law", "current", "electricity"]
            )
    
    def _generate_voltage_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        I = random.uniform(0.1, mult["range"][1] / 100)
        R = random.uniform(1, mult["range"][1] / 10)
        
        I = round(I, mult["decimal"] + 1)
        R = round(R, mult["decimal"])
        
        # V = I × R
        V = I * R
        V = round(V, 2)
        
        question_text = f"A current of {I} A flows through a {R} Ω resistor. Find the voltage across it."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in V)",
            answer=V,
            solution=f"V = I × R = {I} × {R} = {V} V",
            tags=["ohms_law", "voltage", "electricity"]
        )
    
    def _generate_resistance_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        V = random.uniform(1, mult["range"][1] / 10)
        I = random.uniform(0.1, mult["range"][1] / 100)
        
        V = round(V, mult["decimal"])
        I = round(I, mult["decimal"] + 1)
        
        # R = V / I
        R = V / I
        R = round(R, 2)
        
        question_text = f"When {V} V is applied, a current of {I} A flows. Calculate the resistance."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Ω)",
            answer=R,
            solution=f"R = V / I = {V} / {I} = {R} Ω",
            tags=["ohms_law", "resistance", "electricity"]
        )
    
    def _generate_power_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        V = random.uniform(1, mult["range"][1] / 10)
        I = random.uniform(0.1, mult["range"][1] / 100)
        
        V = round(V, mult["decimal"])
        I = round(I, mult["decimal"] + 1)
        
        # P = V × I
        P = V * I
        P = round(P, 2)
        
        question_text = f"Calculate the power dissipated when {V} V drives {I} A through a resistor."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in W)",
            answer=P,
            solution=f"P = V × I = {V} × {I} = {P} W",
            tags=["power", "electricity", "electrical_power"]
        )


class CapacitanceGenerator(QuestionTemplate):
    """Generate capacitance questions"""
    
    def __init__(self):
        super().__init__("Physics", "Electric Current", "Capacitance")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['charge', 'energy', 'series', 'parallel'])
            
            if q_type == 'charge':
                questions.append(self._generate_charge_question(difficulty))
            elif q_type == 'energy':
                questions.append(self._generate_energy_question(difficulty))
            elif q_type == 'series':
                questions.append(self._generate_series_question(difficulty))
            else:
                questions.append(self._generate_parallel_question(difficulty))
        
        return questions
    
    def _generate_charge_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C = random.uniform(1, mult["range"][1] / 10)
        V = random.uniform(1, mult["range"][1] / 10)
        
        C = round(C, mult["decimal"])
        V = round(V, mult["decimal"])
        
        # Q = C × V
        Q = C * V
        Q = round(Q, 2)
        
        question_text = f"A {C} μF capacitor is charged to {V} V. Calculate the charge stored."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in μC)",
            answer=Q,
            solution=f"Q = C × V = {C} × {V} = {Q} μC",
            tags=["capacitance", "charge", "electricity"]
        )
    
    def _generate_energy_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C = random.uniform(1, mult["range"][1] / 10)
        V = random.uniform(1, mult["range"][1] / 10)
        
        C = round(C, mult["decimal"])
        V = round(V, mult["decimal"])
        
        # U = 0.5 × C × V²
        U = 0.5 * C * V**2
        U = round(U, 2)
        
        question_text = f"Find the energy stored in a {C} μF capacitor charged to {V} V."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in μJ)",
            answer=U,
            solution=f"U = ½CV² = 0.5 × {C} × {V}² = {U} μJ",
            tags=["capacitance", "energy", "stored_energy"]
        )
    
    def _generate_series_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C1 = random.uniform(1, mult["range"][1] / 10)
        C2 = random.uniform(1, mult["range"][1] / 10)
        
        C1 = round(C1, mult["decimal"])
        C2 = round(C2, mult["decimal"])
        
        # 1/C_eq = 1/C1 + 1/C2
        C_eq = (C1 * C2) / (C1 + C2)
        C_eq = round(C_eq, 2)
        
        question_text = f"Two capacitors of {C1} μF and {C2} μF are connected in series. Find the equivalent capacitance."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in μF)",
            answer=C_eq,
            solution=f"1/C_eq = 1/{C1} + 1/{C2}, C_eq = {C_eq} μF",
            tags=["capacitance", "series", "combination"]
        )
    
    def _generate_parallel_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C1 = random.uniform(1, mult["range"][1] / 10)
        C2 = random.uniform(1, mult["range"][1] / 10)
        
        C1 = round(C1, mult["decimal"])
        C2 = round(C2, mult["decimal"])
        
        # C_eq = C1 + C2
        C_eq = C1 + C2
        C_eq = round(C_eq, 2)
        
        question_text = f"Two capacitors of {C1} μF and {C2} μF are connected in parallel. Find the equivalent capacitance."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in μF)",
            answer=C_eq,
            solution=f"C_eq = C1 + C2 = {C1} + {C2} = {C_eq} μF",
            tags=["capacitance", "parallel", "combination"]
        )


# ==================== HEAT & THERMODYNAMICS ====================

class HeatTransferGenerator(QuestionTemplate):
    """Generate heat transfer questions"""
    
    def __init__(self):
        super().__init__("Physics", "Heat and Thermometry", "Heat Transfer")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['heat_capacity', 'specific_heat', 'temperature_conversion'])
            
            if q_type == 'heat_capacity':
                questions.append(self._generate_heat_capacity_question(difficulty))
            elif q_type == 'specific_heat':
                questions.append(self._generate_specific_heat_question(difficulty))
            else:
                questions.append(self._generate_temp_conversion_question(difficulty))
        
        return questions
    
    def _generate_heat_capacity_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(0.1, mult["range"][1] / 100)
        c = random.uniform(100, mult["range"][1] * 10)
        dT = random.uniform(10, mult["range"][1] / 5)
        
        m = round(m, mult["decimal"] + 1)
        c = round(c, 0)
        dT = round(dT, mult["decimal"])
        
        # Q = mcΔT
        Q = m * c * dT
        Q = round(Q, 2)
        
        question_text = f"Calculate the heat required to raise the temperature of {m} kg of a substance (specific heat = {c} J/kg·K) by {dT} K."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in J)",
            answer=Q,
            solution=f"Q = mcΔT = {m} × {c} × {dT} = {Q} J",
            tags=["heat_transfer", "heat_capacity", "specific_heat"]
        )
    
    def _generate_specific_heat_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        Q = random.uniform(100, mult["range"][1] * 10)
        m = random.uniform(0.1, mult["range"][1] / 100)
        dT = random.uniform(10, mult["range"][1] / 5)
        
        Q = round(Q, mult["decimal"])
        m = round(m, mult["decimal"] + 1)
        dT = round(dT, mult["decimal"])
        
        # c = Q / (m × ΔT)
        c = Q / (m * dT)
        c = round(c, 2)
        
        question_text = f"If {Q} J of heat raises the temperature of {m} kg substance by {dT} K, find the specific heat."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in J/kg·K)",
            answer=c,
            solution=f"c = Q / (m × ΔT) = {Q} / ({m} × {dT}) = {c} J/kg·K",
            tags=["heat_transfer", "specific_heat"]
        )
    
    def _generate_temp_conversion_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        conversion_type = random.choice(['C_to_F', 'F_to_C', 'C_to_K', 'K_to_C'])
        
        if conversion_type == 'C_to_F':
            C = random.uniform(-50, mult["range"][1] / 2)
            C = round(C, mult["decimal"])
            F = (9/5) * C + 32
            F = round(F, 2)
            
            question_text = f"Convert {C}°C to Fahrenheit."
            solution = f"F = (9/5)C + 32 = (9/5) × {C} + 32 = {F}°F"
            answer = F
            unit = "°F"
        
        elif conversion_type == 'F_to_C':
            F = random.uniform(0, mult["range"][1])
            F = round(F, mult["decimal"])
            C = (5/9) * (F - 32)
            C = round(C, 2)
            
            question_text = f"Convert {F}°F to Celsius."
            solution = f"C = (5/9)(F - 32) = (5/9) × ({F} - 32) = {C}°C"
            answer = C
            unit = "°C"
        
        elif conversion_type == 'C_to_K':
            C = random.uniform(-50, mult["range"][1] / 2)
            C = round(C, mult["decimal"])
            K = C + 273.15
            K = round(K, 2)
            
            question_text = f"Convert {C}°C to Kelvin."
            solution = f"K = C + 273.15 = {C} + 273.15 = {K} K"
            answer = K
            unit = "K"
        
        else:  # K_to_C
            K = random.uniform(273, mult["range"][1] + 273)
            K = round(K, mult["decimal"])
            C = K - 273.15
            C = round(C, 2)
            
            question_text = f"Convert {K} K to Celsius."
            solution = f"C = K - 273.15 = {K} - 273.15 = {C}°C"
            answer = C
            unit = "°C"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text,
            answer=answer,
            solution=solution,
            tags=["temperature", "conversion", "thermometry"]
        )


# ==================== WAVES & OPTICS ====================

class WaveMotionGenerator(QuestionTemplate):
    """Generate wave motion questions"""
    
    def __init__(self):
        super().__init__("Physics", "Wave Motion and Optics", "Waves")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['frequency', 'wavelength', 'speed', 'period'])
            
            if q_type == 'frequency':
                questions.append(self._generate_frequency_question(difficulty))
            elif q_type == 'wavelength':
                questions.append(self._generate_wavelength_question(difficulty))
            elif q_type == 'speed':
                questions.append(self._generate_speed_question(difficulty))
            else:
                questions.append(self._generate_period_question(difficulty))
        
        return questions
    
    def _generate_frequency_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        T = random.uniform(0.001, mult["range"][1] / 1000)
        T = round(T, mult["decimal"] + 3)
        
        # f = 1 / T
        f = 1 / T
        f = round(f, 2)
        
        question_text = f"A wave has a period of {T} s. Calculate its frequency."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Hz)",
            answer=f,
            solution=f"f = 1/T = 1/{T} = {f} Hz",
            tags=["waves", "frequency", "period"]
        )
    
    def _generate_wavelength_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        v = random.uniform(100, mult["range"][1] * 10)
        f = random.uniform(10, mult["range"][1])
        
        v = round(v, mult["decimal"])
        f = round(f, mult["decimal"])
        
        # λ = v / f
        wavelength = v / f
        wavelength = round(wavelength, 2)
        
        question_text = f"A wave travels at {v} m/s with frequency {f} Hz. Find the wavelength."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in m)",
            answer=wavelength,
            solution=f"λ = v/f = {v}/{f} = {wavelength} m",
            tags=["waves", "wavelength", "wave_equation"]
        )
    
    def _generate_speed_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        f = random.uniform(10, mult["range"][1])
        wavelength = random.uniform(0.1, mult["range"][1] / 10)
        
        f = round(f, mult["decimal"])
        wavelength = round(wavelength, mult["decimal"])
        
        # v = f × λ
        v = f * wavelength
        v = round(v, 2)
        
        question_text = f"A wave has frequency {f} Hz and wavelength {wavelength} m. Calculate the wave speed."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in m/s)",
            answer=v,
            solution=f"v = fλ = {f} × {wavelength} = {v} m/s",
            tags=["waves", "wave_speed", "wave_equation"]
        )
    
    def _generate_period_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        f = random.uniform(10, mult["range"][1])
        f = round(f, mult["decimal"])
        
        # T = 1 / f
        T = 1 / f
        T = round(T, 4)
        
        question_text = f"Find the period of a wave with frequency {f} Hz."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in s)",
            answer=T,
            solution=f"T = 1/f = 1/{f} = {T} s",
            tags=["waves", "period", "frequency"]
        )

