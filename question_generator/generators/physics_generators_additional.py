"""
Additional Physics Question Generators for DDCET Syllabus
Covers remaining DDCET topics: Units & Measurement, Electrostatics, and Optics
"""

import random
import math
from typing import List

from ..core.question_engine import Question, QuestionTemplate


# ==================== TOPIC 1: PHYSICAL QUANTITIES & UNITS ====================

class UnitsAndMeasurementGenerator(QuestionTemplate):
    """Generate questions on physical quantities, units, errors and measurements for DDCET"""
    
    def __init__(self):
        super().__init__("Physics", "Physical Quantities and Units", "Units and Measurement")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['unit_conversion', 'error_calculation', 'vernier_caliper', 'micrometer', 'relative_error'])
            
            if q_type == 'unit_conversion':
                questions.append(self._generate_unit_conversion_question())
            elif q_type == 'error_calculation':
                questions.append(self._generate_error_question())
            elif q_type == 'vernier_caliper':
                questions.append(self._generate_vernier_question())
            elif q_type == 'micrometer':
                questions.append(self._generate_micrometer_question())
            else:
                questions.append(self._generate_relative_error_question())
        
        return questions
    
    def _generate_unit_conversion_question(self) -> Question:
        """MKS (SI) to CGS conversion and vice versa"""
        
        conversions = [
            {'from': 'SI', 'to': 'CGS', 'quantity': 'force', 'value': random.uniform(1, 100),
             'si_unit': 'N', 'cgs_unit': 'dyne', 'factor': 1e5, 'operation': '*'},
            {'from': 'SI', 'to': 'CGS', 'quantity': 'energy', 'value': random.uniform(1, 50),
             'si_unit': 'J', 'cgs_unit': 'erg', 'factor': 1e7, 'operation': '*'},
            {'from': 'SI', 'to': 'CGS', 'quantity': 'pressure', 'value': random.uniform(1, 10),
             'si_unit': 'Pa', 'cgs_unit': 'dyne/cm²', 'factor': 10, 'operation': '*'},
            {'from': 'CGS', 'to': 'SI', 'quantity': 'length', 'value': random.uniform(100, 1000),
             'cgs_unit': 'cm', 'si_unit': 'm', 'factor': 100, 'operation': '/'},
            {'from': 'CGS', 'to': 'SI', 'quantity': 'mass', 'value': random.uniform(100, 5000),
             'cgs_unit': 'g', 'si_unit': 'kg', 'factor': 1000, 'operation': '/'}
        ]
        
        conv = random.choice(conversions)
        value = round(conv['value'], 2)
        
        if conv['operation'] == '*':
            result = value * conv['factor']
            from_unit = conv.get('si_unit', conv.get('cgs_unit'))
            to_unit = conv.get('cgs_unit', conv.get('si_unit'))
        else:
            result = value / conv['factor']
            from_unit = conv.get('cgs_unit', conv.get('si_unit'))
            to_unit = conv.get('si_unit', conv.get('cgs_unit'))
        
        result = round(result, 6) if result < 1 else round(result, 2)
        
        question_text = f"Convert {value} {from_unit} of {conv['quantity']} to {conv['to']} system."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text,
            answer=result,
            solution=f"Conversion: {value} {from_unit} {'×' if conv['operation'] == '*' else '÷'} {conv['factor']} = {result} {to_unit}",
            tags=["unit_conversion", "MKS", "CGS", "ddcet_physics"]
        )
    
    def _generate_error_question(self) -> Question:
        measured_value = round(random.uniform(50, 500), 2)
        error = round(random.uniform(0.1, 5), 2)
        
        relative_error = round(error / measured_value, 4)
        percentage_error = round(relative_error * 100, 2)
        
        quantity = random.choice(['length', 'mass', 'time', 'voltage', 'current'])
        question_text = f"A {quantity} is measured as {measured_value} units with absolute error ±{error} units. Calculate the percentage error."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text,
            answer=percentage_error,
            solution=f"Relative error = {error}/{measured_value} = {relative_error}. Percentage error = {percentage_error}%",
            tags=["error_estimation", "percentage_error", "ddcet_physics"]
        )
    
    def _generate_vernier_question(self) -> Question:
        msr = random.randint(10, 95)
        vsd = random.randint(1, 9)
        total = round(msr + (vsd * 0.1), 1)
        
        question_text = f"A vernier caliper (least count 0.1 mm) shows main scale reading {msr} mm and the {vsd}th vernier division coincides with a main scale division. Find the measurement."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in mm)",
            answer=total,
            solution=f"Total = MSR + (VSD × LC) = {msr} + ({vsd} × 0.1) = {total} mm",
            tags=["vernier_caliper", "measurement", "ddcet_physics"]
        )
    
    def _generate_micrometer_question(self) -> Question:
        psr = round(random.uniform(2.0, 8.0), 1)
        csd = random.randint(10, 45)
        total = round(psr + (csd * 0.01), 2)
        
        question_text = f"A micrometer screw gauge (least count 0.01 mm) shows pitch scale reading {psr} mm and circular scale shows {csd}th division. Find the reading."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in mm)",
            answer=total,
            solution=f"Total = PSR + (CSD × LC) = {psr} + ({csd} × 0.01) = {total} mm",
            tags=["micrometer", "measurement", "ddcet_physics"]
        )
    
    def _generate_relative_error_question(self) -> Question:
        x, y = round(random.uniform(10, 50), 1), round(random.uniform(5, 30), 1)
        dx, dy = round(random.uniform(0.1, 2), 2), round(random.uniform(0.1, 1.5), 2)
        
        relative_error = round((dx/x) + (dy/y), 4)
        
        op = random.choice(['multiply', 'divide'])
        question_text = f"Two quantities x = {x} ± {dx} and y = {y} ± {dy}. Find relative error in x {' × ' if op == 'multiply' else ' ÷ '} y."
        solution = f"For {'product' if op == 'multiply' else 'quotient'}: Relative error = Δx/x + Δy/y = {dx}/{x} + {dy}/{y} = {relative_error}"
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text,
            answer=relative_error,
            solution=solution,
            tags=["error_propagation", "ddcet_physics"]
        )


# ==================== TOPIC 3: ELECTROSTATICS ====================

class ElectrostaticsGenerator(QuestionTemplate):
    """Generate questions on Coulomb's Law, Electric Field, and Electric Potential for DDCET"""
    
    def __init__(self):
        super().__init__("Physics", "Electric Current", "Electrostatics")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['coulombs_law', 'electric_field', 'electric_potential', 'electric_flux'])
            
            if q_type == 'coulombs_law':
                questions.append(self._generate_coulombs_law_question())
            elif q_type == 'electric_field':
                questions.append(self._generate_electric_field_question())
            elif q_type == 'electric_potential':
                questions.append(self._generate_potential_question())
            else:
                questions.append(self._generate_flux_question())
        
        return questions
    
    def _generate_coulombs_law_question(self) -> Question:
        q1 = round(random.uniform(1, 10), 1)  # μC
        q2 = round(random.uniform(1, 10), 1)  # μC
        r = round(random.uniform(0.1, 1.0), 2)  # m
        k = 9e9  # N⋅m²/C²
        
        # F = k⋅q1⋅q2 / r²
        F = k * (q1 * 1e-6) * (q2 * 1e-6) / (r ** 2)
        F = round(F, 4)
        
        question_text = f"Two point charges {q1} μC and {q2} μC are placed {r} m apart in air. Calculate the electrostatic force between them using Coulomb's law. (k = 9×10⁹ N⋅m²/C²)"
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in Newtons)",
            answer=F,
            solution=f"F = k⋅q1⋅q2 / r² = 9×10⁹ × {q1}×10⁻⁶ × {q2}×10⁻⁶ / {r}² = {F} N",
            tags=["coulombs_law", "electrostatics", "force", "ddcet_physics"]
        )
    
    def _generate_electric_field_question(self) -> Question:
        q = round(random.uniform(1, 20), 1)  # μC
        r = round(random.uniform(0.1, 2.0), 2)  # m
        k = 9e9
        
        # E = k⋅q / r²
        E = k * (q * 1e-6) / (r ** 2)
        E = round(E, 2)
        
        question_text = f"A point charge of {q} μC is placed in air. Calculate the electric field intensity at a distance of {r} m from the charge."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in N/C)",
            answer=E,
            solution=f"E = k⋅q / r² = 9×10⁹ × {q}×10⁻⁶ / {r}² = {E} N/C",
            tags=["electric_field", "electrostatics", "ddcet_physics"]
        )
    
    def _generate_potential_question(self) -> Question:
        q = round(random.uniform(1, 15), 1)  # μC
        r = round(random.uniform(0.1, 2.0), 2)  # m
        k = 9e9
        
        # V = k⋅q / r
        V = k * (q * 1e-6) / r
        V = round(V, 2)
        
        question_text = f"Calculate the electric potential at a point {r} m away from a point charge of {q} μC."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in Volts)",
            answer=V,
            solution=f"V = k⋅q / r = 9×10⁹ × {q}×10⁻⁶ / {r} = {V} V",
            tags=["electric_potential", "electrostatics", "ddcet_physics"]
        )
    
    def _generate_flux_question(self) -> Question:
        q = round(random.uniform(1, 20), 1)  # μC
        epsilon_0 = 8.85e-12  # C²/N⋅m²
        
        # Φ = q / ε₀
        flux = (q * 1e-6) / epsilon_0
        flux = round(flux, 2)
        
        question_text = f"A point charge of {q} μC is enclosed by a closed surface. Calculate the total electric flux through the surface using Gauss's law. (ε₀ = 8.85×10⁻¹² C²/N⋅m²)"
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in N⋅m²/C)",
            answer=flux,
            solution=f"Φ = q / ε₀ = {q}×10⁻⁶ / 8.85×10⁻¹² = {flux} N⋅m²/C",
            tags=["electric_flux", "gauss_law", "electrostatics", "ddcet_physics"]
        )


# ==================== TOPIC 5: OPTICS ====================

class OpticsGenerator(QuestionTemplate):
    """Generate questions on Reflection, Refraction, Snell's Law, and Optical Fiber for DDCET"""
    
    def __init__(self):
        super().__init__("Physics", "Wave Motion and Optics", "Optics")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['snells_law', 'refractive_index', 'total_internal_reflection', 'critical_angle', 'optical_fiber'])
            
            if q_type == 'snells_law':
                questions.append(self._generate_snells_law_question())
            elif q_type == 'refractive_index':
                questions.append(self._generate_refractive_index_question())
            elif q_type == 'total_internal_reflection':
                questions.append(self._generate_tir_question())
            elif q_type == 'critical_angle':
                questions.append(self._generate_critical_angle_question())
            else:
                questions.append(self._generate_optical_fiber_question())
        
        return questions
    
    def _generate_snells_law_question(self) -> Question:
        n1 = round(random.uniform(1.0, 1.5), 2)
        n2 = round(random.uniform(1.3, 2.0), 2)
        theta1 = random.randint(20, 60)
        
        # n1⋅sin(θ1) = n2⋅sin(θ2)
        theta2_rad = math.asin((n1 * math.sin(math.radians(theta1))) / n2)
        theta2 = round(math.degrees(theta2_rad), 2)
        
        question_text = f"Light travels from a medium with refractive index {n1} to another medium with refractive index {n2}. If the angle of incidence is {theta1}°, calculate the angle of refraction using Snell's law."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in degrees)",
            answer=theta2,
            solution=f"Using Snell's law: n₁⋅sin(θ₁) = n₂⋅sin(θ₂)\n{n1}⋅sin({theta1}°) = {n2}⋅sin(θ₂)\nθ₂ = {theta2}°",
            tags=["snells_law", "refraction", "optics", "ddcet_physics"]
        )
    
    def _generate_refractive_index_question(self) -> Question:
        c = 3e8  # m/s
        v = round(random.uniform(1.5e8, 2.5e8), 2)  # m/s
        
        n = c / v
        n = round(n, 2)
        
        question_text = f"Light travels at {v:.2e} m/s in a certain medium. Calculate the absolute refractive index of the medium. (Speed of light in vacuum = 3×10⁸ m/s)"
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text,
            answer=n,
            solution=f"Refractive index n = c / v = 3×10⁸ / {v:.2e} = {n}",
            tags=["refractive_index", "optics", "ddcet_physics"]
        )
    
    def _generate_critical_angle_question(self) -> Question:
        n1 = round(random.uniform(1.4, 1.8), 2)
        n2 = 1.0  # air
        
        # sin(θc) = n2 / n1
        theta_c_rad = math.asin(n2 / n1)
        theta_c = round(math.degrees(theta_c_rad), 2)
        
        question_text = f"Calculate the critical angle for light traveling from a medium of refractive index {n1} to air (n = 1.0)."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in degrees)",
            answer=theta_c,
            solution=f"Critical angle: sin(θc) = n₂/n₁ = 1.0/{n1} = {1/n1:.4f}\nθc = {theta_c}°",
            tags=["critical_angle", "total_internal_reflection", "optics", "ddcet_physics"]
        )
    
    def _generate_tir_question(self) -> Question:
        n_dense = round(random.uniform(1.4, 1.7), 2)
        n_rare = 1.0
        theta = random.randint(50, 80)
        
        theta_c_rad = math.asin(n_rare / n_dense)
        theta_c = round(math.degrees(theta_c_rad), 2)
        
        will_tir = theta > theta_c
        
        question_text = f"Light travels from a denser medium (n = {n_dense}) to air at an angle of incidence {theta}°. The critical angle is {theta_c}°. Will total internal reflection occur?"
        
        answer = "Yes" if will_tir else "No"
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="mcq",
            question_text=question_text,
            answer=answer,
            options=["Yes", "No"],
            solution=f"Since {theta}° {'>' if will_tir else '<'} {theta_c}° (critical angle), total internal reflection {'will' if will_tir else 'will not'} occur.",
            tags=["total_internal_reflection", "optics", "ddcet_physics"]
        )
    
    def _generate_optical_fiber_question(self) -> Question:
        n_core = round(random.uniform(1.45, 1.55), 2)
        n_cladding = round(n_core - random.uniform(0.01, 0.05), 2)
        
        # Critical angle for optical fiber
        theta_c_rad = math.asin(n_cladding / n_core)
        theta_c = round(math.degrees(theta_c_rad), 2)
        
        question_text = f"An optical fiber has a core refractive index of {n_core} and cladding refractive index of {n_cladding}. Calculate the critical angle for total internal reflection in the fiber, which is essential for light propagation through the fiber."
        
        return Question(
            subject=self.subject, chapter=self.chapter, subtopic=self.subtopic,
            difficulty="medium", question_type="numerical",
            question_text=question_text + " (Answer in degrees)",
            answer=theta_c,
            solution=f"Critical angle: sin(θc) = n_cladding / n_core = {n_cladding}/{n_core}\nθc = {theta_c}°. For TIR in fiber, angle must exceed this.",
            tags=["optical_fiber", "critical_angle", "optics", "ddcet_physics"]
        )

