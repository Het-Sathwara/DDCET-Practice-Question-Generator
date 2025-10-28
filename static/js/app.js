// Question Generator - Frontend JavaScript

let sessionQuestions = [];

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
    hideResults();
    
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
            sessionQuestions = sessionQuestions.concat(data.questions);
            displayQuestions(data.questions);
            updateSessionCount();
            showStats();
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
                    <span class="meta-badge">Q ${sessionQuestions.length - questions.length + index + 1}</span>
                    <span class="meta-badge">${q.chapter}</span>
                    <span class="meta-badge">${q.source}</span>
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
    
    questionsDiv.innerHTML += html;
    resultsDiv.style.display = 'block';
}

// Clear questions
function clearQuestions() {
    if (confirm('Clear all generated questions?')) {
        sessionQuestions = [];
        document.getElementById('questions-list').innerHTML = '';
        document.getElementById('results').style.display = 'none';
        document.getElementById('statistics').style.display = 'none';
        updateSessionCount();
        
        fetch('/api/clear', { method: 'POST' });
    }
}

// Update session count
function updateSessionCount() {
    document.getElementById('session-count').textContent = sessionQuestions.length;
}

// Show/hide loading
function showLoading(show) {
    const loading = document.getElementById('loading');
    if (show) {
        loading.style.display = 'block';
        loading.textContent = '⏳ Fetching questions from database...';
    } else {
        loading.style.display = 'none';
    }
}

// Hide results
function hideResults() {
    // Don't hide, just scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Show statistics
async function showStats() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();
        
        const statsDiv = document.getElementById('statistics');
        const statsContent = document.getElementById('stats-content');
        
        let html = `
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>${data.total.toLocaleString()}</h3>
                    <p>Total Questions</p>
                </div>
                <div class="stat-card">
                    <h3>${sessionQuestions.length}</h3>
                    <p>Generated</p>
                </div>
            </div>
            
            <div class="stat-breakdown">
                <h3>Available by Topic:</h3>
                ${Object.entries(data.by_topic).map(([topic, count]) => `
                    <div class="stat-item">
                        <span>${topic}</span>
                        <span><strong>${count.toLocaleString()}</strong> questions</span>
                    </div>
                `).join('')}
            </div>
        `;
        
        statsContent.innerHTML = html;
        statsDiv.style.display = 'block';
    } catch (error) {
        console.error('Error fetching stats:', error);
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

// Load stats on page load
window.addEventListener('load', () => {
    showStats();
});
