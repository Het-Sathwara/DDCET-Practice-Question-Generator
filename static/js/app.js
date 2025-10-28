// Question Generator - Frontend JavaScript

let sessionQuestions = [];

// Subject change handler
document.getElementById('subject').addEventListener('change', async (e) => {
    const subject = e.target.value;
    const topicSelect = document.getElementById('topic');
    
    if (!subject) {
        topicSelect.disabled = true;
        topicSelect.innerHTML = '<option value="">-- Select subject first --</option>';
        return;
    }
    
    try {
        const response = await fetch(`/api/topics/${subject}`);
        const data = await response.json();
        
        if (data.success) {
            topicSelect.disabled = false;
            topicSelect.innerHTML = '<option value="">-- Choose a topic --</option>';
            
            Object.entries(data.topics).forEach(([key, name]) => {
                const option = document.createElement('option');
                option.value = key;
                option.textContent = name;
                topicSelect.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading topics:', error);
        alert('Failed to load topics');
    }
});

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
            // CLEAR previous questions (replace, don't append)
            sessionQuestions = data.questions;
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
    
    // REPLACE content (not append)
    questionsDiv.innerHTML = html;
    resultsDiv.style.display = 'block';
}

// Clear questions
function clearQuestions() {
    if (confirm('Clear all generated questions?')) {
        sessionQuestions = [];
        document.getElementById('questions-list').innerHTML = '';
        document.getElementById('results').style.display = 'none';
        
        fetch('/api/clear', { method: 'POST' });
    }
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

// Export questions
async function exportQuestions(format) {
    if (sessionQuestions.length === 0) {
        alert('No questions to export!');
        return;
    }
    
    try {
        const response = await fetch(`/api/export/${format}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (format === 'json') {
            const data = await response.json();
            const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
            downloadFile(blob, `questions_${Date.now()}.json`);
        } else if (format === 'text') {
            const text = await response.text();
            const blob = new Blob([text], { type: 'text/plain' });
            downloadFile(blob, `questions_${Date.now()}.txt`);
        }
    } catch (error) {
        console.error('Export error:', error);
        alert('Failed to export questions');
    }
}

// Download file helper
function downloadFile(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
