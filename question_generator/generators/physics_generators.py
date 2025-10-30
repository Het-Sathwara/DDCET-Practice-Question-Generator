class KinematicsGenerator(QuestionTemplate):
    """Generate kinematics questions - Linear Motion with enhanced scenarios"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Kinematics")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['velocity', 'acceleration', 'displacement', 'time', 'complex_motion'])
            
            if q_type == 'velocity':
                questions.append(self._generate_velocity_question(difficulty))
            elif q_type == 'acceleration':
                questions.append(self._generate_acceleration_question(difficulty))
            elif q_type == 'displacement':
                questions.append(self._generate_displacement_question(difficulty))
            elif q_type == 'time':
                questions.append(self._generate_time_question(difficulty))
            else:
                questions.append(self._generate_complex_motion_question(difficulty))
        
        return questions
    
    def _generate_velocity_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        u = random.uniform(0, mult["range"][1] / 10)
        a = random.uniform(1, mult["range"][1] / 20)
        t = random.uniform(1, mult["range"][1] / 10)
        
        u = round(u, mult["decimal"])
        a = round(a, mult["decimal"])
        t = round(t, mult["decimal"])
        
        v = u + a * t
        v = round(v, 2)
        
        scenarios = [
            f"A high-speed train leaves Ahmedabad station, accelerating uniformly from {u} m/s at {a} m/s². The conductor needs to know the train's velocity after {t} seconds of acceleration to adjust the schedule.",
            f"A cricket ball is thrown from the boundary line with an initial speed of {u} m/s. The fielder accelerates it uniformly at {a} m/s² while running towards the stumps. Calculate the ball's speed after {t} seconds.",
            f"A metro train departing from Gandhinagar station accelerates from {u} m/s at a constant rate of {a} m/s². Determine its velocity after traveling for {t} seconds to ensure proper signaling system operation."
        ]
        
        question_text = random.choice(scenarios)
        
        if random.random() < 0.6:
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
                solution=f"Using the first equation of motion: v = u + at = {u} + {a} × {t} = {v} m/s",
                tags=["kinematics", "velocity", "uniform_acceleration", "linear_motion"]
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
                tags=["kinematics", "velocity", "uniform_acceleration", "linear_motion"]
            )
    
    def _generate_complex_motion_question(self, difficulty: str) -> Question:
        """Generate multi-stage motion problems"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        # Stage 1: acceleration
        u1 = random.uniform(0, 5)
        a1 = random.uniform(2, 4)
        t1 = random.uniform(3, 8)
        
        # Stage 2: constant velocity
        t2 = random.uniform(5, 12)
        
        u1 = round(u1, 1)
        a1 = round(a1, 1)
        t1 = round(t1, 1)
        t2 = round(t2, 1)
        
        # Calculate velocities
        v1 = u1 + a1 * t1  # velocity after acceleration
        # Total distance = distance during acceleration + distance during constant velocity
        s1 = u1 * t1 + 0.5 * a1 * t1**2
        s2 = v1 * t2
        total_distance = s1 + s2
        total_distance = round(total_distance, 2)
        
        scenarios = [
            f"A bus departing from SG Highway starts from rest and accelerates at {a1} m/s² for {t1} seconds. It then continues at constant velocity for {t2} seconds. Calculate the total distance covered by the bus.",
            f"A particle starts with initial velocity {u1} m/s and accelerates at {a1} m/s² for {t1} seconds, then maintains constant speed for {t2} seconds. Find the total displacement of the particle.",
            f"An auto-rickshaw in Ahmedabad accelerates from {u1} m/s at {a1} m/s² for {t1} seconds, then cruises at constant speed for {t2} seconds. Determine the total distance traveled."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Solution involves two stages:
Stage 1 (Acceleration): 
Velocity after acceleration: v = u + at = {u1} + {a1} × {t1} = {v1:.1f} m/s
Distance during acceleration: s₁ = ut + ½at² = {u1}×{t1} + 0.5×{a1}×{t1}² = {s1:.1f} m

Stage 2 (Constant Velocity):
Distance during constant velocity: s₂ = vt = {v1:.1f} × {t2} = {s2:.1f} m

Total distance = s₁ + s₂ = {s1:.1f} + {s2:.1f} = {total_distance} m"""

        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in meters)",
            answer=total_distance,
            solution=solution,
            tags=["kinematics", "complex_motion", "multi_stage", "linear_motion"]
        )


class NewtonLawsGenerator(QuestionTemplate):
    """Generate questions on Newton's Laws of Motion with enhanced scenarios"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Newton's Laws")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['force', 'mass', 'momentum', 'impulse', 'connected_bodies'])
            
            if q_type == 'force':
                questions.append(self._generate_force_question(difficulty))
            elif q_type == 'mass':
                questions.append(self._generate_mass_question(difficulty))
            elif q_type == 'momentum':
                questions.append(self._generate_momentum_question(difficulty))
            elif q_type == 'impulse':
                questions.append(self._generate_impulse_question(difficulty))
            else:
                questions.append(self._generate_connected_bodies_question(difficulty))
        
        return questions
    
    def _generate_impulse_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(0.1, mult["range"][1] / 10)
        u = random.uniform(5, 15)
        v = random.uniform(-10, -1)  # Opposite direction for impulse
        
        m = round(m, 1)
        u = round(u, 1)
        v = round(v, 1)
        
        impulse = m * (v - u)
        impulse = round(impulse, 2)
        
        scenarios = [
            f"A cricket ball of mass {m} kg approaches a batsman at {u} m/s and is hit back in the opposite direction at {abs(v)} m/s. Calculate the impulse imparted to the ball by the bat.",
            f"A {m} kg football rolling towards a player at {u} m/s is kicked back with speed {abs(v)} m/s in the opposite direction. Determine the impulse delivered to the ball.",
            f"During a car safety test, a {m} kg dummy moving at {u} m/s hits the airbag and rebounds at {abs(v)} m/s. Find the impulse experienced by the dummy."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Impulse = Change in momentum = m(v - u)
= {m} × ({v} - {u}) 
= {m} × ({v - u}) 
= {impulse} N·s

The negative sign indicates the impulse is opposite to the initial direction of motion."""

        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in N·s, consider direction for sign)",
            answer=impulse,
            solution=solution,
            tags=["impulse", "momentum", "change_in_momentum", "force"]
        )
    
    def _generate_connected_bodies_question(self, difficulty: str) -> Question:
        """Generate problems with multiple connected bodies"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        m1 = random.uniform(2, 8)
        m2 = random.uniform(1, 5)
        F = random.uniform(20, 50)
        
        m1 = round(m1, 1)
        m2 = round(m2, 1)
        F = round(F, 1)
        
        total_m = m1 + m2
        a = F / total_m
        T = m1 * a  # Tension between bodies
        a = round(a, 2)
        T = round(T, 2)
        
        scenarios = [
            f"Two blocks of masses {m1} kg and {m2} kg are connected by a light string and pulled horizontally by a force of {F} N on a frictionless surface. Calculate the tension in the string connecting the blocks.",
            f"A system consists of two crates ({m1} kg and {m2} kg) tied together and pulled with {F} N force. Determine the tension in the rope between them, ignoring friction.",
            f"Two objects of mass {m1} kg and {m2} kg are connected and accelerated by {F} N force. Find the tension force between the two objects."
        ]
        
        question_text = random.choice(scenarios)
        
        q_type = random.choice(['tension', 'acceleration'])
        
        if q_type == 'tension':
            answer = T
            solution = f"""Step 1: Total mass = {m1} + {m2} = {total_m} kg
Step 2: Acceleration of system: a = F/m_total = {F}/{total_m} = {a} m/s²
Step 3: Tension on {m1} kg block: T = m₁ × a = {m1} × {a} = {T} N

The tension accelerates the {m1} kg block."""
        else:
            answer = a
            solution = f"""Total mass = {m1} + {m2} = {total_m} kg
Acceleration: a = F/m_total = {F}/{total_m} = {a} m/s²

Both blocks move with the same acceleration."""
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text,
            answer=answer,
            solution=solution,
            tags=["newton_laws", "connected_bodies", "tension", "system_acceleration"]
        )


class CircularMotionGenerator(QuestionTemplate):
    """Generate enhanced circular motion questions with real scenarios"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Circular Motion")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['centripetal_force', 'angular_velocity', 'centripetal_acceleration', 
                                  'banking_angle', 'angular_acceleration'])
            
            if q_type == 'centripetal_force':
                questions.append(self._generate_centripetal_force_question(difficulty))
            elif q_type == 'angular_velocity':
                questions.append(self._generate_angular_velocity_question(difficulty))
            elif q_type == 'centripetal_acceleration':
                questions.append(self._generate_centripetal_acceleration_question(difficulty))
            elif q_type == 'banking_angle':
                questions.append(self._generate_banking_angle_question(difficulty))
            else:
                questions.append(self._generate_angular_acceleration_question(difficulty))
        
        return questions
    
    def _generate_angular_velocity_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        # Using relationship: ω = 2πf = 2π/T [citation:8]
        f = random.uniform(0.1, 5)  # frequency in Hz
        r = random.uniform(1, 20)   # radius in meters
        
        f = round(f, 1)
        r = round(r, 1)
        
        omega = 2 * math.pi * f  # angular velocity
        v = omega * r  # linear velocity
        omega = round(omega, 2)
        v = round(v, 2)
        
        scenarios = [
            f"A Ferris wheel at Kankaria Carnival completes {f} revolutions per minute. If a passenger seat is {r} meters from the center, calculate the angular velocity of the wheel and the linear speed of the passenger.",
            f"A grinding wheel rotates at {f} revolutions per second. Determine the angular velocity and the linear speed at a point {r} cm from the center of rotation.",
            f"A bicycle wheel makes {f} complete turns every second. Calculate its angular velocity and the linear speed of a point on the rim located {r} meters from the axle."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Step 1: Convert frequency to angular velocity
ω = 2πf = 2 × π × {f} = {omega:.2f} rad/s

Step 2: Calculate linear speed
v = rω = {r} × {omega:.2f} = {v:.2f} m/s

The wheel rotates with angular velocity {omega:.2f} rad/s, giving a linear speed of {v:.2f} m/s at radius {r} m."""

        # For this question, we'll ask for angular velocity as the answer
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Provide angular velocity in rad/s)",
            answer=omega,
            solution=solution,
            tags=["circular_motion", "angular_velocity", "frequency", "rotation"]
        )
    
    def _generate_angular_acceleration_question(self, difficulty: str) -> Question:
        """Generate questions on angular acceleration"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        omega_i = random.uniform(0, 5)  # initial angular velocity
        omega_f = random.uniform(10, 20)  # final angular velocity  
        t = random.uniform(2, 8)  # time
        r = random.uniform(0.1, 1)  # radius
        
        omega_i = round(omega_i, 1)
        omega_f = round(omega_f, 1)
        t = round(t, 1)
        r = round(r, 2)
        
        alpha = (omega_f - omega_i) / t  # angular acceleration
        a_t = alpha * r  # tangential acceleration
        alpha = round(alpha, 2)
        a_t = round(a_t, 2)
        
        scenarios = [
            f"A centrifuge in a medical lab increases its rotation rate from {omega_i} rad/s to {omega_f} rad/s in {t} seconds. Calculate the angular acceleration and the tangential acceleration at a point {r} m from the axis.",
            f"A merry-go-round speeds up uniformly from {omega_i} rad/s to {omega_f} rad/s over {t} seconds. Determine its angular acceleration and the tangential acceleration experienced by a child sitting {r} m from the center.",
            f"A pottery wheel accelerates from {omega_i} rad/s to {omega_f} rad/s in {t} s. Find the angular acceleration and tangential acceleration at a point {r} m from the rotation axis."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Step 1: Angular acceleration
α = (ω_f - ω_i) / t = ({omega_f} - {omega_i}) / {t} = {alpha:.2f} rad/s²

Step 2: Tangential acceleration  
a_t = r × α = {r} × {alpha:.2f} = {a_t:.2f} m/s²

The angular acceleration is {alpha:.2f} rad/s², producing tangential acceleration of {a_t:.2f} m/s²."""
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical", 
            question_text=question_text + " (Provide angular acceleration in rad/s²)",
            answer=alpha,
            solution=solution,
            tags=["circular_motion", "angular_acceleration", "rotational_kinematics"]
        )
    
    def _generate_banking_angle_question(self, difficulty: str) -> Question:
        """Generate questions on banked curves"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        v = random.uniform(10, 30)  # speed in m/s
        r = random.uniform(20, 100)  # radius in meters
        g = 9.8  # gravity
        
        v = round(v, 1)
        r = round(r, 1)
        
        # θ = arctan(v² / (rg)) for ideal banking
        theta_rad = math.atan(v**2 / (r * g))
        theta_deg = math.degrees(theta_rad)
        theta_deg = round(theta_deg, 1)
        
        scenarios = [
            f"A race track designer needs to bank a curve of radius {r} m for cars traveling at {v} m/s. Calculate the ideal banking angle so no friction is needed to prevent skidding.",
            f"A highway curve with radius {r} m is designed for vehicles moving at {v} m/s. Determine the proper banking angle to eliminate side friction at this speed.",
            f"For a circular road of radius {r} m, find the banking angle required for vehicles to safely navigate the curve at {v} m/s without relying on friction."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""For ideal banking: tanθ = v² / (rg)
tanθ = ({v})² / ({r} × 9.8) = {v**2} / {r*9.8} = {v**2/(r*9.8):.3f}
θ = arctan({v**2/(r*9.8):.3f}) = {theta_deg}°

The curve should be banked at {theta_deg}° for optimal safety at {v} m/s."""

        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in degrees)",
            answer=theta_deg,
            solution=solution,
            tags=["circular_motion", "banking_angle", "centripetal_force", "design"]
        )


class WorkEnergyGenerator(QuestionTemplate):
    """Generate enhanced work, energy, and power questions"""
    
    def __init__(self):
        super().__init__("Physics", "Classical Mechanics", "Work and Energy")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['work', 'kinetic_energy', 'potential_energy', 'power', 
                                  'energy_conservation', 'work_energy_theorem'])
            
            if q_type == 'work':
                questions.append(self._generate_work_question(difficulty))
            elif q_type == 'kinetic_energy':
                questions.append(self._generate_ke_question(difficulty))
            elif q_type == 'potential_energy':
                questions.append(self._generate_pe_question(difficulty))
            elif q_type == 'power':
                questions.append(self._generate_power_question(difficulty))
            elif q_type == 'energy_conservation':
                questions.append(self._generate_energy_conservation_question(difficulty))
            else:
                questions.append(self._generate_work_energy_theorem_question(difficulty))
        
        return questions
    
    def _generate_power_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        # Enhanced power scenarios
        m = random.uniform(50, 100)  # mass in kg
        h = random.uniform(10, 30)   # height in m
        t = random.uniform(2, 10)    # time in s
        g = 9.8
        
        m = round(m, 1)
        h = round(h, 1)
        t = round(t, 1)
        
        work = m * g * h
        power = work / t
        work = round(work, 1)
        power = round(power, 1)
        
        scenarios = [
            f"A construction worker lifts {m} kg of building materials to a height of {h} meters in {t} seconds. Calculate the power developed by the worker.",
            f"During gym training, an athlete lifts a {m} kg weight through {h} meters in {t} seconds. Determine the average power output.",
            f"A crane lifts a {m} kg load vertically to {h} m height in {t} s. Find the power delivered by the crane's motor (ignore efficiency losses)."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Step 1: Work done against gravity
Work = mgh = {m} × 9.8 × {h} = {work} J

Step 2: Power developed  
Power = Work / time = {work} / {t} = {power} W

The average power output is {power} Watts."""

        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Watts)",
            answer=power,
            solution=solution,
            tags=["power", "work", "energy", "time"]
        )
    
    def _generate_energy_conservation_question(self, difficulty: str) -> Question:
        """Generate energy conservation problems"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        h = random.uniform(5, 20)  # height in meters
        g = 9.8
        
        h = round(h, 1)
        
        # Using conservation: mgh = 0.5mv² => v = √(2gh)
        v = math.sqrt(2 * g * h)
        v = round(v, 2)
        
        scenarios = [
            f"A student drops a physics textbook from a {h} meter high building. Using energy conservation principles, calculate the speed of the book just before it hits the ground.",
            f"A roller coaster car starts from rest at a height of {h} meters on the first hill. Neglecting friction, find its speed at the bottom of the hill using energy conservation.",
            f"A skier begins from rest at a height of {h} m on a frictionless slope. Determine the skier's speed at the bottom using energy considerations."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Using conservation of mechanical energy:
Initial PE = mgh, Initial KE = 0
Final PE = 0, Final KE = ½mv²

mgh = ½mv²
v = √(2gh) = √(2 × 9.8 × {h}) = √({2*9.8*h}) = {v} m/s

The final speed is {v} m/s."""

        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in m/s)",
            answer=v,
            solution=solution,
            tags=["energy_conservation", "potential_energy", "kinetic_energy", "mechanical_energy"]
        )
    
    def _generate_work_energy_theorem_question(self, difficulty: str) -> Question:
        """Generate work-energy theorem problems"""
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(1, 10)  # mass in kg
        u = random.uniform(0, 5)   # initial velocity
        F = random.uniform(10, 50) # force applied
        d = random.uniform(2, 10)  # distance
        
        m = round(m, 1)
        u = round(u, 1)
        F = round(F, 1)
        d = round(d, 1)
        
        # Work-energy theorem: Work = ΔKE = 0.5m(v² - u²)
        work = F * d
        ke_initial = 0.5 * m * u**2
        ke_final = ke_initial + work
        v = math.sqrt(2 * ke_final / m)
        v = round(v, 2)
        
        scenarios = [
            f"A {m} kg object initially moving at {u} m/s is pushed by a constant force of {F} N over a distance of {d} m. Using the work-energy theorem, find its final speed.",
            f"A constant force of {F} N acts on a {m} kg crate initially moving at {u} m/s. After the force acts over {d} m, what is the crate's final velocity?",
            f"Workers push a {m} kg box with {F} N force over {d} m. If the box started at {u} m/s, calculate its final speed using work-energy principles."
        ]
        
        question_text = random.choice(scenarios)
        
        solution = f"""Using Work-Energy Theorem: Work done = Change in Kinetic Energy

Step 1: Work done by force
Work = F × d = {F} × {d} = {F*d} J

Step 2: Initial kinetic energy
KE_initial = ½mu² = 0.5 × {m} × {u}² = {ke_initial:.1f} J

Step 3: Final kinetic energy  
KE_final = KE_initial + Work = {ke_initial:.1f} + {F*d} = {ke_final:.1f} J

Step 4: Final velocity
KE_final = ½mv² => v = √(2 × KE_final / m) = √(2 × {ke_final:.1f} / {m}) = {v} m/s

The final speed is {v} m/s."""

        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in m/s)",
            answer=v,
            solution=solution,
            tags=["work_energy_theorem", "kinetic_energy", "work", "energy"]
        )
        
# ==================== ELECTRICITY & MAGNETISM ====================

class OhmsLawGenerator(QuestionTemplate):
    """Generate comprehensive Ohm's Law and electric current questions for DDCET"""
    
    def __init__(self):
        super().__init__("Physics", "Electric Current", "Ohm's Law")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['current', 'voltage', 'resistance', 'power', 'series_circuit', 'parallel_circuit'])
            
            if q_type == 'current':
                questions.append(self._generate_current_question(difficulty))
            elif q_type == 'voltage':
                questions.append(self._generate_voltage_question(difficulty))
            elif q_type == 'resistance':
                questions.append(self._generate_resistance_question(difficulty))
            elif q_type == 'power':
                questions.append(self._generate_power_question(difficulty))
            elif q_type == 'series_circuit':
                questions.append(self._generate_series_circuit_question(difficulty))
            else:
                questions.append(self._generate_parallel_circuit_question(difficulty))
        
        return questions
    
    def _generate_current_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        V = random.uniform(1, mult["range"][1] * 2)
        R = random.uniform(1, mult["range"][1] * 1.5)
        
        V = round(V, mult["decimal"])
        R = round(R, mult["decimal"])
        
        # I = V / R
        I = V / R
        I = round(I, 3)
        
        circuit_elements = [
            "a copper conductor of uniform cross-section",
            "a tungsten filament in an incandescent bulb",
            "a nichrome wire heating element",
            "a carbon composition resistor",
            "an aluminum conductor used in power transmission"
        ]
        
        applications = [
            f"connected to a {V} V battery",
            f"across a {V} V DC power supply",
            f"with a potential difference of {V} V maintained across it",
            f"in a circuit with {V} V applied voltage"
        ]
        
        element = random.choice(circuit_elements)
        application = random.choice(applications)
        
        question_text = f"In an electrical circuit, {element} with resistance {R} Ω is {application}. Determine the current flowing through the conductor, considering Ohm's law holds true for this material."
        
        if random.random() < 0.6:
            distractors = self._generate_distractor_options(I, 3, percentage_range=15)
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
                solution=f"According to Ohm's Law: I = V/R = {V} / {R} = {I} A",
                tags=["ohms_law", "current", "electric_current", "ddcet_physics"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in Amperes with 3 decimal places)",
                answer=I,
                solution=f"Using Ohm's Law: I = V/R = {V} / {R} = {I} A",
                tags=["ohms_law", "current", "electric_current", "ddcet_physics"]
            )
    
    def _generate_voltage_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        I = random.uniform(0.05, mult["range"][1] / 20)
        R = random.uniform(10, mult["range"][1] * 2)
        
        I = round(I, mult["decimal"] + 2)
        R = round(R, mult["decimal"])
        
        # V = I × R
        V = I * R
        V = round(V, 2)
        
        scenarios = [
            f"A current of {I} A is measured through a precision resistor of {R} Ω in a laboratory experiment.",
            f"In a temperature-controlled environment, a constant current of {I} A flows through a {R} Ω standard resistor.",
            f"A digital multimeter shows {I} A current passing through a {R} Ω resistance in a calibration circuit.",
            f"For quality testing, a {I} A current is forced through a {R} Ω test resistor in the circuit."
        ]
        
        question_text = f"{random.choice(scenarios)} Calculate the voltage drop across the resistor using fundamental principles of electric circuits."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Volts)",
            answer=V,
            solution=f"Using Ohm's Law: V = I × R = {I} × {R} = {V} V",
            tags=["ohms_law", "voltage", "potential_difference", "ddcet_physics"]
        )
    
    def _generate_resistance_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        V = random.uniform(1, mult["range"][1] * 3)
        I = random.uniform(0.01, mult["range"][1] / 50)
        
        V = round(V, mult["decimal"])
        I = round(I, mult["decimal"] + 2)
        
        # R = V / I
        R = V / I
        R = round(R, 2)
        
        experimental_setups = [
            f"In a physics laboratory experiment, when {V} V is applied across an unknown resistor, the ammeter shows a reading of {I} A.",
            f"During circuit analysis, a voltage source of {V} V causes a current of {I} A to flow through a circuit component.",
            f"A student measures {V} V across a mystery component while the series ammeter indicates {I} A current flow.",
            f"In an electronic device testing, {V} V potential difference results in {I} A current through the device under test."
        ]
        
        question_text = f"{random.choice(experimental_setups)} Determine the resistance of the component, assuming it follows Ohm's law in its operating region."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Ohms)",
            answer=R,
            solution=f"Using Ohm's Law: R = V / I = {V} / {I} = {R} Ω",
            tags=["ohms_law", "resistance", "electrical_resistance", "ddcet_physics"]
        )
    
    def _generate_power_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        V = random.uniform(3, mult["range"][1] * 4)
        I = random.uniform(0.1, mult["range"][1] / 10)
        
        V = round(V, mult["decimal"])
        I = round(I, mult["decimal"] + 1)
        
        # P = V × I
        P = V * I
        P = round(P, 2)
        
        power_scenarios = [
            f"An electrical appliance operates at {V} V and draws {I} A from the mains supply.",
            f"A DC motor running at rated conditions has {V} V across its terminals and {I} A current through its windings.",
            f"In a power electronics circuit, a load requires {V} V and consumes {I} A from the source.",
            f"An industrial heater element operates with {V} V applied and {I} A current flow."
        ]
        
        question_text = f"{random.choice(power_scenarios)} Calculate the power consumed by the device and the energy dissipated as heat per second."
        
        if random.random() < 0.5:
            distractors = self._generate_distractor_options(P, 3, percentage_range=20)
            options = [f"{P} W"] + [f"{d} W" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{P} W",
                options=options,
                solution=f"Electrical Power P = V × I = {V} × {I} = {P} W",
                tags=["electrical_power", "power_dissipation", "joules_law", "ddcet_physics"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in Watts)",
                answer=P,
                solution=f"Electrical Power P = V × I = {V} × {I} = {P} W",
                tags=["electrical_power", "power_dissipation", "joules_law", "ddcet_physics"]
            )
    
    def _generate_series_circuit_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        R1 = random.uniform(10, mult["range"][1])
        R2 = random.uniform(15, mult["range"][1] * 1.2)
        R3 = random.uniform(20, mult["range"][1] * 1.5)
        V_total = random.uniform(12, mult["range"][1] * 3)
        
        R1 = round(R1, mult["decimal"])
        R2 = round(R2, mult["decimal"])
        R3 = round(R3, mult["decimal"])
        V_total = round(V_total, mult["decimal"])
        
        # Series resistance
        R_eq = R1 + R2 + R3
        I_total = V_total / R_eq
        V1 = I_total * R1
        V2 = I_total * R2
        V3 = I_total * R3
        
        R_eq = round(R_eq, 2)
        I_total = round(I_total, 3)
        V1 = round(V1, 2)
        V2 = round(V2, 2)
        V3 = round(V3, 2)
        
        circuit_configs = [
            f"Three resistors R₁ = {R1} Ω, R₂ = {R2} Ω, and R₃ = {R3} Ω are connected in series across a {V_total} V battery.",
            f"In a series circuit, resistors of values {R1} Ω, {R2} Ω, and {R3} Ω are connected to a {V_total} V DC power supply.",
            f"A voltage source of {V_total} V is connected to a series combination of {R1} Ω, {R2} Ω, and {R3} Ω resistors."
        ]
        
        questions = [
            "Calculate the equivalent resistance of the circuit and the current flowing through each resistor.",
            "Determine the total circuit current and the voltage drop across each resistor.",
            "Find the current in the circuit and the power dissipated by each resistor."
        ]
        
        question_text = f"{random.choice(circuit_configs)} {random.choice(questions)}"
        
        if "equivalent resistance" in question_text:
            answer = R_eq
            solution = f"Series equivalent resistance R_eq = R₁ + R₂ + R₃ = {R1} + {R2} + {R3} = {R_eq} Ω"
        elif "current" in question_text and "voltage" not in question_text:
            answer = I_total
            solution = f"Total current I = V/R_eq = {V_total}/{R_eq} = {I_total} A (same through all series resistors)"
        else:
            answer = I_total
            solution = f"Total current I = V/R_eq = {V_total}/{R_eq} = {I_total} A, Voltages: V₁ = I×R₁ = {I_total}×{R1} = {V1} V, V₂ = {I_total}×{R2} = {V2} V, V₃ = {I_total}×{R3} = {V3} V"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text,
            answer=answer,
            solution=solution,
            tags=["series_circuit", "equivalent_resistance", "voltage_divider", "ddcet_physics"]
        )
    
    def _generate_parallel_circuit_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        R1 = random.uniform(10, mult["range"][1])
        R2 = random.uniform(15, mult["range"][1] * 1.2)
        R3 = random.uniform(20, mult["range"][1] * 1.5)
        V_total = random.uniform(12, mult["range"][1] * 3)
        
        R1 = round(R1, mult["decimal"])
        R2 = round(R2, mult["decimal"])
        R3 = round(R3, mult["decimal"])
        V_total = round(V_total, mult["decimal"])
        
        # Parallel resistance
        R_eq = 1 / (1/R1 + 1/R2 + 1/R3)
        I_total = V_total / R_eq
        I1 = V_total / R1
        I2 = V_total / R2
        I3 = V_total / R3
        
        R_eq = round(R_eq, 2)
        I_total = round(I_total, 2)
        I1 = round(I1, 2)
        I2 = round(I2, 2)
        I3 = round(I3, 2)
        
        circuit_descriptions = [
            f"In a household electrical circuit, three appliances with resistances {R1} Ω, {R2} Ω, and {R3} Ω are connected in parallel to a {V_total} V supply.",
            f"Three resistors of values {R1} Ω, {R2} Ω, and {R3} Ω are connected in parallel across a {V_total} V battery in an electronics lab.",
            f"A parallel combination of {R1} Ω, {R2} Ω, and {R3} Ω resistors is connected to a {V_total} V DC power source."
        ]
        
        questions = [
            "Calculate the equivalent resistance of the parallel combination and the total current drawn from the source.",
            "Determine the current through each branch and verify Kirchhoff's current law at the junction.",
            "Find the total circuit resistance and the power supplied by the source to the parallel network."
        ]
        
        question_text = f"{random.choice(circuit_descriptions)} {random.choice(questions)}"
        
        if "equivalent resistance" in question_text:
            answer = R_eq
            solution = f"Parallel equivalent resistance: 1/R_eq = 1/{R1} + 1/{R2} + 1/{R3} = {1/R1:.4f} + {1/R2:.4f} + {1/R3:.4f} = {1/R_eq:.4f}, so R_eq = {R_eq} Ω"
        elif "current through each branch" in question_text:
            answer = I1
            solution = f"Branch currents: I₁ = V/R₁ = {V_total}/{R1} = {I1} A, I₂ = {V_total}/{R2} = {I2} A, I₃ = {V_total}/{R3} = {I3} A. Total I = I₁ + I₂ + I₃ = {I1} + {I2} + {I3} = {I_total} A"
        else:
            answer = I_total
            solution = f"Total current I = V/R_eq = {V_total}/{R_eq} = {I_total} A"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text,
            answer=answer,
            solution=solution,
            tags=["parallel_circuit", "equivalent_resistance", "current_division", "kirchhoff_law", "ddcet_physics"]
        )


class CapacitanceGenerator(QuestionTemplate):
    """Generate comprehensive capacitance questions for DDCET syllabus"""
    
    def __init__(self):
        super().__init__("Physics", "Electric Current", "Capacitance")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['charge', 'energy', 'series', 'parallel', 'time_constant', 'energy_density'])
            
            if q_type == 'charge':
                questions.append(self._generate_charge_question(difficulty))
            elif q_type == 'energy':
                questions.append(self._generate_energy_question(difficulty))
            elif q_type == 'series':
                questions.append(self._generate_series_question(difficulty))
            elif q_type == 'parallel':
                questions.append(self._generate_parallel_question(difficulty))
            elif q_type == 'time_constant':
                questions.append(self._generate_time_constant_question(difficulty))
            else:
                questions.append(self._generate_energy_density_question(difficulty))
        
        return questions
    
    def _generate_charge_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C = random.uniform(10, mult["range"][1] * 2)  # μF
        V = random.uniform(10, mult["range"][1] * 3)  # V
        
        C = round(C, mult["decimal"])
        V = round(V, mult["decimal"])
        
        # Q = C × V
        Q = C * V
        Q = round(Q, 2)
        
        capacitor_types = [
            "parallel plate capacitor with air dielectric",
            "electrolytic capacitor",
            "ceramic disk capacitor", 
            "mica capacitor",
            "tantalum capacitor"
        ]
        
        applications = [
            f"charged to {V} V in a power supply filter circuit",
            f"connected across a {V} V battery in a timing circuit",
            f"subjected to {V} V in a flash lamp circuit",
            f"charged with {V} V potential difference in an energy storage system"
        ]
        
        cap_type = random.choice(capacitor_types)
        application = random.choice(applications)
        
        question_text = f"A {C} μF {cap_type} is {application}. Calculate the amount of electric charge stored on each plate of the capacitor."
        
        if random.random() < 0.5:
            distractors = self._generate_distractor_options(Q, 3, percentage_range=15)
            options = [f"{Q} μC"] + [f"{d} μC" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{Q} μC",
                options=options,
                solution=f"Charge stored Q = C × V = {C} μF × {V} V = {Q} μC",
                tags=["capacitance", "charge_storage", "capacitor", "ddcet_physics"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in microcoulombs)",
                answer=Q,
                solution=f"Charge stored Q = C × V = {C} μF × {V} V = {Q} μC",
                tags=["capacitance", "charge_storage", "capacitor", "ddcet_physics"]
            )
    
    def _generate_energy_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C = random.uniform(100, mult["range"][1] * 5)  # μF
        V = random.uniform(25, mult["range"][1] * 4)   # V
        
        C = round(C, mult["decimal"])
        V = round(V, mult["decimal"])
        
        # U = 0.5 × C × V²
        U = 0.5 * C * V**2
        U = round(U, 2)
        
        energy_contexts = [
            f"A {C} μF capacitor used in a camera flash circuit is charged to {V} V.",
            f"In a defibrillator machine, a {C} μF capacitor is charged to {V} V for delivering a shock.",
            f"A {C} μF energy storage capacitor in a power electronics application is charged to {V} V.",
            f"For pulse power applications, a {C} μF capacitor bank is charged to {V} V."
        ]
        
        question_text = f"{random.choice(energy_contexts)} Calculate the total energy stored in the capacitor that can be released during discharge."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in microjoules)",
            answer=U,
            solution=f"Energy stored U = ½CV² = 0.5 × {C} × {V}² = {U} μJ",
            tags=["capacitance", "energy_storage", "capacitor_energy", "ddcet_physics"]
        )
    
    def _generate_series_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C1 = random.uniform(10, mult["range"][1])
        C2 = random.uniform(15, mult["range"][1] * 1.5)
        C3 = random.uniform(20, mult["range"][1] * 2)
        
        C1 = round(C1, mult["decimal"])
        C2 = round(C2, mult["decimal"])
        C3 = round(C3, mult["decimal"])
        
        # 1/C_eq = 1/C1 + 1/C2 + 1/C3
        C_eq = 1 / (1/C1 + 1/C2 + 1/C3)
        C_eq = round(C_eq, 3)
        
        circuit_scenarios = [
            f"In a high voltage application, three capacitors of {C1} μF, {C2} μF, and {C3} μF are connected in series to increase the voltage rating.",
            f"For impedance matching in an RF circuit, capacitors of values {C1} μF, {C2} μF, and {C3} μF are connected in series.",
            f"In a power factor correction circuit, {C1} μF, {C2} μF, and {C3} μF capacitors are connected in series combination."
        ]
        
        question_text = f"{random.choice(circuit_scenarios)} Calculate the equivalent capacitance of this series combination and explain why the equivalent capacitance is less than any individual capacitor in the series."
        
        if random.random() < 0.5:
            distractors = self._generate_distractor_options(C_eq, 3, percentage_range=12)
            options = [f"{C_eq} μF"] + [f"{d} μF" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{C_eq} μF",
                options=options,
                solution=f"Series combination: 1/C_eq = 1/{C1} + 1/{C2} + 1/{C3} = {1/C1:.4f} + {1/C2:.4f} + {1/C3:.4f} = {1/C_eq:.4f}, so C_eq = {C_eq} μF",
                tags=["capacitance", "series_combination", "equivalent_capacitance", "ddcet_physics"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in microfarads with 3 decimal places)",
                answer=C_eq,
                solution=f"Series combination: 1/C_eq = 1/{C1} + 1/{C2} + 1/{C3} = {1/C1:.4f} + {1/C2:.4f} + {1/C3:.4f} = {1/C_eq:.4f}, so C_eq = {C_eq} μF",
                tags=["capacitance", "series_combination", "equivalent_capacitance", "ddcet_physics"]
            )
    
    def _generate_parallel_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C1 = random.uniform(10, mult["range"][1])
        C2 = random.uniform(15, mult["range"][1] * 1.5)
        C3 = random.uniform(20, mult["range"][1] * 2)
        
        C1 = round(C1, mult["decimal"])
        C2 = round(C2, mult["decimal"])
        C3 = round(C3, mult["decimal"])
        
        # C_eq = C1 + C2 + C3
        C_eq = C1 + C2 + C3
        C_eq = round(C_eq, 2)
        
        application_contexts = [
            f"In a power supply filter circuit, capacitors of {C1} μF, {C2} μF, and {C3} μF are connected in parallel to increase the total capacitance.",
            f"For energy storage in a pulse forming network, {C1} μF, {C2} μF, and {C3} μF capacitors are connected in parallel.",
            f"In an audio amplifier circuit, decoupling capacitors of values {C1} μF, {C2} μF, and {C3} μF are connected in parallel combination."
        ]
        
        question_text = f"{random.choice(application_contexts)} Determine the equivalent capacitance of this parallel arrangement and calculate the total charge storage capacity when connected to a 50V source."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in microfarads for capacitance)",
            answer=C_eq,
            solution=f"Parallel combination: C_eq = C₁ + C₂ + C₃ = {C1} + {C2} + {C3} = {C_eq} μF. Total charge at 50V = C_eq × 50 = {C_eq} × 50 = {C_eq * 50} μC",
            tags=["capacitance", "parallel_combination", "equivalent_capacitance", "ddcet_physics"]
        )
    
    def _generate_time_constant_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        R = random.uniform(1, mult["range"][1] * 2)  # kΩ
        C = random.uniform(10, mult["range"][1] * 3)  # μF
        
        R = round(R, mult["decimal"])
        C = round(C, mult["decimal"])
        
        # τ = R × C (converting units: kΩ × μF = ms)
        tau = R * C  # in milliseconds
        tau = round(tau, 2)
        
        rc_circuits = [
            f"In an RC timing circuit, a resistor of {R} kΩ is connected in series with a capacitor of {C} μF.",
            f"A simple low-pass filter uses a {R} kΩ resistor and {C} μF capacitor in series.",
            f"For generating time delays, an RC circuit is constructed with {R} kΩ resistance and {C} μF capacitance."
        ]
        
        question_text = f"{random.choice(rc_circuits)} Calculate the time constant of this RC circuit, which represents the time required for the capacitor to charge to approximately 63.2% of the supply voltage or discharge to 36.8% of its initial voltage."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in milliseconds)",
            answer=tau,
            solution=f"Time constant τ = R × C = {R} kΩ × {C} μF = {tau} ms",
            tags=["rc_circuit", "time_constant", "capacitor_charging", "ddcet_physics"]
        )
    
    def _generate_energy_density_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        C = random.uniform(1000, mult["range"][1] * 10)  # μF
        V = random.uniform(50, mult["range"][1] * 5)     # V
        volume = random.uniform(0.1, mult["range"][1] / 10)  # cm³
        
        C = round(C, mult["decimal"])
        V = round(V, mult["decimal"])
        volume = round(volume, mult["decimal"] + 1)
        
        # Energy in joules: U = 0.5 × C × V² (convert μF to F: ×10⁻⁶)
        U_joules = 0.5 * (C * 1e-6) * V**2
        # Energy density in J/cm³
        energy_density = U_joules / volume
        energy_density = round(energy_density * 1e3, 4)  # Convert to mJ/cm³ for better readability
        
        question_text = f"A compact capacitor of {C} μF is rated for {V} V and has a volume of {volume} cm³. Calculate the energy density of this capacitor, which is an important parameter for energy storage applications like electric vehicles and renewable energy systems."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in millijoules per cubic centimeter)",
            answer=energy_density,
            solution=f"Energy U = ½CV² = 0.5 × {C}×10⁻⁶ × {V}² = {U_joules:.6f} J. Energy density = U/volume = {U_joules:.6f}/{volume} = {energy_density} mJ/cm³",
            tags=["capacitance", "energy_density", "energy_storage", "advanced_capacitance", "ddcet_physics"]
        )


# ==================== HEAT & THERMODYNAMICS ====================

class HeatTransferGenerator(QuestionTemplate):
    """Generate comprehensive heat and thermometry questions for DDCET"""
    
    def __init__(self):
        super().__init__("Physics", "Heat and Thermometry", "Heat Transfer")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['heat_capacity', 'specific_heat', 'temperature_conversion', 'thermal_expansion', 'heat_transfer', 'calorimetry'])
            
            if q_type == 'heat_capacity':
                questions.append(self._generate_heat_capacity_question(difficulty))
            elif q_type == 'specific_heat':
                questions.append(self._generate_specific_heat_question(difficulty))
            elif q_type == 'temperature_conversion':
                questions.append(self._generate_temp_conversion_question(difficulty))
            elif q_type == 'thermal_expansion':
                questions.append(self._generate_thermal_expansion_question(difficulty))
            elif q_type == 'heat_transfer':
                questions.append(self._generate_heat_transfer_rate_question(difficulty))
            else:
                questions.append(self._generate_calorimetry_question(difficulty))
        
        return questions
    
    def _generate_heat_capacity_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m = random.uniform(0.5, mult["range"][1] / 20)
        c = random.uniform(200, mult["range"][1] * 15)
        dT = random.uniform(15, mult["range"][1] / 3)
        
        m = round(m, mult["decimal"] + 1)
        c = round(c, 0)
        dT = round(dT, mult["decimal"])
        
        # Q = mcΔT
        Q = m * c * dT
        Q = round(Q, 2)
        
        materials = [
            f"a {m} kg block of aluminum",
            f"a {m} kg copper vessel",
            f"a {m} kg iron component",
            f"a {m} kg sample of glass"
        ]
        
        processes = [
            f"from an initial temperature to a final temperature that is {dT}°C higher",
            f"through a temperature rise of {dT} K during a manufacturing process",
            f"to increase its temperature by {dT}°C in a heating application",
            f"undergoing a {dT} K temperature change in a thermal treatment"
        ]
        
        material = random.choice(materials)
        process = random.choice(processes)
        
        question_text = f"In an industrial heating process, {material} with specific heat capacity {c} J/kg·K is heated {process}. Calculate the amount of heat energy required for this temperature change, neglecting any heat losses to the surroundings."
        
        if random.random() < 0.5:
            distractors = self._generate_distractor_options(Q, 3, percentage_range=15)
            options = [f"{Q} J"] + [f"{d} J" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{Q} J",
                options=options,
                solution=f"Q = m × c × ΔT = {m} × {c} × {dT} = {Q} J",
                tags=["heat_capacity", "specific_heat", "heat_transfer", "ddcet_physics"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in Joules)",
                answer=Q,
                solution=f"Q = m × c × ΔT = {m} × {c} × {dT} = {Q} J",
                tags=["heat_capacity", "specific_heat", "heat_transfer", "ddcet_physics"]
            )
    
    def _generate_specific_heat_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        Q = random.uniform(500, mult["range"][1] * 20)
        m = random.uniform(0.2, mult["range"][1] / 50)
        dT = random.uniform(12, mult["range"][1] / 8)
        
        Q = round(Q, mult["decimal"])
        m = round(m, mult["decimal"] + 1)
        dT = round(dT, mult["decimal"])
        
        # c = Q / (m × ΔT)
        c = Q / (m * dT)
        c = round(c, 2)
        
        experimental_contexts = [
            f"In a laboratory experiment to determine specific heat capacity, {Q} J of heat energy is supplied to a {m} kg metal sample, resulting in a temperature increase of {dT}°C.",
            f"During material testing, {Q} J of thermal energy is transferred to a {m} kg test specimen, causing a {dT} K rise in temperature.",
            f"A calorimetry experiment shows that {Q} J of heat raises the temperature of a {m} kg unknown substance by {dT}°C."
        ]
        
        question_text = f"{random.choice(experimental_contexts)} Calculate the specific heat capacity of the material and identify what common material it might be based on typical specific heat values."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in J/kg·K)",
            answer=c,
            solution=f"Specific heat c = Q / (m × ΔT) = {Q} / ({m} × {dT}) = {c} J/kg·K",
            tags=["specific_heat", "calorimetry", "material_properties", "ddcet_physics"]
        )
    
    def _generate_temp_conversion_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        conversion_type = random.choice(['C_to_F', 'F_to_C', 'C_to_K', 'K_to_C', 'F_to_K', 'K_to_F'])
        
        if conversion_type == 'C_to_F':
            C = random.uniform(-40, mult["range"][1])
            C = round(C, mult["decimal"])
            F = (9/5) * C + 32
            F = round(F, 2)
            
            context = f"In a weather station recording, the temperature is measured as {C}°C."
            question_text = f"{context} Convert this temperature to Fahrenheit scale for an international weather report."
            solution = f"F = (9/5)C + 32 = (9/5) × {C} + 32 = {F}°F"
            answer = F
            unit = "°F"
        
        elif conversion_type == 'F_to_C':
            F = random.uniform(-40, mult["range"][1] * 2)
            F = round(F, mult["decimal"])
            C = (5/9) * (F - 32)
            C = round(C, 2)
            
            context = f"A medical thermometer shows a patient's body temperature as {F}°F."
            question_text = f"{context} Convert this reading to Celsius scale for clinical records."
            solution = f"C = (5/9)(F - 32) = (5/9) × ({F} - 32) = {C}°C"
            answer = C
            unit = "°C"
        
        elif conversion_type == 'C_to_K':
            C = random.uniform(-273, mult["range"][1])
            C = round(C, mult["decimal"])
            K = C + 273.15
            K = round(K, 2)
            
            context = f"In a chemical reaction, the process temperature is maintained at {C}°C."
            question_text = f"{context} Express this temperature in Kelvin for thermodynamic calculations."
            solution = f"K = C + 273.15 = {C} + 273.15 = {K} K"
            answer = K
            unit = "K"
        
        elif conversion_type == 'K_to_C':
            K = random.uniform(200, mult["range"][1] + 273)
            K = round(K, mult["decimal"])
            C = K - 273.15
            C = round(C, 2)
            
            context = f"A scientific instrument records temperature as {K} K during an experiment."
            question_text = f"{context} Convert this measurement to Celsius scale for reporting."
            solution = f"C = K - 273.15 = {K} - 273.15 = {C}°C"
            answer = C
            unit = "°C"
        
        elif conversion_type == 'F_to_K':
            F = random.uniform(-40, mult["range"][1] * 2)
            F = round(F, mult["decimal"])
            K = (5/9) * (F - 32) + 273.15
            K = round(K, 2)
            
            context = f"In an American engineering document, temperature is specified as {F}°F."
            question_text = f"{context} Convert this value to Kelvin for international scientific communication."
            solution = f"First convert to Celsius: C = (5/9)({F} - 32) = {(5/9)*(F-32):.2f}°C, then to Kelvin: K = C + 273.15 = {K} K"
            answer = K
            unit = "K"
        
        else:  # K_to_F
            K = random.uniform(250, mult["range"][1] + 273)
            K = round(K, mult["decimal"])
            F = (9/5) * (K - 273.15) + 32
            F = round(F, 2)
            
            context = f"A physics experiment requires temperature of {K} K."
            question_text = f"{context} Express this temperature in Fahrenheit for equipment calibration in US customary units."
            solution = f"First convert to Celsius: C = {K} - 273.15 = {K-273.15:.2f}°C, then to Fahrenheit: F = (9/5)C + 32 = {F}°F"
            answer = F
            unit = "°F"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text,
            answer=answer,
            solution=solution,
            tags=["temperature", "conversion", "thermometry", "temperature_scales", "ddcet_physics"]
        )
    
    def _generate_thermal_expansion_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        L0 = random.uniform(1, mult["range"][1] / 2)
        alpha = random.choice([1.2e-5, 1.7e-5, 2.3e-5, 1.1e-5])  # Common expansion coefficients
        dT = random.uniform(20, mult["range"][1])
        
        L0 = round(L0, mult["decimal"])
        dT = round(dT, mult["decimal"])
        
        # ΔL = L0 × α × ΔT
        dL = L0 * alpha * dT
        dL = round(dL * 1000, 3)  # Convert to mm
        
        materials = {
            1.2e-5: "iron",
            1.7e-5: "brass", 
            2.3e-5: "aluminum",
            1.1e-5: "steel"
        }
        
        material = materials[alpha]
        scenarios = [
            f"A {L0} m long {material} rod is subjected to a temperature increase of {dT}°C.",
            f"In a bridge construction, a {L0} m {material} beam experiences a temperature rise of {dT} K.",
            f"A {material} pipeline of length {L0} m is heated from ambient temperature, increasing by {dT}°C."
        ]
        
        question_text = f"{random.choice(scenarios)} Calculate the linear expansion of the material, considering the thermal expansion coefficient of {material} is {alpha:.1e} per °C. This expansion must be accounted for in engineering designs to prevent structural stress."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in millimeters)",
            answer=dL,
            solution=f"Linear expansion ΔL = L₀ × α × ΔT = {L0} × {alpha:.1e} × {dT} = {dL/1000:.6f} m = {dL} mm",
            tags=["thermal_expansion", "linear_expansion", "thermometry", "ddcet_physics"]
        )
    
    def _generate_heat_transfer_rate_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        k = random.uniform(0.02, mult["range"][1] / 50)  # Thermal conductivity W/m·K
        A = random.uniform(0.5, mult["range"][1] / 20)   # Area in m²
        dT = random.uniform(10, mult["range"][1] / 5)    # Temperature difference
        thickness = random.uniform(0.01, mult["range"][1] / 100)  # Thickness in meters
        
        k = round(k, mult["decimal"] + 2)
        A = round(A, mult["decimal"] + 1)
        dT = round(dT, mult["decimal"])
        thickness = round(thickness, mult["decimal"] + 2)
        
        # Q/t = k × A × ΔT / d
        Q_rate = k * A * dT / thickness
        Q_rate = round(Q_rate, 2)
        
        materials = [
            "a brick wall", "a glass window", "a metal plate", "an insulating panel"
        ]
        
        applications = [
            f"with thermal conductivity {k} W/m·K",
            f"having heat transfer coefficient {k} W/m·K",
            f"with thermal conduction property of {k} W/m·K"
        ]
        
        material = random.choice(materials)
        application = random.choice(applications)
        
        question_text = f"In building heat loss calculations, {material} of area {A} m² and thickness {thickness} m {application} separates two environments with {dT}°C temperature difference. Calculate the rate of heat transfer through this material by conduction."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Watts)",
            answer=Q_rate,
            solution=f"Heat transfer rate Q/t = k × A × ΔT / d = {k} × {A} × {dT} / {thickness} = {Q_rate} W",
            tags=["heat_transfer", "conduction", "thermal_conductivity", "ddcet_physics"]
        )
    
    def _generate_calorimetry_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        m1 = random.uniform(0.1, mult["range"][1] / 100)
        c1 = random.uniform(390, 900)  # J/kg·K for common materials
        T1 = random.uniform(80, mult["range"][1] * 1.5)
        
        m2 = random.uniform(0.15, mult["range"][1] / 80)
        c2 = 4186  # Water specific heat
        T2 = random.uniform(15, mult["range"][1] / 6)
        
        m1 = round(m1, mult["decimal"] + 2)
        c1 = round(c1, 0)
        T1 = round(T1, mult["decimal"])
        m2 = round(m2, mult["decimal"] + 2)
        T2 = round(T2, mult["decimal"])
        
        # Heat lost by hot object = Heat gained by cold object
        # m1*c1*(T1 - Tf) = m2*c2*(Tf - T2)
        Tf = (m1 * c1 * T1 + m2 * c2 * T2) / (m1 * c1 + m2 * c2)
        Tf = round(Tf, 2)
        
        hot_objects = [
            f"a {m1} kg metal piece (specific heat {c1} J/kg·K) heated to {T1}°C",
            f"a {m1} kg ceramic sample (specific heat {c1} J/kg·K) at {T1}°C",
            f"a {m1} kg material (specific heat {c1} J/kg·K) with initial temperature {T1}°C"
        ]
        
        question_text = f"In a calorimetry experiment, {random.choice(hot_objects)} is dropped into {m2} kg of water at {T2}°C. Assuming no heat loss to the surroundings, calculate the final equilibrium temperature of the mixture."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in °C)",
            answer=Tf,
            solution=f"Using principle of calorimetry: m₁c₁(T₁ - T_f) = m₂c₂(T_f - T₂). Solving: T_f = (m₁c₁T₁ + m₂c₂T₂)/(m₁c₁ + m₂c₂) = ({m1}×{c1}×{T1} + {m2}×4186×{T2})/({m1}×{c1} + {m2}×4186) = {Tf}°C",
            tags=["calorimetry", "heat_transfer", "thermal_equilibrium", "ddcet_physics"]
        )


# ==================== WAVES & OPTICS ====================

class WaveMotionGenerator(QuestionTemplate):
    """Generate comprehensive wave motion questions for DDCET"""
    
    def __init__(self):
        super().__init__("Physics", "Wave Motion and Optics", "Waves")
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        questions = []
        
        for _ in range(count):
            q_type = random.choice(['frequency', 'wavelength', 'speed', 'period', 'wave_equation', 'doppler_effect', 'standing_waves'])
            
            if q_type == 'frequency':
                questions.append(self._generate_frequency_question(difficulty))
            elif q_type == 'wavelength':
                questions.append(self._generate_wavelength_question(difficulty))
            elif q_type == 'speed':
                questions.append(self._generate_speed_question(difficulty))
            elif q_type == 'period':
                questions.append(self._generate_period_question(difficulty))
            elif q_type == 'wave_equation':
                questions.append(self._generate_wave_equation_question(difficulty))
            elif q_type == 'doppler_effect':
                questions.append(self._generate_doppler_effect_question(difficulty))
            else:
                questions.append(self._generate_standing_waves_question(difficulty))
        
        return questions
    
    def _generate_frequency_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        T = random.uniform(0.002, mult["range"][1] / 500)
        T = round(T, mult["decimal"] + 3)
        
        # f = 1 / T
        f = 1 / T
        f = round(f, 1)
        
        wave_types = [
            "sound wave produced by a musical instrument",
            "electromagnetic wave from a radio transmitter",
            "mechanical wave on a stretched string",
            "ultrasonic wave used in medical imaging",
            "vibration in a mechanical system"
        ]
        
        contexts = [
            f"has a periodic time of {T} seconds",
            f"completes one cycle in {T} s",
            f"shows a repetition period of {T} s in oscilloscope measurements",
            f"has a time period of {T} s between successive crests"
        ]
        
        wave_type = random.choice(wave_types)
        context = random.choice(contexts)
        
        question_text = f"A {wave_type} {context}. Determine the frequency of this wave motion, which represents the number of complete oscillations per second."
        
        if random.random() < 0.5:
            distractors = self._generate_distractor_options(f, 3, percentage_range=10)
            options = [f"{f} Hz"] + [f"{d} Hz" for d in distractors]
            random.shuffle(options)
            
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="mcq",
                question_text=question_text,
                answer=f"{f} Hz",
                options=options,
                solution=f"Frequency f = 1/T = 1/{T} = {f} Hz",
                tags=["waves", "frequency", "wave_parameters", "ddcet_physics"]
            )
        else:
            return Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type="numerical",
                question_text=question_text + " (Answer in Hertz)",
                answer=f,
                solution=f"Frequency f = 1/T = 1/{T} = {f} Hz",
                tags=["waves", "frequency", "wave_parameters", "ddcet_physics"]
            )
    
    def _generate_wavelength_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        v = random.uniform(200, mult["range"][1] * 20)
        f = random.uniform(50, mult["range"][1] * 2)
        
        v = round(v, mult["decimal"])
        f = round(f, mult["decimal"])
        
        # λ = v / f
        wavelength = v / f
        wavelength = round(wavelength, 3)
        
        wave_scenarios = [
            f"In air, a sound wave travels at {v} m/s with frequency {f} Hz.",
            f"An electromagnetic wave propagates at {v} m/s in a medium with frequency {f} Hz.",
            f"A mechanical wave moves through a material at {v} m/s with oscillation frequency {f} Hz.",
            f"A water wave advances at {v} m/s while vibrating at {f} Hz frequency."
        ]
        
        question_text = f"{random.choice(wave_scenarios)} Calculate the wavelength of this wave, which is the spatial period of the wave—the distance over which the wave's shape repeats."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in meters)",
            answer=wavelength,
            solution=f"Wavelength λ = v/f = {v}/{f} = {wavelength} m",
            tags=["waves", "wavelength", "wave_parameters", "ddcet_physics"]
        )
    
    def _generate_speed_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        f = random.uniform(100, mult["range"][1] * 3)
        wavelength = random.uniform(0.5, mult["range"][1] / 20)
        
        f = round(f, mult["decimal"])
        wavelength = round(wavelength, mult["decimal"])
        
        # v = f × λ
        v = f * wavelength
        v = round(v, 2)
        
        measurement_contexts = [
            f"Laboratory measurements show a wave with frequency {f} Hz and wavelength {wavelength} m.",
            f"In wave characterization, a frequency of {f} Hz and wavelength of {wavelength} m are observed.",
            f"Analysis of a periodic wave reveals it oscillates at {f} Hz with consecutive peaks separated by {wavelength} m."
        ]
        
        question_text = f"{random.choice(measurement_contexts)} Using the fundamental wave equation, calculate the propagation speed of this wave through the medium."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in meters per second)",
            answer=v,
            solution=f"Wave speed v = f × λ = {f} × {wavelength} = {v} m/s",
            tags=["waves", "wave_speed", "wave_equation", "ddcet_physics"]
        )
    
    def _generate_period_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        f = random.uniform(20, mult["range"][1] * 2)
        f = round(f, mult["decimal"])
        
        # T = 1 / f
        T = 1 / f
        T = round(T, 4)
        
        oscillation_contexts = [
            f"A pendulum oscillates with frequency {f} Hz.",
            f"A mass-spring system vibrates at {f} Hz natural frequency.",
            f"An AC circuit oscillates at {f} Hz.",
            f"A guitar string vibrates with fundamental frequency {f} Hz."
        ]
        
        question_text = f"{random.choice(oscillation_contexts)} Determine the time period of this oscillation, which is the time taken for one complete cycle of motion."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in seconds)",
            answer=T,
            solution=f"Time period T = 1/f = 1/{f} = {T} s",
            tags=["waves", "period", "oscillation", "ddcet_physics"]
        )
    
    def _generate_wave_equation_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        A = random.uniform(0.1, mult["range"][1] / 10)
        k = random.uniform(1, mult["range"][1] / 5)
        omega = random.uniform(10, mult["range"][1] * 2)
        
        A = round(A, mult["decimal"] + 1)
        k = round(k, mult["decimal"])
        omega = round(omega, mult["decimal"])
        
        # Wave equation: y = A sin(kx - ωt)
        # Wave speed v = ω/k
        
        v = omega / k
        v = round(v, 2)
        
        question_text = f"A progressive wave is described by the equation y = {A} sin({k}x - {omega}t), where all quantities are in SI units. Calculate the wave speed and explain the physical significance of the parameters in this wave equation."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer for wave speed in m/s)",
            answer=v,
            solution=f"Comparing with standard wave equation y = A sin(kx - ωt), wave speed v = ω/k = {omega}/{k} = {v} m/s. Here, A = {A} m is amplitude, k = {k} rad/m is wave number, ω = {omega} rad/s is angular frequency.",
            tags=["wave_equation", "progressive_waves", "wave_parameters", "advanced_waves", "ddcet_physics"]
        )
    
    def _generate_doppler_effect_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        f0 = random.uniform(400, mult["range"][1] * 5)
        vs = random.uniform(10, mult["range"][1] / 2)
        v = 340  # Speed of sound in air
        
        f0 = round(f0, mult["decimal"])
        vs = round(vs, mult["decimal"])
        
        # Source moving toward stationary observer: f = f0 * v / (v - vs)
        f_observed = f0 * v / (v - vs)
        f_observed = round(f_observed, 1)
        
        scenarios = [
            f"A police car siren emits sound at frequency {f0} Hz while moving toward a stationary observer at {vs} m/s.",
            f"An ambulance with a siren frequency of {f0} Hz approaches a stationary person at speed {vs} m/s.",
            f"A train blowing its horn at {f0} Hz moves toward a stationary listener at {vs} m/s."
        ]
        
        question_text = f"{random.choice(scenarios)} Assuming speed of sound in air is 340 m/s, calculate the frequency observed by the stationary person due to the Doppler effect. This phenomenon is crucial in applications like radar, medical ultrasound, and astronomy."
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + " (Answer in Hertz)",
            answer=f_observed,
            solution=f"For source moving toward stationary observer: f_observed = f₀ × v / (v - v_s) = {f0} × 340 / (340 - {vs}) = {f_observed} Hz",
            tags=["doppler_effect", "sound_waves", "frequency_shift", "ddcet_physics"]
        )
    
    def _generate_standing_waves_question(self, difficulty: str) -> Question:
        mult = self._get_difficulty_multiplier(difficulty)
        
        L = random.uniform(0.5, mult["range"][1] / 4)
        n = random.randint(2, 5)  # Harmonic number
        v = random.uniform(100, mult["range"][1] * 10)
        
        L = round(L, mult["decimal"] + 1)
        v = round(v, mult["decimal"])
        
        # For standing waves on string fixed at both ends: λ = 2L/n
        # f = v/λ = nv/(2L)
        
        wavelength = 2 * L / n
        f = n * v / (2 * L)
        wavelength = round(wavelength, 3)
        f = round(f, 1)
        
        instruments = [
            f"A guitar string of length {L} m",
            f"A violin string {L} m long",
            f"A piano wire of length {L} m",
            f"A stretched string {L} m in length"
        ]
        
        question_text = f"{random.choice(instruments)} under tension supports standing waves. If the wave speed on the string is {v} m/s, calculate the wavelength and frequency of the {n}{'th' if n>3 else ['nd','rd','th'][n-2] if n>1 else 'st'} harmonic of vibration. Standing waves are fundamental to musical instruments and resonance phenomena."
        
        if random.random() < 0.5:
            answer = wavelength
            solution = f"Wavelength for {n}{'th' if n>3 else ['nd','rd','th'][n-2] if n>1 else 'st'} harmonic: λ = 2L/n = 2×{L}/{n} = {wavelength} m. Frequency f = v/λ = {v}/{wavelength} = {f} Hz"
            answer_type = "wavelength in meters"
        else:
            answer = f
            solution = f"Frequency for {n}{'th' if n>3 else ['nd','rd','th'][n-2] if n>1 else 'st'} harmonic: f = nv/(2L) = {n}×{v}/(2×{L}) = {f} Hz. Wavelength λ = 2L/n = 2×{L}/{n} = {wavelength} m"
            answer_type = "frequency in Hertz"
        
        return Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="numerical",
            question_text=question_text + f" (Answer for {answer_type})",
            answer=answer,
            solution=solution,
            tags=["standing_waves", "harmonics", "resonance", "wave_superposition", "ddcet_physics"]
        )