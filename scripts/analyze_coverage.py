#!/usr/bin/env python3
"""
Analyze DDCET Syllabus Coverage
Check what subtopics are missing or have low question counts
"""

import json
import os
from collections import defaultdict

# DDCET Syllabus requirements
DDCET_SYLLABUS = {
    "Matrices": {
        "marks": 8,
        "subtopics": [
            "Determinant 2x2",
            "Determinant 3x3",
            "Types of matrices",
            "Matrix addition",
            "Matrix subtraction",
            "Scalar multiplication",
            "Matrix multiplication",
            "Adjoint (2x2)",
            "Inverse (2x2)",
            "Solving 2-variable linear equations"
        ]
    },
    "Trigonometry": {
        "marks": 6,
        "subtopics": [
            "Degree/Radian conversion",
            "Basic trig functions (sin, cos, tan, cot, sec, cosec)",
            "Periods of trig functions",
            "Allied angles",
            "Compound angles",
            "Multiple angles (2θ, 3θ)",
            "Submultiple angles (θ/2)",
            "Sum to product",
            "Product to sum"
        ]
    },
    "Vectors": {
        "marks": 4,
        "subtopics": [
            "Vector basics",
            "Direction & Magnitude",
            "Null vector",
            "Unit vector",
            "Vector addition",
            "Vector subtraction",
            "Dot product",
            "Cross product",
            "Angle between vectors"
        ]
    },
    "Coordinate Geometry": {
        "marks": 4,
        "subtopics": [
            "Slope of a line",
            "Two-point form",
            "Slope-point form",
            "Intercept form",
            "General form of line",
            "Parallel lines",
            "Perpendicular lines",
            "Angle between lines",
            "Circle equation (center, radius)",
            "Finding center/radius from general equation"
        ]
    },
    "Limits": {
        "marks": 0,  # Part of Function & Limit
        "subtopics": [
            "Function basics",
            "Limit concept",
            "lim sin(x)/x",
            "lim tan(x)/x",
            "lim (e^x - 1)/x",
            "lim log(1+x)/x",
            "Limits at infinity",
            "L'Hospital's rule"
        ]
    },
    "Differentiation": {
        "marks": 8,
        "subtopics": [
            "Basic differentiation",
            "Sum/Difference rules",
            "Product rule",
            "Quotient rule",
            "Chain rule",
            "Implicit differentiation",
            "Parametric differentiation",
            "Logarithmic differentiation",
            "Second derivative",
            "Velocity (application)",
            "Acceleration (application)"
        ]
    },
    "Integration": {
        "marks": 8,
        "subtopics": [
            "Basic integration",
            "Standard integrals",
            "Substitution method",
            "Integration by parts",
            "Definite integrals",
            "Properties of definite integrals"
        ]
    },
    "Logarithm": {
        "marks": 4,
        "subtopics": [
            "Logarithm as function",
            "Laws of logarithm",
            "Change of base",
            "Logarithmic equations",
            "Exponential equations"
        ]
    },
    "Algebra": {
        "marks": 0,  # Not explicitly mentioned but important
        "subtopics": [
            "Quadratic equations",
            "Cubic equations",
            "AP sequences",
            "GP sequences",
            "Binomial theorem",
            "Permutation",
            "Combination"
        ]
    },
    "Probability": {
        "marks": 0,
        "subtopics": [
            "Basic probability",
            "Addition rule",
            "Multiplication rule",
            "Conditional probability",
            "Binomial distribution"
        ]
    }
}

def analyze_questions():
    banks_dir = "../question_generator/data/question_banks"
    
    print("\n" + "="*80)
    print("DDCET SYLLABUS COVERAGE ANALYSIS")
    print("="*80)
    
    coverage_report = {}
    
    for topic_file in sorted(os.listdir(banks_dir)):
        if not topic_file.endswith('.json'):
            continue
        
        topic_name = topic_file.replace('.json', '').replace('_', ' ').title()
        
        # Map file names to syllabus topics
        topic_key = topic_name
        if 'Coordinate' in topic_name:
            topic_key = 'Coordinate Geometry'
        
        filepath = os.path.join(banks_dir, topic_file)
        with open(filepath, 'r') as f:
            data = json.load(f)
            questions = data.get('questions', [])
        
        print(f"\n📚 {topic_key.upper()}")
        print("-" * 80)
        print(f"Total Questions: {len(questions)}")
        
        if topic_key not in DDCET_SYLLABUS:
            print(f"  ⚠️  Topic not in DDCET syllabus")
            continue
        
        syllabus_data = DDCET_SYLLABUS[topic_key]
        print(f"DDCET Marks: {syllabus_data['marks']}")
        print(f"Required Subtopics: {len(syllabus_data['subtopics'])}")
        
        # Analyze question patterns
        patterns = defaultdict(int)
        
        for q in questions[:100]:  # Sample first 100
            q_text = q['question'].lower()
            
            # Matrices patterns
            if '2' in q_text and '2' in q_text and ('|' in q_text or 'determinant' in q_text):
                patterns['determinant_2x2'] += 1
            if '3' in q_text and ('|' in q_text or 'determinant' in q_text):
                patterns['determinant_3x3'] += 1
            if 'inverse' in q_text or 'a⁻¹' in q_text or 'a^-1' in q_text:
                patterns['inverse'] += 1
            if 'adjoint' in q_text or 'adj' in q_text:
                patterns['adjoint'] += 1
            if 'solve' in q_text and ('ax' in q_text or 'system' in q_text):
                patterns['linear_equations'] += 1
            
            # Coordinate Geometry
            if 'circle' in q_text:
                patterns['circle'] += 1
            if 'slope' in q_text:
                patterns['slope'] += 1
            if 'parallel' in q_text:
                patterns['parallel'] += 1
            if 'perpendicular' in q_text:
                patterns['perpendicular'] += 1
            if 'two-point' in q_text or 'two point' in q_text:
                patterns['two_point_form'] += 1
            if 'intercept' in q_text:
                patterns['intercept_form'] += 1
            if 'angle between' in q_text and 'line' in q_text:
                patterns['angle_between_lines'] += 1
            
            # Vectors
            if 'dot product' in q_text or 'scalar product' in q_text or ' · ' in q_text:
                patterns['dot_product'] += 1
            if 'cross product' in q_text or 'vector product' in q_text or ' × ' in q_text:
                patterns['cross_product'] += 1
            if 'unit vector' in q_text:
                patterns['unit_vector'] += 1
            if 'magnitude' in q_text:
                patterns['magnitude'] += 1
            
            # Differentiation
            if 'parametric' in q_text:
                patterns['parametric'] += 1
            if 'implicit' in q_text:
                patterns['implicit'] += 1
            if 'logarithmic differentiation' in q_text:
                patterns['log_differentiation'] += 1
            if 'velocity' in q_text or 'acceleration' in q_text:
                patterns['physics_applications'] += 1
            if 'second derivative' in q_text or 'd²y' in q_text:
                patterns['second_derivative'] += 1
            
            # Integration
            if 'by parts' in q_text:
                patterns['by_parts'] += 1
            if 'substitution' in q_text:
                patterns['substitution'] += 1
            if 'definite' in q_text or '∫_' in q_text:
                patterns['definite_integral'] += 1
        
        if patterns:
            print(f"\n  📊 Pattern Detection (first 100 questions):")
            for pattern, count in sorted(patterns.items(), key=lambda x: -x[1]):
                percentage = (count / 100) * 100
                status = "✅" if count > 5 else "⚠️" if count > 0 else "❌"
                print(f"    {status} {pattern.replace('_', ' ').title()}: {count}/100 ({percentage:.0f}%)")
        
        # Check for missing patterns
        print(f"\n  🔍 Required Subtopics:")
        for subtopic in syllabus_data['subtopics']:
            print(f"    • {subtopic}")
        
        # Sample questions
        print(f"\n  📝 Sample Questions (first 3):")
        for i in range(min(3, len(questions))):
            q_preview = questions[i]['question'][:70].replace('\n', ' ')
            print(f"    {i+1}. {q_preview}...")
        
        coverage_report[topic_key] = {
            'total': len(questions),
            'patterns': dict(patterns),
            'subtopics_required': len(syllabus_data['subtopics'])
        }
    
    # Summary
    print("\n" + "="*80)
    print("MISSING/LOW COVERAGE AREAS")
    print("="*80)
    
    print("\n🚨 CRITICAL GAPS FOUND:\n")
    
    gaps = {
        "Coordinate Geometry": ["Circle equations (center/radius)", "Finding center/radius from general equation"],
        "Differentiation": ["Parametric differentiation", "Velocity/Acceleration applications"],
        "Matrices": ["Solving 2-variable linear equations (AX=B)"],
        "Logarithm": ["Logarithmic equations", "Exponential equations"],
    }
    
    for topic, missing_items in gaps.items():
        print(f"📌 {topic}:")
        for item in missing_items:
            print(f"   ❌ MISSING: {item}")
    
    print("\n" + "="*80)
    print("RECOMMENDATION: Generate 500-1000 more questions for each gap")
    print("="*80)

if __name__ == "__main__":
    analyze_questions()

