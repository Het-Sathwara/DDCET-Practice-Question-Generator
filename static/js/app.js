// Question Generator - Frontend JavaScript

// Form submission
document.getElementById('question-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const topic = document.getElementById('topic').value;
    const count = document.getElementById('count').value;
    
    if (!topic) {
        alert('Please select a topic!');
        return;
    }
    
    // Show loading
    showLoading(true);
    
    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ topic, count })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // REPLACE old questions with new ones
            displayQuestions(data.questions);
        } else {
            alert(data.error || 'Failed to generate questions');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate questions. Please try again.');
    } finally {
        showLoading(false);
    }
});

// Display questions
function displayQuestions(questions) {
    const resultsDiv = document.getElementById('results');
    const questionsDiv = document.getElementById('questions-list');
    
    let html = '';
    
    questions.forEach((q, index) => {
        html += `
            <div class="question-item">
                <div class="question-meta">
                    <span class="meta-badge">Q ${index + 1}</span>
                    <span class="meta-badge">${q.chapter}</span>
                </div>
                
                <div class="question-text">
                    ${q.question}
                </div>
                
                <div class="answer-box">
                    <strong>Answer:</strong> ${q.answer}
                </div>
                
                <div class="solution-box">
                    <strong>Solution:</strong><br>
                    ${q.solution}
                </div>
            </div>
        `;
    });
    
    // REPLACE content instead of append
    questionsDiv.innerHTML = html;
    resultsDiv.style.display = 'block';
    
    // Scroll to top to show new questions
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Show/hide loading
function showLoading(show) {
    const loading = document.getElementById('loading');
    if (show) {
        loading.style.display = 'block';
        loading.textContent = 'Loading questions...';
    } else {
        loading.style.display = 'none';
    }
}
