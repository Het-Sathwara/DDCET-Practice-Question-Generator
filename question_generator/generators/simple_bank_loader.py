"""
Simple Question Bank Loader - NO difficulty labels, just chapter-based
Loads REAL questions that you add manually
"""

import json
import random
import os
from typing import List, Dict
from ..core.question_engine import Question, QuestionTemplate


class SimpleQuestionBankLoader(QuestionTemplate):
    """Load questions from simple JSON banks (chapter-based, no fake difficulty)"""
    
    def __init__(self, chapter_file: str):
        """
        Initialize with a chapter file (e.g., 'trigonometry.json')
        """
        self.chapter_file = chapter_file
        self.questions_data = self._load_questions()
        
        # Extract chapter name from data
        chapter_name = self.questions_data.get("chapter", "Unknown")
        super().__init__("Mathematics", chapter_name, chapter_name)
    
    def _load_questions(self) -> Dict:
        """Load questions from JSON file"""
        bank_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'data',
            'question_banks',
            self.chapter_file
        )
        
        try:
            with open(bank_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Question bank {self.chapter_file} not found!")
            print(f"   Create it using the template in ADD_QUESTIONS_HERE.md")
            return {"chapter": "Unknown", "questions": []}
    
    def generate(self, difficulty: str = "medium", count: int = 1) -> List[Question]:
        """
        Generate questions by randomly selecting from bank
        NOTE: 'difficulty' parameter is ignored - we don't label difficulty anymore
        """
        questions = []
        
        bank = self.questions_data.get("questions", [])
        
        if not bank:
            print(f"⚠️  No questions found in {self.chapter_file}")
            print(f"   Add questions using the guide in ADD_QUESTIONS_HERE.md")
            return questions
        
        # Randomly select questions (with replacement if needed)
        selected = random.choices(bank, k=count) if len(bank) < count else random.sample(bank, count)
        
        for q_data in selected:
            questions.append(Question(
                subject=self.subject,
                chapter=self.chapter,
                subtopic=self.subtopic,
                difficulty="mixed",  # No fake difficulty labels
                question_type="mixed",
                question_text=q_data.get('question', ''),
                answer=q_data.get('answer', ''),
                solution=q_data.get('solution', ''),
                tags=[self.chapter, q_data.get('source', 'unknown')]
            ))
        
        return questions


# Pre-configured loaders for each topic
class TrigonometryBankLoader(SimpleQuestionBankLoader):
    def __init__(self):
        super().__init__("trigonometry.json")


class CalculusBankLoader(SimpleQuestionBankLoader):
    def __init__(self):
        super().__init__("calculus.json")


class AlgebraBankLoader(SimpleQuestionBankLoader):
    def __init__(self):
        super().__init__("algebra.json")


class VectorsBankLoader(SimpleQuestionBankLoader):
    def __init__(self):
        super().__init__("vectors.json")


class MechanicsBankLoader(SimpleQuestionBankLoader):
    def __init__(self):
        super().__init__("mechanics.json")


class ElectromagnetismBankLoader(SimpleQuestionBankLoader):
    def __init__(self):
        super().__init__("electromagnetism.json")

