"""
Flask Web Application - Question Generator
Serves 27,000 questions from JSON files
"""

from flask import Flask, render_template, request, jsonify, session, send_from_directory
from flask_cors import CORS
import json
import os
import random
from datetime import datetime

# Import Physics Generators
from question_generator.generators.physics_generators import (
    KinematicsGenerator,
    NewtonLawsGenerator,
    CircularMotionGenerator,
    WorkEnergyGenerator,
    OhmsLawGenerator,
    CapacitanceGenerator,
    HeatTransferGenerator,
    WaveMotionGenerator
)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'
CORS(app)

# Physics Generator Mapping
PHYSICS_GENERATORS = {
    'kinematics': KinematicsGenerator,
    'newton_laws': NewtonLawsGenerator,
    'circular_motion': CircularMotionGenerator,
    'work_energy': WorkEnergyGenerator,
    'ohms_law': OhmsLawGenerator,
    'capacitance': CapacitanceGenerator,
    'heat_transfer': HeatTransferGenerator,
    'wave_motion': WaveMotionGenerator
}

# SEO Routes
@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

# Google Search Console Verification
@app.route('/googlef6777d96df3cbc34.html')
def google_verification():
    return send_from_directory('static', 'googlef6777d96df3cbc34.html')

# Path to question banks
QUESTION_BANKS_DIR = 'question_generator/data/question_banks'

# Available topics organized by subject
TOPICS = {
    'mathematics': {
        'limits': 'Limits',
        'differentiation': 'Differentiation',
        'integration': 'Integration',
        'trigonometry': 'Trigonometry',
        'algebra': 'Algebra',
        'vectors': 'Vectors',
        'coordinate_geometry': 'Coordinate Geometry',
        'matrices': 'Matrices',
        'probability': 'Probability',
        'logarithm': 'Logarithm',
        'statistics': 'Statistics'
    },
    'physics': {
        'kinematics': 'Kinematics',
        'newton_laws': "Newton's Laws",
        'circular_motion': 'Circular Motion',
        'work_energy': 'Work & Energy',
        'ohms_law': "Ohm's Law",
        'capacitance': 'Capacitance',
        'heat_transfer': 'Heat Transfer',
        'wave_motion': 'Wave Motion'
    }
}


def load_questions(topic):
    """Load questions from JSON file"""
    filepath = os.path.join(QUESTION_BANKS_DIR, f'{topic}.json')
    
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('questions', [])
    except Exception as e:
        print(f"Error loading {topic}: {e}")
        return []


def get_total_questions():
    """Get total number of questions across all topics"""
    total = 0
    for topic in TOPICS.keys():
        questions = load_questions(topic)
        total += len(questions)
    return total


@app.route('/')
def index():
    """Main page"""
    total_questions = get_total_questions()
    return render_template('index.html', 
                          total_questions=total_questions,
                          topics=TOPICS)

@app.route('/api/topics/<subject>')
def get_topics(subject):
    """Get topics for a specific subject"""
    if subject in TOPICS:
        return jsonify({'success': True, 'topics': TOPICS[subject]})
    return jsonify({'success': False, 'error': 'Invalid subject'}), 400


@app.route('/api/generate', methods=['POST'])
def generate_questions():
    """Generate/fetch questions based on user selection"""
    data = request.json
    
    topic = data.get('topic')
    count = int(data.get('count', 10))
    
    # Validate count
    if count < 1 or count > 100:
        return jsonify({'error': 'Count must be between 1 and 100'}), 400
    
    # Check if it's a physics topic (use generator) or math topic (use JSON)
    if topic in PHYSICS_GENERATORS:
        # Use Python generator for Physics
        try:
            generator_class = PHYSICS_GENERATORS[topic]
            generator = generator_class()
            
            # Generate questions using the generator
            questions_obj = generator.generate_questions(
                difficulty='medium',
                count=count,
                question_type='all'
            )
            
            # Format response
            questions_formatted = []
            for q in questions_obj:
                questions_formatted.append({
                    'id': len(questions_formatted) + 1,
                    'question': q.question,
                    'answer': q.answer,
                    'solution': q.solution if hasattr(q, 'solution') else f"Apply {q.chapter} principles to solve.",
                    'chapter': q.chapter,
                    'source': 'Physics Generator'
                })
            
        except Exception as e:
            return jsonify({'error': f'Failed to generate physics questions: {str(e)}'}), 500
    
    else:
        # Use JSON for Mathematics
        all_questions = load_questions(topic)
        
        if not all_questions:
            return jsonify({'error': 'No questions available for this topic'}), 404
        
        # Randomly select questions
        if len(all_questions) >= count:
            selected = random.sample(all_questions, count)
        else:
            selected = all_questions
        
        # Format response
        questions_formatted = []
        for q in selected:
            # Get topic name from nested TOPICS dict
            topic_name = None
            for subject in TOPICS.values():
                if topic in subject:
                    topic_name = subject[topic]
                    break
            
            questions_formatted.append({
                'id': q.get('id', 0),
                'question': q.get('question', ''),
                'answer': q.get('answer', ''),
                'solution': q.get('solution', ''),
                'chapter': topic_name or topic,
                'source': q.get('source', 'JEE/GUJCET Pattern')
            })
    
    # Store in session
    if 'generated_questions' not in session:
        session['generated_questions'] = []
    
    session['generated_questions'].extend(questions_formatted)
    session.modified = True
    
    return jsonify({
        'success': True,
        'questions': questions_formatted,
        'count': len(questions_formatted)
    })


@app.route('/api/stats')
def get_stats():
    """Get statistics"""
    stats = {}
    
    for topic_key, topic_name in TOPICS.items():
        questions = load_questions(topic_key)
        stats[topic_name] = len(questions)
    
    return jsonify({
        'total': sum(stats.values()),
        'by_topic': stats
    })


@app.route('/api/clear', methods=['POST'])
def clear_session():
    """Clear generated questions from session"""
    session.pop('generated_questions', None)
    return jsonify({'success': True})


@app.route('/api/export/<format>', methods=['POST'])
def export_questions(format):
    """Export questions in various formats"""
    questions = session.get('generated_questions', [])
    
    if not questions:
        return jsonify({'error': 'No questions to export'}), 400
    
    if format == 'json':
        return jsonify(questions)
    
    elif format == 'text':
        output = []
        output.append("="*70)
        output.append(f"GENERATED QUESTIONS - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        output.append("="*70)
        output.append("")
        
        for i, q in enumerate(questions, 1):
            output.append(f"Question {i}: ({q['chapter']})")
            output.append("-"*70)
            output.append(f"Q: {q['question']}")
            output.append(f"\nAnswer: {q['answer']}")
            output.append(f"\nSolution:\n{q['solution']}")
            output.append("")
            output.append("="*70)
            output.append("")
        
        return '\n'.join(output), 200, {'Content-Type': 'text/plain; charset=utf-8'}
    
    else:
        return jsonify({'error': 'Unsupported format'}), 400


if __name__ == '__main__':
    print("\n" + "="*70)
    print("QUESTION GENERATOR - WEB APPLICATION")
    print("="*70)
    print(f"Total Questions Available: {get_total_questions():,}")
    print("Topics:")
    for key, name in TOPICS.items():
        count = len(load_questions(key))
        print(f"  - {name}: {count:,} questions")
    print("\nStarting server...")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
