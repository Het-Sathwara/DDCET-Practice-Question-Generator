# Question Generator

A comprehensive, intelligent question generation system for Physics and Mathematics based on the **DDCET (Diploma to Degree Common Entrance Test)** syllabus
## Status: Prototype | 130+ Formulas | 20 Generators

### Latest Update: Comprehensive Individual Math Generators
- Limits: 14+ formulas (ALL from formula image)
- Differentiation: 20+ formulas (ALL from PDF)
- Integration: 20+ formulas (ALL from PDF)

## Features

### Intelligent Question Generation
- **Dynamic Parameter-Based Generation**: Not just templates - questions mutate with different values, concepts, and solving approaches
- **Formula Engine**: Uses SymPy for symbolic mathematics to ensure mathematical correctness
- **Adaptive Difficulty Scaling**: Easy → Medium → Hard → Extreme
- **Multiple Question Types**: MCQ, Numerical Answer, Integer Type, Conceptual Reasoning

### Physics Coverage (8 Generators - ALL TESTED & WORKING)
- Kinematics (Linear Motion)
- Newton's Laws of Motion
- Circular Motion
- Work, Energy & Power
- Ohm's Law & Electric Current
- Capacitance
- Heat & Thermometry
- Wave Motion

### Mathematics Coverage

#### **Individual Comprehensive Generators** (in `question_generator/maths/`)
These topics have dedicated, comprehensive individual files with extensive formula coverage:

- **Trigonometry** (780 lines, 50+ formulas)
  - ALL 6 functions: sin, cos, tan, **cot**, sec, cosec
  - Pythagorean identities, compound angles, double/triple/half angles
  - Sum-to-product & product-to-sum formulas
  - Allied angles, periods, angle conversions
  - **12 question type generators**
  
- **Limits** **NEW!** (549 lines, 14+ formulas)
  - ALL 6 trigonometric limits (sin(x)/x, etc.)
  - 3 forms of 1^∞  
  - 5 log/exponential limits
  - L'Hospital's Rule
  - Limits at infinity
  - **ALL formulas from formula image!**
  
- **Differentiation** **NEW!** (674 lines, 20+ formulas)
  - ALL 6 basic rules (constant, sum, product, quotient, chain, power)
  - ALL 6 trig derivatives (sin, cos, tan, **cot**, sec, csc)
  - ALL 6 inverse trig derivatives (sin⁻¹, cos⁻¹, tan⁻¹, **cot⁻¹**, sec⁻¹, csc⁻¹)
  - Exponential & logarithmic derivatives
  - Parametric, implicit, logarithmic differentiation
  - Applications (velocity, acceleration)
  - **ALL formulas from PDF!**
  
- **Integration** **NEW!** (554 lines, 20+ formulas)
  - ALL 3 basic integrals (∫dx, ∫x^n dx, ∫1/x dx)
  - ALL 6 trig integrals (sin, cos, tan, **cot**, sec, csc)
  - Trig squared (sec², csc²) & products (sec·tan, csc·cot)
  - 3 inverse trig integrals
  - Exponential & logarithmic integrals
  - Substitution, by parts, definite integrals
  - **ALL formulas from PDF!**
  
- **Vectors** (319 lines, 6 formulas)
  - Magnitude, unit vectors, addition/subtraction
  - Dot product (scalar product)
  - Cross product (vector product)
  - Angle between vectors, vector types
  
- **Coordinate Geometry** (344 lines, 10 formulas)
  - Slope, distance, midpoint formulas
  - Line equations (all forms)
  - Parallel/perpendicular lines
  - Circle equations (standard & general)

#### **Legacy Generators** (in `question_generator/generators/math_generators.py`)
Remaining basic generators without comprehensive individual files yet:
- Matrices & Determinants (determinant calculation, operations)
- Logarithm (laws of logarithm)
- Statistics (mean, median, mode - ungrouped data)

### Smart Features

#### 1. **Intelligent MCQ Distractor Generation**
Creates plausible but incorrect options based on common mistake patterns:
- Sign errors
- Unit mistakes
- Order of magnitude errors
- Formula misapplication
- Calculation errors

#### 2. **Question Text Mutation**
Automatically varies question wording for diversity:
```
"A ball is thrown..." → "An object is projected..." → "A particle is launched..."
```

#### 3. **Multi-Step Problem Generation**
Combines multiple concepts for advanced difficulty levels.

#### 4. **Practice Set Generator**
Generate custom sets by:
- Subject (Physics/Mathematics)
- Chapter/Topic
- Difficulty Level
- Question Count

### Export Capabilities
- **JSON**: Machine-readable format for integration
- **CSV**: Spreadsheet-compatible for analysis
- **Text**: Human-readable formatted output
- **Summary Statistics**: Detailed breakdown of generated questions

### Beautiful CLI Interface
- Color-coded menus and output
- Interactive question selection
- Real-time preview
- Progress tracking
- Session management

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or download the repository**
```bash
cd /home/toji/Python
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install sympy numpy colorama questionary python-dateutil
```

## 📖 Usage

### Quick Start

Run the main application:
```bash
python main.py
```

Or directly:
```bash
python -m question_generator.cli.cli_interface
```

### Interactive CLI Workflow

1. **Start the Application**
   - Beautiful menu-driven interface appears

2. **Generate Questions**
   - Choose: Physics, Mathematics, or Mixed
   - Select topic/chapter
   - Choose difficulty: easy/medium/hard/extreme
   - Specify quantity

3. **Preview Questions**
   - View generated questions before export
   - Check quality and variety

4. **Export Results**
   - Choose format: JSON/CSV/Text
   - Get summary statistics
   - Files saved to `generated_questions/` directory

5. **View Statistics**
   - See breakdown by subject, difficulty, type
   - Track your question generation session

### Example: Generate 50 Physics Questions

```python
# Via CLI
1. Select: "Generate Physics Questions"
2. Choose: "Kinematics (Linear Motion)"
3. Difficulty: "medium"
4. Count: "50"
5. Preview and export!
```

### Programmatic Usage

You can also use the generators programmatically:

#### Using Physics Generators (Class-based)
```python
from question_generator.generators.physics_generators import KinematicsGenerator
from question_generator.utils.export_utils import QuestionExporter

# Create generator
generator = KinematicsGenerator()

# Generate 20 medium difficulty questions
questions = generator.generate(difficulty="medium", count=20)

# Export to JSON
exporter = QuestionExporter()
filepath = exporter.export_to_json(questions, "kinematics_practice.json")

print(f"Exported to: {filepath}")
```

#### Using NEW Math Generators (Function-based)
```python
from question_generator.maths import (
    generate_differentiation_questions,
    generate_integration_questions,
    generate_limit_questions,
    generate_trigonometric_questions
)

# Generate 15 hard-level differentiation questions (all types)
diff_questions = generate_differentiation_questions(
    difficulty="hard", 
    count=15, 
    question_type="all"
)

# Generate 10 medium trigonometric limit questions
limit_questions = generate_limit_questions(
    difficulty="medium",
    count=10,
    question_type="trig"
)

# Print results
for q in diff_questions[:3]:
    print(f"Q: {q['question']}")
    print(f"A: {q['answer']}")
    print(f"Solution: {q['solution']}\n")
```

#### Using Legacy Math Generators (Class-based)
```python
from question_generator.generators.math_generators import MatricesGenerator

# Generate matrices questions
gen = MatricesGenerator()
questions = gen.generate(difficulty="medium", count=10)

for q in questions:
    print(f"Q: {q.question_text}")
    print(f"A: {q.answer}\n")
```

## Project Structure

```
question_generator/
├── core/
│   ├── __init__.py
│   └── question_engine.py              # Base classes, Question template engine
│
├── generators/
│   ├── __init__.py
│   ├── physics_generators.py           # 8 Physics generators (all topics)
│   └── math_generators.py              # 3 Legacy math generators (Matrices, Logarithm, Statistics)
│
├── maths/                               # NEW: Comprehensive individual math generators
│   ├── __init__.py                     # Registry for all math generators
│   ├── trigonometric_functions.py      # 780 lines, 50+ formulas, 12 question types
│   ├── limits.py                       # 549 lines, 14+ formulas (from formula image)
│   ├── differentiation.py              # 674 lines, 20+ formulas (from PDF)
│   ├── integration.py                  # 554 lines, 20+ formulas (from PDF)
│   ├── vectors.py                      # 319 lines, 6 formulas
│   └── coordinate_geometry.py          # 344 lines, 10 formulas
│
├── utils/
│   ├── __init__.py
│   └── export_utils.py                 # Export to JSON/CSV/Text with statistics
│
├── cli/
│   ├── __init__.py
│   └── cli_interface.py                # Interactive menu-driven CLI
│
└── __init__.py

generated_questions/                     # Auto-created directory for exports
├── questions_TIMESTAMP.json
├── questions_TIMESTAMP.csv
├── questions_TIMESTAMP.txt
└── summary_TIMESTAMP.txt

main.py                                  # Entry point - Run this!
requirements.txt                         # Python dependencies
README.md                                # This file
```

## Question Types

### 1. Multiple Choice Questions (MCQ)
- 4 options
- Smart distractor generation
- Plausible incorrect answers

### 2. Numerical Answer
- Exact numerical value
- With units
- Precision specified

### 3. Integer Type
- Whole number answers
- Common in competitive exams

### 4. Conceptual/Reasoning
- Formula-based
- Derivation questions
- Theory applications

## 🔧 Advanced Features

### Difficulty Scaling

| Level | Characteristics |
|-------|----------------|
| **Easy** | Simple values, 1-step problems, basic formulas |
| **Medium** | Moderate values, 2-step problems, combined concepts |
| **Hard** | Complex values, 3-step problems, multiple concepts |
| **Extreme** | Very complex, 4+ steps, advanced reasoning, JEE-level |

### Question Metadata

Each question includes:
- Subject & Chapter
- Subtopic
- Difficulty level
- Question type
- Tags for categorization
- Full solution steps

## 📊 Export Formats

### JSON Output
```json
{
  "subject": "Physics",
  "chapter": "Classical Mechanics",
  "subtopic": "Kinematics",
  "difficulty": "medium",
  "question_type": "mcq",
  "question": "A car accelerates uniformly from rest at 2 m/s²...",
  "answer": "25 m",
  "options": ["25 m", "50 m", "12.5 m", "5 m"],
  "solution": "Using s = ut + ½at² = 0 + 0.5×2×5² = 25 m",
  "tags": ["kinematics", "displacement", "equations_of_motion"]
}
```

### CSV Output
Spreadsheet-compatible with columns:
- subject, chapter, subtopic, difficulty
- question_type, question, answer
- options, solution, tags

## 🧪 Example Generated Questions

### Physics - Kinematics (Medium)
**Q:** A vehicle accelerates uniformly from 10 m/s at 3 m/s². Find the final velocity after 4 seconds.

**Options:**
- A) 22 m/s ✓
- B) 44 m/s
- C) 11 m/s
- D) 2.2 m/s

**Solution:** Using v = u + at = 10 + 3 × 4 = 22 m/s

### Mathematics - Differentiation (Hard)
**Q:** Differentiate using product rule: y = (x²)(3x - 1)

**Answer:** 9x² - 2x

**Solution:** dy/dx = 9x² - 2x

## Educational Applications

1. **Self-Study Practice**: Generate unlimited practice questions
2. **Mock Tests**: Create full-length practice exams
3. **Concept Mastery**: Focus on specific weak topics
4. **Difficulty Progression**: Start easy, gradually increase
5. **Question Banks**: Build institutional question repositories

## Technical Details

### Formula Engine
- Uses **SymPy** for symbolic mathematics
- Ensures mathematical correctness
- Automatic solution verification
- Handles complex algebraic expressions

### Randomization
- Numpy random for numerical values
- Controlled ranges per difficulty
- Ensures non-trivial problems
- Avoids edge cases

### Question Quality
- No duplicate questions in single session
- Diverse parameter values
- Varied question structures
- Balanced difficulty within level

## Contributing

### Option 1: Add Class-Based Generator (Physics/Legacy Math)

1. Create a new generator class in `generators/`
2. Inherit from `QuestionTemplate`
3. Implement `generate()` method
4. Add to CLI mapping

Example:
```python
from question_generator.core.question_engine import Question, QuestionTemplate

class MyNewGenerator(QuestionTemplate):
    def __init__(self):
        super().__init__("Physics", "My Chapter", "My Subtopic")
    
    def generate(self, difficulty="medium", count=1):
        questions = []
        # Your generation logic
        question = Question(
            subject=self.subject,
            chapter=self.chapter,
            subtopic=self.subtopic,
            difficulty=difficulty,
            question_type="mcq",
            question_text="Your question here",
            answer="Answer",
            solution="Solution steps",
            tags=["tag1", "tag2"]
        )
        questions.append(question)
        return questions
```

### Option 2: Add Function-Based Generator (New Math Style)

1. Create a new file in `question_generator/maths/`
2. Write generator functions returning dict-based questions
3. Add to `__init__.py` registry
4. Create wrapper class in CLI

Example:
```python
# question_generator/maths/my_topic.py
import random

def generate_my_topic_questions(difficulty="medium", count=10, question_type="all"):
    questions = []
    for _ in range(count):
        value = random.randint(1, 100)
        question = {
            "question": f"Solve for x: x + {value} = 0",
            "answer": f"x = {-value}",
            "solution": f"x = 0 - {value} = {-value}",
            "difficulty": difficulty,
            "topic": "My Topic",
            "formula": "x + a = 0"
        }
        questions.append(question)
    return questions
```

## 📝 License

This project is for educational purposes. Feel free to use and modify.

## 🐛 Troubleshooting

### Import Errors
```bash
# Ensure you're in the correct directory
cd /home/toji/Python
python main.py
```

### Missing Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Permission Issues
```bash
chmod +x main.py
```

## 🌟 Future Enhancements

- [ ] PDF export with LaTeX formatting
- [ ] Image-based questions (graphs, diagrams)
- [ ] Multi-language support
- [ ] Web interface
- [ ] Database integration
- [ ] Question difficulty AI prediction
- [ ] Adaptive learning paths
- [ ] Performance analytics

## 📧 Support

For issues, questions, or suggestions:
- Review the documentation
- Check existing questions
- Experiment with different parameters

## Acknowledgments

- **DDCET Syllabus**: Gujarat Technological University
- **Inspiration**: JEE Main/Advanced question patterns
- **Libraries**: SymPy, Colorama, Questionary

---

**Version:** 1.0.0  
**Last Updated:** October 2025  
**Platform:** Cross-platform (Linux, macOS, Windows)

Made for DDCET aspirants

