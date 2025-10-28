"""
Export Utilities
Handles exporting questions to various formats (JSON, CSV, PDF)
"""

import json
import csv
from typing import List
from datetime import datetime
import os

from ..core.question_engine import Question


class QuestionExporter:
    """Export questions to various formats"""
    
    def __init__(self, output_dir: str = "generated_questions"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def export_to_json(self, questions: List[Question], filename: str = None) -> str:
        """Export questions to JSON format"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"questions_{timestamp}.json"
        
        filepath = os.path.join(self.output_dir, filename)
        
        questions_data = [q.to_dict() for q in questions]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(questions_data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def export_to_csv(self, questions: List[Question], filename: str = None) -> str:
        """Export questions to CSV format"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"questions_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        fieldnames = [
            'subject', 'chapter', 'subtopic', 'difficulty', 
            'question_type', 'question', 'answer', 'options', 'solution', 'tags'
        ]
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for q in questions:
                row = q.to_dict()
                # Convert lists to strings for CSV
                if row['options']:
                    row['options'] = ' | '.join(row['options'])
                if row['tags']:
                    row['tags'] = ', '.join(row['tags'])
                writer.writerow(row)
        
        return filepath
    
    def export_to_text(self, questions: List[Question], filename: str = None) -> str:
        """Export questions to human-readable text format"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"questions_{timestamp}.txt"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("GENERATED QUESTIONS\n")
            f.write("=" * 80 + "\n\n")
            
            for i, q in enumerate(questions, 1):
                f.write(f"Question {i}\n")
                f.write(f"{'='*60}\n")
                f.write(f"Subject: {q.subject}\n")
                f.write(f"Chapter: {q.chapter}\n")
                f.write(f"Subtopic: {q.subtopic}\n")
                f.write(f"Difficulty: {q.difficulty}\n")
                f.write(f"Type: {q.question_type}\n")
                f.write(f"\n{q.question_text}\n")
                
                if q.options:
                    f.write("\nOptions:\n")
                    for opt in q.options:
                        f.write(f"  • {opt}\n")
                
                f.write(f"\nAnswer: {q.answer}\n")
                
                if q.solution:
                    f.write(f"\nSolution: {q.solution}\n")
                
                f.write(f"\nTags: {', '.join(q.tags)}\n")
                f.write("\n" + "="*60 + "\n\n")
        
        return filepath
    
    def export_summary(self, questions: List[Question], filename: str = None) -> str:
        """Export summary statistics"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"summary_{timestamp}.txt"
        
        filepath = os.path.join(self.output_dir, filename)
        
        # Calculate statistics
        total = len(questions)
        by_subject = {}
        by_difficulty = {}
        by_type = {}
        by_chapter = {}
        
        for q in questions:
            # Count by subject
            by_subject[q.subject] = by_subject.get(q.subject, 0) + 1
            
            # Count by difficulty
            by_difficulty[q.difficulty] = by_difficulty.get(q.difficulty, 0) + 1
            
            # Count by type
            by_type[q.question_type] = by_type.get(q.question_type, 0) + 1
            
            # Count by chapter
            key = f"{q.subject} - {q.chapter}"
            by_chapter[key] = by_chapter.get(key, 0) + 1
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("QUESTION GENERATION SUMMARY\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Total Questions Generated: {total}\n\n")
            
            f.write("By Subject:\n")
            for subject, count in sorted(by_subject.items()):
                f.write(f"  • {subject}: {count} ({count/total*100:.1f}%)\n")
            
            f.write("\nBy Difficulty:\n")
            for difficulty, count in sorted(by_difficulty.items()):
                f.write(f"  • {difficulty}: {count} ({count/total*100:.1f}%)\n")
            
            f.write("\nBy Question Type:\n")
            for qtype, count in sorted(by_type.items()):
                f.write(f"  • {qtype}: {count} ({count/total*100:.1f}%)\n")
            
            f.write("\nBy Chapter:\n")
            for chapter, count in sorted(by_chapter.items()):
                f.write(f"  • {chapter}: {count}\n")
            
            f.write("\n" + "=" * 80 + "\n")
        
        return filepath


class QuestionLoader:
    """Load previously generated questions"""
    
    @staticmethod
    def load_from_json(filepath: str) -> List[Question]:
        """Load questions from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        questions = []
        for q_data in data:
            q = Question(
                subject=q_data['subject'],
                chapter=q_data['chapter'],
                subtopic=q_data['subtopic'],
                difficulty=q_data['difficulty'],
                question_type=q_data['question_type'],
                question_text=q_data['question'],
                answer=q_data['answer'],
                options=q_data.get('options', []),
                solution=q_data.get('solution', ''),
                tags=q_data.get('tags', [])
            )
            questions.append(q)
        
        return questions

