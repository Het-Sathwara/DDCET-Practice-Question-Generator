"""
Question Bank System - Load from JSON instead of generating
Much better variety and can easily add hundreds of questions
"""

import random
import json
import os
from typing import List
from ..core.question_engine import Question, QuestionTemplate


class QuestionBankGenerator(QuestionTemplate):
    """Load questions from JSON bank - unlimited variety!"""
    
    def __init__(self, subject: str, chapter: str, subtopic: str, bank_file: str):
        super().__init__(subject, chapter, subtopic)
        self.bank_file = bank_file
        self.question_bank = self._load_bank()
    
    def _load_bank(self):
        """Load question bank from JSON"""
        bank_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 'data', 'question_banks', 
            self.bank_file
        )
        
        try:
            with open(bank_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Question bank {self.bank_file} not found. Using empty bank.")
            return {"easy": [], "medium": [], "hard": []}
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        """Generate questions by randomly selecting from bank"""
        questions = []
        
        # Get questions for this difficulty
        bank = self.question_bank.get(difficulty, [])
        
        if not bank:
            print(f"Warning: No questions in bank for difficulty: {difficulty}")
            return questions
        
        # Randomly select questions (with replacement if count > bank size)
        selected = random.choices(bank, k=count) if len(bank) < count else random.sample(bank, count)
        
        for q_data in selected:
            questions.append(Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty=difficulty,
                question_type=q_data.get('type', 'conceptual'),
                question_text=q_data['question'],
                answer=q_data['answer'],
                solution=q_data['solution'],
                tags=[q_data.get('type', 'general')]
            ))
        
        return questions


class MatricesBankGenerator(QuestionBankGenerator):
    """Matrices questions from bank"""
    
    def __init__(self):
        super().__init__(
            "Mathematics",
            "Determinant and Matrices",
            "Matrices",
            "matrices_bank.json"
        )


class LogarithmBankGenerator(QuestionBankGenerator):
    """Logarithm questions from bank"""
    
    def __init__(self):
        super().__init__(
            "Mathematics",
            "Logarithm",
            "Laws and Equations",
            "logarithm_bank.json"
        )

