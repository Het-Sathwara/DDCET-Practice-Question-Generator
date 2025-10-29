"""
Interactive CLI Interface
menu-driven command-line interface for question generation
"""

import os
import sys
import time
from typing import List, Dict, Any
from colorama import init, Fore, Back, Style
import questionary
from questionary import Style as QStyle

from ..core.question_engine import Question
from ..generators.physics_generators import (
    KinematicsGenerator, NewtonLawsGenerator, CircularMotionGenerator,
    WorkEnergyGenerator, OhmsLawGenerator, CapacitanceGenerator,
    HeatTransferGenerator, WaveMotionGenerator
)
from ..generators.physics_generators_additional import (
    UnitsAndMeasurementGenerator, ElectrostaticsGenerator, OpticsGenerator
)
# Math generators - Bank-based for better variety
from ..generators.math_bank_generator import (
    MatricesBankGenerator, LogarithmBankGenerator
)
# Legacy
from ..generators.math_generators import (
    StatisticsGenerator
)
# New comprehensive individual generators
from ..maths import (
    generate_trigonometric_questions,
    generate_vector_questions,
    generate_coordinate_geometry_questions,
    generate_limit_questions,
    generate_differentiation_questions,
    generate_integration_questions
)
from ..utils.export_utils import QuestionExporter

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

# Custom questionary style
custom_style = QStyle([
    ('qmark', 'fg:#673ab7 bold'),
    ('question', 'bold'),
    ('answer', 'fg:#f44336 bold'),
    ('pointer', 'fg:#673ab7 bold'),
    ('highlighted', 'fg:#673ab7 bold'),
    ('selected', 'fg:#cc5454'),
    ('separator', 'fg:#cc5454'),
    ('instruction', ''),
    ('text', ''),
    ('disabled', 'fg:#858585 italic')
])


# Wrapper classes for new function-based generators
class TrigonometryGeneratorWrapper:
    """Wrapper for new trigonometry function-based generator"""
    def generate(self, difficulty: str = "medium", count: int = 10) -> List[Question]:
        questions_data = generate_trigonometric_questions(difficulty, max(count, 20), 'all')
        return [self._dict_to_question(q, "Trigonometry") for q in questions_data[:count]]
    
    def _dict_to_question(self, q_dict: Dict, topic: str) -> Question:
        return Question(
            subject="Mathematics",
            chapter="Trigonometry",
            subtopic=topic,
            difficulty=q_dict.get('difficulty', 'medium'),
            question_type=q_dict.get('type', 'numerical'),
            question_text=q_dict['question'],
            answer=q_dict['answer'],
            options=q_dict.get('options'),
            solution=q_dict.get('solution'),
            tags=[]
        )


class VectorsGeneratorWrapper:
    """Wrapper for new vectors function-based generator"""
    def generate(self, difficulty: str = "medium", count: int = 10) -> List[Question]:
        questions_data = generate_vector_questions(difficulty, max(count, 15), 'all')
        return [self._dict_to_question(q, "Vectors") for q in questions_data[:count]]
    
    def _dict_to_question(self, q_dict: Dict, topic: str) -> Question:
        return Question(
            subject="Mathematics",
            chapter="Vectors",
            subtopic=topic,
            difficulty=q_dict.get('difficulty', 'medium'),
            question_type=q_dict.get('type', 'numerical'),
            question_text=q_dict['question'],
            answer=q_dict['answer'],
            options=q_dict.get('options'),
            solution=q_dict.get('solution'),
            tags=[]
        )


class CoordinateGeometryGeneratorWrapper:
    """Wrapper for new coordinate geometry function-based generator"""
    def generate(self, difficulty: str = "medium", count: int = 10) -> List[Question]:
        questions_data = generate_coordinate_geometry_questions(difficulty, max(count, 15), 'all')
        return [self._dict_to_question(q, "Coordinate Geometry") for q in questions_data[:count]]
    
    def _dict_to_question(self, q_dict: Dict, topic: str) -> Question:
        return Question(
            subject="Mathematics",
            chapter="Coordinate Geometry",
            subtopic=topic,
            difficulty=q_dict.get('difficulty', 'medium'),
            question_type=q_dict.get('type', 'numerical'),
            question_text=q_dict['question'],
            answer=q_dict['answer'],
            options=q_dict.get('options'),
            solution=q_dict.get('solution'),
            tags=[]
        )


class LimitsGeneratorWrapper:
    """Wrapper for new limits function-based generator (14+ formulas)"""
    def generate(self, difficulty: str = "medium", count: int = 10) -> List[Question]:
        questions_data = generate_limit_questions(difficulty, max(count, 20), 'trig')
        if len(questions_data) < count:
            questions_data.extend(generate_limit_questions(difficulty, count, 'log_exp'))
        return [self._dict_to_question(q, "Limits") for q in questions_data[:count]]
    
    def _dict_to_question(self, q_dict: Dict, topic: str) -> Question:
        return Question(
            subject="Mathematics",
            chapter="Limits",
            subtopic=q_dict.get('topic', topic),
            difficulty=q_dict.get('difficulty', 'medium'),
            question_type=q_dict.get('type', 'numerical'),
            question_text=q_dict['question'],
            answer=q_dict['answer'],
            options=q_dict.get('options'),
            solution=q_dict.get('solution'),
            tags=[]
        )


class DifferentiationGeneratorWrapper:
    """Wrapper for new differentiation function-based generator (20+ formulas)"""
    def generate(self, difficulty: str = "medium", count: int = 10) -> List[Question]:
        questions_data = generate_differentiation_questions(difficulty, max(count, 20), 'trig')
        if len(questions_data) < count:
            questions_data.extend(generate_differentiation_questions(difficulty, count, 'power'))
        return [self._dict_to_question(q, "Differentiation") for q in questions_data[:count]]
    
    def _dict_to_question(self, q_dict: Dict, topic: str) -> Question:
        return Question(
            subject="Mathematics",
            chapter="Calculus",
            subtopic=q_dict.get('topic', topic),
            difficulty=q_dict.get('difficulty', 'medium'),
            question_type=q_dict.get('type', 'conceptual'),
            question_text=q_dict['question'],
            answer=str(q_dict['answer']),
            options=q_dict.get('options'),
            solution=q_dict.get('solution'),
            tags=[]
        )


class IntegrationGeneratorWrapper:
    """Wrapper for new integration function-based generator (20+ formulas)"""
    def generate(self, difficulty: str = "medium", count: int = 10) -> List[Question]:
        questions_data = generate_integration_questions(difficulty, max(count, 20), 'trig')
        if len(questions_data) < count:
            questions_data.extend(generate_integration_questions(difficulty, count, 'basic'))
        return [self._dict_to_question(q, "Integration") for q in questions_data[:count]]
    
    def _dict_to_question(self, q_dict: Dict, topic: str) -> Question:
        return Question(
            subject="Mathematics",
            chapter="Calculus",
            subtopic=q_dict.get('topic', topic),
            difficulty=q_dict.get('difficulty', 'medium'),
            question_type=q_dict.get('type', 'conceptual'),
            question_text=q_dict['question'],
            answer=str(q_dict['answer']),
            options=q_dict.get('options'),
            solution=q_dict.get('solution'),
            tags=[]
        )


class QuestionGeneratorCLI:
    """Main CLI application for question generation"""
    
    def __init__(self):
        self.exporter = QuestionExporter()
        self.generated_questions = []
        self.last_generation_time = 0
        self.generation_cooldown = 2  # seconds
        self.max_questions_per_generation = 100
        
        # Physics generators mapping - Complete DDCET Coverage
        self.physics_generators = {
            "Units & Measurement": UnitsAndMeasurementGenerator,  # NEW
            "Kinematics (Linear Motion)": KinematicsGenerator,
            "Newton's Laws of Motion": NewtonLawsGenerator,
            "Circular Motion": CircularMotionGenerator,
            "Work, Energy & Power": WorkEnergyGenerator,
            "Ohm's Law & Electric Current": OhmsLawGenerator,
            "Electrostatics (Coulomb's Law)": ElectrostaticsGenerator,  # NEW
            "Capacitance": CapacitanceGenerator,
            "Heat & Thermometry": HeatTransferGenerator,
            "Wave Motion": WaveMotionGenerator,
            "Optics (Refraction & TIR)": OpticsGenerator  # NEW
        }
        
        # Mathematics generators mapping (using NEW comprehensive generators)
        self.math_generators = {
            "Trigonometry (50+ formulas)": TrigonometryGeneratorWrapper,
            "Limits (14+ formulas)": LimitsGeneratorWrapper,
            "Differentiation (20+ formulas)": DifferentiationGeneratorWrapper,
            "Integration (20+ formulas)": IntegrationGeneratorWrapper,
            "Vectors": VectorsGeneratorWrapper,
            "Coordinate Geometry": CoordinateGeometryGeneratorWrapper,
            "Matrices & Determinants": MatricesBankGenerator,
            "Logarithm": LogarithmBankGenerator,
            "Statistics": StatisticsGenerator
        }
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print application header"""
        self.clear_screen()
        print(Fore.CYAN + Style.BRIGHT + "=" * 80)
        print(Fore.GREEN + "Question Generation ".center(80))
        print(Fore.CYAN + "=" * 80 + "\n")
    
    def print_success(self, message: str):
        """Print success message"""
        print(Fore.GREEN + Style.BRIGHT + "[SUCCESS] " + message)
    
    def print_error(self, message: str):
        """Print error message"""
        print(Fore.RED + Style.BRIGHT + "[ERROR] " + message)
    
    def print_info(self, message: str):
        """Print info message"""
        print(Fore.CYAN + Style.BRIGHT + "[INFO] " + message)
    
    def print_warning(self, message: str):
        """Print warning message"""
        print(Fore.YELLOW + Style.BRIGHT + "[WARNING] " + message)
    
    def show_main_menu(self) -> str:
        """Display main menu and get user choice"""
        self.print_header()
        
        if self.generated_questions:
            self.print_info(f"Current session: {len(self.generated_questions)} questions generated\n")
        
        choices = [
            "Generate Physics Questions",
            "Generate Mathematics Questions",
            "Generate Mixed Question Set",
            "Preview Generated Questions",
            "Export Questions",
            "View Statistics",
            "Clear Generated Questions",
            "Exit"
        ]
        
        choice = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()
        
        return choice
    
    def generate_physics_questions(self):
        """Generate physics questions workflow"""
        self.print_header()
        print(Fore.CYAN + Style.BRIGHT + "PHYSICS QUESTION GENERATION\n")
        
        # Select topic
        topic = questionary.select(
            "Select Physics topic:",
            choices=list(self.physics_generators.keys()) + ["← Back"],
            style=custom_style
        ).ask()
        
        if topic == "← Back":
            return
        
        # Select difficulty
        difficulty = questionary.select(
            "Select difficulty level:",
            choices=["easy", "medium", "hard", "extreme"],
            style=custom_style
        ).ask()
        
        # Select count with limit
        count = questionary.text(
            f"How many questions to generate? (Max: {self.max_questions_per_generation})",
            default="10",
            validate=lambda x: x.isdigit() and 0 < int(x) <= self.max_questions_per_generation
        ).ask()
        
        count = int(count)
        
        # Spam prevention
        current_time = time.time()
        time_since_last = current_time - self.last_generation_time
        
        if time_since_last < self.generation_cooldown and self.last_generation_time > 0:
            wait_time = self.generation_cooldown - time_since_last
            self.print_warning(f"Please wait {wait_time:.1f} seconds...")
            time.sleep(wait_time)
        
        # Generate questions
        self.print_info(f"\nGenerating {count} {difficulty} questions on {topic}...\n")
        
        try:
            generator_class = self.physics_generators[topic]
            generator = generator_class()
            questions = generator.generate(difficulty=difficulty, count=count)
            
            self.generated_questions.extend(questions)
            self.last_generation_time = time.time()
            self.print_success(f"Successfully generated {len(questions)} questions!")
            
            # Preview option
            if questionary.confirm(
                "Would you like to preview the generated questions?",
                style=custom_style
            ).ask():
                self.preview_questions(questions)
        
        except Exception as e:
            self.print_error(f"Error generating questions: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def generate_math_questions(self):
        """Generate mathematics questions workflow"""
        self.print_header()
        print(Fore.CYAN + Style.BRIGHT + "MATHEMATICS QUESTION GENERATION\n")
        
        # Select topic
        topic = questionary.select(
            "Select Mathematics topic:",
            choices=list(self.math_generators.keys()) + ["← Back"],
            style=custom_style
        ).ask()
        
        if topic == "← Back":
            return
        
        # Check if function-based generator (has formulas in name or is Vectors/Coordinate)
        is_function_generator = ("formulas" in topic or 
                                 topic in ["Vectors", "Coordinate Geometry"])
        
        # Dual-mode option for function generators
        use_generation_mode = False
        if is_function_generator:
            mode = questionary.select(
                "Select mode:",
                choices=[
                    "Question Bank (Better quality, all difficulties)",
                    "Auto Generate (Easy questions only)",
                    "← Back"
                ],
                style=custom_style
            ).ask()
            
            if mode == "← Back":
                return
            
            use_generation_mode = (mode == "Auto Generate (Easy questions only)")
        
        # Select difficulty
        if use_generation_mode:
            difficulty = "easy"
            self.print_warning("Auto Generate mode creates easy-level questions only")
        else:
            difficulty = questionary.select(
                "Select difficulty level:",
                choices=["easy", "medium", "hard", "extreme"],
                style=custom_style
            ).ask()
        
        # Select count with limit
        count = questionary.text(
            f"How many questions to generate? (Max: {self.max_questions_per_generation})",
            default="10",
            validate=lambda x: x.isdigit() and 0 < int(x) <= self.max_questions_per_generation
        ).ask()
        
        count = int(count)
        
        # Spam prevention
        current_time = time.time()
        time_since_last = current_time - self.last_generation_time
        
        if time_since_last < self.generation_cooldown and self.last_generation_time > 0:
            wait_time = self.generation_cooldown - time_since_last
            self.print_warning(f"Please wait {wait_time:.1f} seconds...")
            time.sleep(wait_time)
        
        # Generate questions
        self.print_info(f"\nGenerating {count} {difficulty} questions on {topic}...\n")
        
        try:
            generator_class = self.math_generators[topic]
            generator = generator_class()
            questions = generator.generate(difficulty=difficulty, count=count)
            
            self.generated_questions.extend(questions)
            self.last_generation_time = time.time()
            self.print_success(f"Successfully generated {len(questions)} questions!")
            
            # Preview option
            if questionary.confirm(
                "Would you like to preview the generated questions?",
                style=custom_style
            ).ask():
                self.preview_questions(questions)
        
        except Exception as e:
            self.print_error(f"Error generating questions: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def generate_mixed_questions(self):
        """Generate a mixed set of physics and math questions"""
        self.print_header()
        print(Fore.CYAN + Style.BRIGHT + "MIXED QUESTION SET GENERATION\n")
        
        # Get parameters
        difficulty = questionary.select(
            "Select difficulty level:",
            choices=["easy", "medium", "hard", "extreme"],
            style=custom_style
        ).ask()
        
        total_count = questionary.text(
            "Total questions to generate?",
            default="50",
            validate=lambda x: x.isdigit() and int(x) > 0
        ).ask()
        
        total_count = int(total_count)
        
        # Split between physics and math
        physics_count = total_count // 2
        math_count = total_count - physics_count
        
        self.print_info(f"\nGenerating {physics_count} Physics + {math_count} Math questions...\n")
        
        try:
            all_questions = []
            
            # Generate physics questions
            for generator_class in self.physics_generators.values():
                generator = generator_class()
                count_per_topic = max(1, physics_count // len(self.physics_generators))
                questions = generator.generate(difficulty=difficulty, count=count_per_topic)
                all_questions.extend(questions)
            
            # Generate math questions
            for generator_class in self.math_generators.values():
                generator = generator_class()
                count_per_topic = max(1, math_count // len(self.math_generators))
                questions = generator.generate(difficulty=difficulty, count=count_per_topic)
                all_questions.extend(questions)
            
            self.generated_questions.extend(all_questions)
            self.print_success(f"Successfully generated {len(all_questions)} mixed questions!")
            
        except Exception as e:
            self.print_error(f"Error generating questions: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def preview_questions(self, questions: List[Question] = None):
        """Preview generated questions"""
        if questions is None:
            questions = self.generated_questions
        
        if not questions:
            self.print_warning("No questions to preview!")
            input("\nPress Enter to continue...")
            return
        
        self.print_header()
        print(Fore.CYAN + Style.BRIGHT + f"PREVIEW: {len(questions)} Questions\n")
        
        # Show first 5 questions
        preview_count = min(5, len(questions))
        
        for i, q in enumerate(questions[:preview_count], 1):
            print(Fore.YELLOW + Style.BRIGHT + f"\n{'='*70}")
            print(Fore.YELLOW + Style.BRIGHT + f"Question {i}")
            print(Fore.YELLOW + Style.BRIGHT + f"{'='*70}")
            print(Fore.CYAN + f"Subject: {q.subject} | Chapter: {q.chapter}")
            print(Fore.CYAN + f"Difficulty: {q.difficulty} | Type: {q.question_type}")
            print(Fore.WHITE + Style.BRIGHT + f"\n{q.question_text}")
            
            if q.options:
                print(Fore.GREEN + "\nOptions:")
                for opt in q.options:
                    print(Fore.GREEN + f"  • {opt}")
            
            print(Fore.MAGENTA + f"\nAnswer: {q.answer}")
            
            if q.solution:
                print(Fore.BLUE + f"Solution: {q.solution}")
        
        if len(questions) > preview_count:
            print(Fore.YELLOW + f"\n... and {len(questions) - preview_count} more questions")
        
        input("\nPress Enter to continue...")
    
    def export_questions(self):
        """Export questions workflow"""
        if not self.generated_questions:
            self.print_warning("No questions to export!")
            input("\nPress Enter to continue...")
            return
        
        self.print_header()
        print(Fore.CYAN + Style.BRIGHT + "EXPORT QUESTIONS\n")
        
        # Select format
        format_choice = questionary.select(
            "Select export format:",
            choices=["JSON", "CSV", "Text File", "All Formats", "← Back"],
            style=custom_style
        ).ask()
        
        if format_choice == "← Back":
            return
        
        # Get filename
        filename_base = questionary.text(
            "Enter filename (without extension):",
            default="ddcet_questions"
        ).ask()
        
        try:
            exported_files = []
            
            if format_choice == "JSON" or format_choice == "All Formats":
                filepath = self.exporter.export_to_json(
                    self.generated_questions,
                    f"{filename_base}.json"
                )
                exported_files.append(filepath)
            
            if format_choice == "CSV" or format_choice == "All Formats":
                filepath = self.exporter.export_to_csv(
                    self.generated_questions,
                    f"{filename_base}.csv"
                )
                exported_files.append(filepath)
            
            if format_choice == "Text File" or format_choice == "All Formats":
                filepath = self.exporter.export_to_text(
                    self.generated_questions,
                    f"{filename_base}.txt"
                )
                exported_files.append(filepath)
            
            # Always export summary
            summary_path = self.exporter.export_summary(
                self.generated_questions,
                f"{filename_base}_summary.txt"
            )
            exported_files.append(summary_path)
            
            self.print_success(f"\n✓ Exported {len(self.generated_questions)} questions!")
            self.print_info("\nExported files:")
            for filepath in exported_files:
                print(Fore.GREEN + f"  [FILE] {filepath}")
        
        except Exception as e:
            self.print_error(f"Error exporting questions: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def view_statistics(self):
        """View statistics about generated questions"""
        if not self.generated_questions:
            self.print_warning("No questions generated yet!")
            input("\nPress Enter to continue...")
            return
        
        self.print_header()
        print(Fore.CYAN + Style.BRIGHT + "STATISTICS\n")
        
        # Calculate statistics
        total = len(self.generated_questions)
        
        # By subject
        by_subject = {}
        by_difficulty = {}
        by_type = {}
        by_chapter = {}
        
        for q in self.generated_questions:
            by_subject[q.subject] = by_subject.get(q.subject, 0) + 1
            by_difficulty[q.difficulty] = by_difficulty.get(q.difficulty, 0) + 1
            by_type[q.question_type] = by_type.get(q.question_type, 0) + 1
            key = f"{q.subject} - {q.chapter}"
            by_chapter[key] = by_chapter.get(key, 0) + 1
        
        print(Fore.YELLOW + Style.BRIGHT + f"Total Questions: {total}\n")
        
        print(Fore.CYAN + Style.BRIGHT + "By Subject:")
        for subject, count in sorted(by_subject.items()):
            percentage = count / total * 100
            print(Fore.GREEN + f"  • {subject}: {count} ({percentage:.1f}%)")
        
        print(Fore.CYAN + Style.BRIGHT + "\nBy Difficulty:")
        for difficulty, count in sorted(by_difficulty.items()):
            percentage = count / total * 100
            print(Fore.GREEN + f"  • {difficulty}: {count} ({percentage:.1f}%)")
        
        print(Fore.CYAN + Style.BRIGHT + "\nBy Question Type:")
        for qtype, count in sorted(by_type.items()):
            percentage = count / total * 100
            print(Fore.GREEN + f"  • {qtype}: {count} ({percentage:.1f}%)")
        
        print(Fore.CYAN + Style.BRIGHT + "\nTop Chapters:")
        sorted_chapters = sorted(by_chapter.items(), key=lambda x: x[1], reverse=True)[:10]
        for chapter, count in sorted_chapters:
            print(Fore.GREEN + f"  • {chapter}: {count}")
        
        input("\nPress Enter to continue...")
    
    def clear_questions(self):
        """Clear all generated questions"""
        if not self.generated_questions:
            self.print_warning("No questions to clear!")
            input("\nPress Enter to continue...")
            return
        
        if questionary.confirm(
            f"Are you sure you want to clear {len(self.generated_questions)} questions?",
            style=custom_style
        ).ask():
            self.generated_questions.clear()
            self.print_success("All questions cleared!")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main application loop"""
        while True:
            choice = self.show_main_menu()
            
            if choice == "Generate Physics Questions":
                self.generate_physics_questions()
            
            elif choice == "Generate Mathematics Questions":
                self.generate_math_questions()
            
            elif choice == "Generate Mixed Question Set":
                self.generate_mixed_questions()
            
            elif choice == "Preview Generated Questions":
                self.preview_questions()
            
            elif choice == "Export Questions":
                self.export_questions()
            
            elif choice == "View Statistics":
                self.view_statistics()
            
            elif choice == "Clear Generated Questions":
                self.clear_questions()
            
            elif choice == "Exit":
                self.print_header()
                if self.generated_questions:
                    if questionary.confirm(
                        f"You have {len(self.generated_questions)} unsaved questions. Exit anyway?",
                        style=custom_style
                    ).ask():
                        break
                else:
                    break
        
        self.print_header()
        print(Fore.GREEN + Style.BRIGHT + "Thank you for using the DDCET Question Generator! 🎓\n")
        print(Fore.CYAN + "Questions generated in this session: " + 
              Fore.YELLOW + Style.BRIGHT + str(len(self.generated_questions)))
        print()


def main():
    """Entry point for CLI application"""
    try:
        app = QuestionGeneratorCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "Operation cancelled by user.")
    except Exception as e:
        print("\n" + Fore.RED + f"Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

