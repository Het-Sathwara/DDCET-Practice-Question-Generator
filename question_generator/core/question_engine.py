"""
Core Question Generation Engine
Provides base classes and utilities for dynamic question generation
"""

import random
import string
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
import sympy as sp
from sympy import symbols, solve, diff, integrate, simplify, expand, factor


class Question:
    """Represents a single question with all metadata"""
    
    def __init__(self, 
                 subject: str,
                 chapter: str,
                 subtopic: str,
                 difficulty: str,
                 question_type: str,
                 question_text: str,
                 answer: Any,
                 options: Optional[List[str]] = None,
                 solution: Optional[str] = None,
                 tags: Optional[List[str]] = None):
        self.subject = subject
        self.chapter = chapter
        self.subtopic = subtopic
        self.difficulty = difficulty  # easy, medium, hard, extreme
        self.question_type = question_type  # mcq, numerical, integer, conceptual
        self.question_text = question_text
        self.answer = answer
        self.options = options or []
        self.solution = solution
        self.tags = tags or []
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert question to dictionary format"""
        return {
            "subject": self.subject,
            "chapter": self.chapter,
            "subtopic": self.subtopic,
            "difficulty": self.difficulty,
            "question_type": self.question_type,
            "question": self.question_text,
            "answer": str(self.answer),
            "options": self.options,
            "solution": self.solution,
            "tags": self.tags
        }


class QuestionTemplate(ABC):
    """Abstract base class for all question templates"""
    
    def __init__(self, subject: str, chapter: str, subtopic: str):
        self.subject = subject
        self.chapter = chapter
        self.subtopic = subtopic
        
    @abstractmethod
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        """Generate questions based on template"""
        pass
    
    def _vary_text(self, base_text: str, variations: List[str]) -> str:
        """Randomly vary question text for diversity"""
        return random.choice([base_text] + variations)
    
    def _get_difficulty_multiplier(self, difficulty: str) -> Dict[str, float]:
        """Get numerical multipliers based on difficulty"""
        multipliers = {
            "easy": {"range": (1, 10), "decimal": 0, "steps": 1},
            "medium": {"range": (10, 100), "decimal": 1, "steps": 2},
            "hard": {"range": (50, 500), "decimal": 2, "steps": 3},
            "extreme": {"range": (100, 1000), "decimal": 3, "steps": 4}
        }
        return multipliers.get(difficulty, multipliers["medium"])
    
    def _generate_distractor_options(self, correct_answer: float, 
                                     num_options: int = 3) -> List[str]:
        """Generate plausible but incorrect options for MCQs"""
        distractors = []
        
        # Common mistake patterns
        patterns = [
            lambda x: x * 2,           # Double the answer
            lambda x: x / 2,           # Half the answer
            lambda x: x * 10,          # Order of magnitude error
            lambda x: x / 10,          # Order of magnitude error
            lambda x: -x,              # Sign error
            lambda x: x + random.uniform(1, 10),  # Add random offset
            lambda x: x - random.uniform(1, 10),  # Subtract random offset
            lambda x: x * 1.5,         # 50% more
            lambda x: x * 0.75,        # 25% less
            lambda x: abs(x) if x < 0 else -x,  # Sign flip
        ]
        
        random.shuffle(patterns)
        
        for pattern in patterns[:num_options]:
            try:
                distractor = pattern(correct_answer)
                # Round appropriately
                if abs(distractor) > 100:
                    distractor = round(distractor, 1)
                elif abs(distractor) > 10:
                    distractor = round(distractor, 2)
                else:
                    distractor = round(distractor, 3)
                    
                if distractor != correct_answer and distractor not in distractors:
                    distractors.append(distractor)
            except:
                continue
        
        # Fill remaining slots with random variations
        while len(distractors) < num_options:
            variation = correct_answer * random.uniform(0.5, 2.0)
            variation = round(variation, 2)
            if variation != correct_answer and variation not in distractors:
                distractors.append(variation)
        
        return distractors[:num_options]


class FormulaBasedTemplate(QuestionTemplate):
    """Template for formula-based physics/math problems"""
    
    def __init__(self, subject: str, chapter: str, subtopic: str, 
                 formula: str, variables: Dict[str, tuple]):
        super().__init__(subject, chapter, subtopic)
        self.formula = formula
        self.variables = variables  # {var_name: (min, max, unit)}
        
    def _generate_random_values(self, difficulty: str) -> Dict[str, float]:
        """Generate random values for variables based on difficulty"""
        multiplier = self._get_difficulty_multiplier(difficulty)
        values = {}
        
        for var_name, (min_val, max_val, unit) in self.variables.items():
            # Scale based on difficulty
            scaled_min = min_val * (multiplier["range"][0] / 10)
            scaled_max = max_val * (multiplier["range"][1] / 10)
            
            value = random.uniform(scaled_min, scaled_max)
            
            # Round based on difficulty
            if multiplier["decimal"] == 0:
                value = round(value)
            else:
                value = round(value, multiplier["decimal"])
            
            values[var_name] = value
        
        return values
    
    def _solve_formula(self, values: Dict[str, float], solve_for: str) -> float:
        """Solve formula for unknown variable using SymPy"""
        # Create symbolic variables
        sym_vars = {name: symbols(name) for name in self.variables.keys()}
        
        # Substitute known values
        expr = sp.sympify(self.formula)
        for var_name, value in values.items():
            if var_name != solve_for:
                expr = expr.subs(sym_vars[var_name], value)
        
        # Solve for unknown
        solution = solve(expr, sym_vars[solve_for])
        
        if solution:
            return float(solution[0])
        return 0.0


class NumericalMutator:
    """Utility class for mutating numerical values and expressions"""
    
    @staticmethod
    def mutate_number(value: float, mutation_rate: float = 0.2) -> float:
        """Mutate a number by a small random amount"""
        mutation = random.uniform(-mutation_rate, mutation_rate)
        return value * (1 + mutation)
    
    @staticmethod
    def mutate_expression(expr_str: str, var_mutations: Dict[str, float]) -> str:
        """Mutate variables in an expression"""
        expr = sp.sympify(expr_str)
        for var, value in var_mutations.items():
            expr = expr.subs(symbols(var), value)
        return str(simplify(expr))


class TextMutator:
    """Utility class for mutating question text to create variations"""
    
    SYNONYMS = {
        "ball": ["sphere", "object", "particle", "projectile"],
        "thrown": ["projected", "launched", "tossed", "released"],
        "car": ["vehicle", "automobile", "object"],
        "accelerates": ["speeds up", "gains speed", "increases velocity"],
        "find": ["calculate", "determine", "compute", "evaluate"],
        "distance": ["displacement", "path length"],
        "velocity": ["speed"],
        "force": ["applied force", "net force"],
        "current": ["electric current", "flow of charge"],
        "resistance": ["electrical resistance", "resistor value"],
    }
    
    @staticmethod
    def mutate_text(text: str, mutation_count: int = 2) -> str:
        """Replace random words with synonyms"""
        words = text.split()
        mutated = False
        attempts = 0
        
        while not mutated and attempts < 10:
            for _ in range(mutation_count):
                for i, word in enumerate(words):
                    word_lower = word.lower().strip('.,!?')
                    if word_lower in TextMutator.SYNONYMS and random.random() < 0.5:
                        synonym = random.choice(TextMutator.SYNONYMS[word_lower])
                        # Preserve capitalization
                        if word[0].isupper():
                            synonym = synonym.capitalize()
                        words[i] = word.replace(word_lower, synonym)
                        mutated = True
            attempts += 1
        
        return " ".join(words)
    
    @staticmethod
    def vary_question_prefix() -> str:
        """Generate varied question prefixes"""
        prefixes = [
            "Calculate",
            "Determine",
            "Find",
            "Compute",
            "Evaluate",
            "What is",
            "Solve for"
        ]
        return random.choice(prefixes)


class ConceptMixer:
    """Mix multiple concepts to create complex questions"""
    
    @staticmethod
    def combine_concepts(concept1: str, concept2: str, 
                        difficulty: str = "medium") -> str:
        """Combine two concepts into a multi-step problem"""
        templates = [
            f"A problem involving both {concept1} and {concept2}",
            f"Use {concept1} to solve for an intermediate value, then apply {concept2}",
            f"Apply principles of {concept1} and {concept2} simultaneously"
        ]
        return random.choice(templates)

