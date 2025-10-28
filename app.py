"""
Flask Web Application for DDCET Question Generator
Mobile-responsive web interface with all CLI features
"""

from flask import Flask, render_template, request, jsonify, send_file, session
from flask_cors import CORS
import os
import json
from datetime import datetime
import secrets

# Import generators
from question_generator.generators.physics_generators import (
    KinematicsGenerator, NewtonLawsGenerator, CircularMotionGenerator,
    WorkEnergyGenerator, OhmsLawGenerator, CapacitanceGenerator,
    HeatTransferGenerator, WaveMotionGenerator
)
from question_generator.generators.math_generators import (
    MatricesGenerator, LogarithmGenerator, StatisticsGenerator
)
from question_generator.maths import (
    generate_trigonometric_questions,
    generate_vector_questions,
    generate_coordinate_geometry_questions,
    generate_limit_questions,
    generate_differentiation_questions,
    generate_integration_questions
)
from question_generator.utils.export_utils import QuestionExporter

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)

# Initialize generators
PHYSICS_GENERATORS = {
    "Kinematics": KinematicsGenerator,
    "Newton's Laws": NewtonLawsGenerator,
    "Circular Motion": CircularMotionGenerator,
    "Work & Energy": WorkEnergyGenerator,
    "Ohm's Law": OhmsLawGenerator,
    "Capacitance": CapacitanceGenerator,
    "Heat & Thermometry": HeatTransferGenerator,
    "Wave Motion": WaveMotionGenerator
}

MATH_GENERATORS_CLASS = {
    "Matrices & Determinants": MatricesGenerator,
    "Logarithm": LogarithmGenerator,
    "Statistics": StatisticsGenerator
}

MATH_GENERATORS_FUNC = {
    "Trigonometry (50+ formulas)": ("trigonometry", generate_trigonometric_questions),
    "Limits (14+ formulas)": ("limits", generate_limit_questions),
    "Differentiation (20+ formulas)": ("differentiation", generate_differentiation_questions),
    "Integration (20+ formulas)": ("integration", generate_integration_questions),
    "Vectors": ("vectors", generate_vector_questions),
    "Coordinate Geometry": ("coordinate_geometry", generate_coordinate_geometry_questions)
}

# Session storage for generated questions
def get_session_questions():
    if 'questions' not in session:
        session['questions'] = []
    return session['questions']

def add_to_session(questions):
    current = get_session_questions()
    current.extend(questions)
    session['questions'] = current
    session.modified = True

def clear_session():
    session['questions'] = []
    session.modified = True

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')

@app.route('/api/generators')
def get_generators():
    """Get list of all available generators"""
    physics = list(PHYSICS_GENERATORS.keys())
    math_class = list(MATH_GENERATORS_CLASS.keys())
    math_func = list(MATH_GENERATORS_FUNC.keys())
    
    return jsonify({
        "physics": physics,
        "mathematics": math_class + math_func
    })

@app.route('/api/generate', methods=['POST'])
def generate_questions():
    """Generate questions based on parameters"""
    try:
        data = request.json
        subject = data.get('subject')
        topic = data.get('topic')
        difficulty = data.get('difficulty', 'medium')
        count = int(data.get('count', 10))
        question_type = data.get('question_type', 'all')
        
        questions = []
        
        if subject == 'Physics':
            if topic in PHYSICS_GENERATORS:
                generator = PHYSICS_GENERATORS[topic]()
                q_objects = generator.generate(difficulty=difficulty, count=count)
                # Convert Question objects to dicts
                questions = [
                    {
                        'subject': q.subject,
                        'chapter': q.chapter,
                        'subtopic': q.subtopic,
                        'difficulty': q.difficulty,
                        'question_type': q.question_type,
                        'question': q.question_text,
                        'answer': str(q.answer),
                        'options': q.options if hasattr(q, 'options') else None,
                        'solution': q.solution,
                        'tags': q.tags
                    }
                    for q in q_objects
                ]
        
        elif subject == 'Mathematics':
            if topic in MATH_GENERATORS_CLASS:
                generator = MATH_GENERATORS_CLASS[topic]()
                q_objects = generator.generate(difficulty=difficulty, count=count)
                # Convert Question objects to dicts
                questions = [
                    {
                        'subject': q.subject,
                        'chapter': q.chapter,
                        'subtopic': q.subtopic,
                        'difficulty': q.difficulty,
                        'question_type': q.question_type,
                        'question': q.question_text,
                        'answer': str(q.answer),
                        'options': q.options if hasattr(q, 'options') else None,
                        'solution': q.solution,
                        'tags': q.tags
                    }
                    for q in q_objects
                ]
            
            elif topic in MATH_GENERATORS_FUNC:
                func_name, func = MATH_GENERATORS_FUNC[topic]
                questions = func(difficulty=difficulty, count=count, question_type=question_type)
        
        # Add to session
        add_to_session(questions)
        
        return jsonify({
            'success': True,
            'count': len(questions),
            'questions': questions,
            'total_in_session': len(get_session_questions())
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/questions')
def get_all_questions():
    """Get all questions in current session"""
    questions = get_session_questions()
    return jsonify({
        'count': len(questions),
        'questions': questions
    })

@app.route('/api/statistics')
def get_statistics():
    """Get statistics about generated questions"""
    questions = get_session_questions()
    
    if not questions:
        return jsonify({
            'total': 0,
            'by_subject': {},
            'by_difficulty': {},
            'by_type': {}
        })
    
    stats = {
        'total': len(questions),
        'by_subject': {},
        'by_difficulty': {},
        'by_type': {}
    }
    
    for q in questions:
        # By subject
        subject = q.get('subject', 'Unknown')
        stats['by_subject'][subject] = stats['by_subject'].get(subject, 0) + 1
        
        # By difficulty
        difficulty = q.get('difficulty', 'unknown')
        stats['by_difficulty'][difficulty] = stats['by_difficulty'].get(difficulty, 0) + 1
        
        # By type
        q_type = q.get('question_type', 'unknown')
        stats['by_type'][q_type] = stats['by_type'].get(q_type, 0) + 1
    
    return jsonify(stats)

@app.route('/api/export/<format>')
def export_questions(format):
    """Export questions to specified format"""
    try:
        questions = get_session_questions()
        
        if not questions:
            return jsonify({
                'success': False,
                'error': 'No questions to export'
            }), 400
        
        exporter = QuestionExporter()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create export directory if it doesn't exist
        export_dir = "generated_questions"
        os.makedirs(export_dir, exist_ok=True)
        
        if format == 'json':
            filename = f"questions_web_{timestamp}.json"
            filepath = os.path.join(export_dir, filename)
            with open(filepath, 'w') as f:
                json.dump(questions, f, indent=2)
            return send_file(filepath, as_attachment=True, download_name=filename)
        
        elif format == 'csv':
            # Convert dicts to Question-like objects for exporter
            from question_generator.core.question_engine import Question
            q_objects = []
            for q in questions:
                q_obj = Question(
                    subject=q.get('subject', ''),
                    chapter=q.get('chapter', ''),
                    subtopic=q.get('subtopic', ''),
                    difficulty=q.get('difficulty', ''),
                    question_type=q.get('question_type', ''),
                    question_text=q.get('question', ''),
                    answer=q.get('answer', ''),
                    solution=q.get('solution', ''),
                    tags=q.get('tags', [])
                )
                q_objects.append(q_obj)
            
            filepath = exporter.export_to_csv(q_objects, f"questions_web_{timestamp}.csv")
            return send_file(filepath, as_attachment=True)
        
        elif format == 'txt':
            filename = f"questions_web_{timestamp}.txt"
            filepath = os.path.join(export_dir, filename)
            with open(filepath, 'w') as f:
                f.write("=" * 80 + "\n")
                f.write("DDCET QUESTION GENERATOR - EXPORTED QUESTIONS\n")
                f.write("=" * 80 + "\n\n")
                
                for i, q in enumerate(questions, 1):
                    f.write(f"Question {i}:\n")
                    f.write(f"Subject: {q.get('subject', 'N/A')}\n")
                    f.write(f"Topic: {q.get('chapter', 'N/A')} - {q.get('subtopic', 'N/A')}\n")
                    f.write(f"Difficulty: {q.get('difficulty', 'N/A')}\n")
                    f.write(f"Type: {q.get('question_type', 'N/A')}\n\n")
                    f.write(f"Q: {q.get('question', '')}\n")
                    
                    if q.get('options'):
                        f.write(f"Options: {', '.join(q['options'])}\n")
                    
                    f.write(f"Answer: {q.get('answer', '')}\n")
                    f.write(f"Solution: {q.get('solution', '')}\n")
                    f.write("\n" + "-" * 80 + "\n\n")
            
            return send_file(filepath, as_attachment=True, download_name=filename)
        
        else:
            return jsonify({
                'success': False,
                'error': 'Invalid format'
            }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/clear', methods=['POST'])
def clear_questions():
    """Clear all questions from session"""
    clear_session()
    return jsonify({
        'success': True,
        'message': 'All questions cleared'
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'generators': {
            'physics': len(PHYSICS_GENERATORS),
            'mathematics': len(MATH_GENERATORS_CLASS) + len(MATH_GENERATORS_FUNC)
        }
    })

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('generated_questions', exist_ok=True)
    
    # Run the app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

