// Global state
let generators = { physics: [], mathematics: [] };

// Load generators on page load
document.addEventListener('DOMContentLoaded', () => {
    loadGenerators();
    updateSessionCount();
    setupEventListeners();
});

// Setup event listeners
function setupEventListeners() {
    const subjectSelect = document.getElementById('subject');
    const topicSelect = document.getElementById('topic');
    const generateForm = document.getElementById('generateForm');

    subjectSelect.addEventListener('change', handleSubjectChange);
    generateForm.addEventListener('submit', handleGenerate);
}

// Load available generators from API
async function loadGenerators() {
    try {
        const response = await fetch('/api/generators');
        const data = await response.json();
        generators = data;
    } catch (error) {
        console.error('Error loading generators:', error);
        showAlert('Failed to load generators', 'error');
    }
}

// Handle subject change
function handleSubjectChange(event) {
    const subject = event.target.value;
    const topicSelect = document.getElementById('topic');
    
    topicSelect.innerHTML = '<option value="">Select topic</option>';
    
    if (subject && generators[subject.toLowerCase()]) {
        topicSelect.disabled = false;
        const topics = generators[subject.toLowerCase()];
        
        topics.forEach(topic => {
            const option = document.createElement('option');
            option.value = topic;
            option.textContent = topic;
            topicSelect.appendChild(option);
        });
    } else {
        topicSelect.disabled = true;
    }
}

// Handle form submission
async function handleGenerate(event) {
    event.preventDefault();
    
    const formData = {
        subject: document.getElementById('subject').value,
        topic: document.getElementById('topic').value,
        difficulty: document.getElementById('difficulty').value,
        count: document.getElementById('count').value,
        question_type: document.getElementById('questionType').value
    };
    
    showLoading(true);
    hideResults();
    
    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayQuestions(data.questions);
            updateSessionCount(data.total_in_session);
            showActions();
            showAlert(`Successfully generated ${data.count} questions!`, 'success');
        } else {
            showAlert(data.error || 'Failed to generate questions', 'error');
        }
    } catch (error) {
        console.error('Error generating questions:', error);
        showAlert('An error occurred while generating questions', 'error');
    } finally {
        showLoading(false);
    }
}

// Display questions
function displayQuestions(questions) {
    const resultsSection = document.getElementById('results');
    const questionsList = document.getElementById('questionsList');
    
    questionsList.innerHTML = '';
    
    questions.forEach((q, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question-item';
        
        let optionsHTML = '';
        if (q.options && q.options.length > 0) {
            optionsHTML = `
                <div class="question-options">
                    <strong>Options:</strong>
                    <ul>
                        ${q.options.map(opt => `<li>${opt}</li>`).join('')}
                    </ul>
                </div>
            `;
        }
        
        questionDiv.innerHTML = `
            <h3>Question ${index + 1}</h3>
            <div class="question-meta">
                <span class="meta-badge">${q.subject} - ${q.chapter || q.subtopic}</span>
                <span class="meta-badge difficulty">${q.difficulty}</span>
                <span class="meta-badge type">${q.question_type}</span>
            </div>
            <div class="question-text">
                <strong>Q:</strong> ${q.question}
            </div>
            ${optionsHTML}
            <div class="answer-box">
                <strong>Answer:</strong> ${q.answer}
            </div>
            <div class="solution-box">
                <strong>Solution:</strong> ${q.solution || 'N/A'}
            </div>
        `;
        
        questionsList.appendChild(questionDiv);
    });
    
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// View all questions in session
async function viewAllQuestions() {
    showLoading(true);
    
    try {
        const response = await fetch('/api/questions');
        const data = await response.json();
        
        if (data.count > 0) {
            displayQuestions(data.questions);
            showAlert(`Displaying all ${data.count} questions in session`, 'info');
        } else {
            showAlert('No questions in session', 'info');
        }
    } catch (error) {
        console.error('Error fetching questions:', error);
        showAlert('Failed to fetch questions', 'error');
    } finally {
        showLoading(false);
    }
}

// Show statistics
async function showStatistics() {
    showLoading(true);
    
    try {
        const response = await fetch('/api/statistics');
        const stats = await response.json();
        
        const statsSection = document.getElementById('statistics');
        const statsContent = document.getElementById('statsContent');
        
        if (stats.total === 0) {
            statsContent.innerHTML = '<p>No statistics available. Generate some questions first!</p>';
        } else {
            statsContent.innerHTML = `
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>${stats.total}</h3>
                        <p>Total Questions</p>
                    </div>
                    <div class="stat-card">
                        <h3>${Object.keys(stats.by_subject).length}</h3>
                        <p>Subjects</p>
                    </div>
                    <div class="stat-card">
                        <h3>${Object.keys(stats.by_difficulty).length}</h3>
                        <p>Difficulty Levels</p>
                    </div>
                </div>
                
                <div class="stat-breakdown">
                    <h3>By Subject</h3>
                    ${Object.entries(stats.by_subject).map(([key, val]) => `
                        <div class="stat-item">
                            <span>${key}</span>
                            <strong>${val}</strong>
                        </div>
                    `).join('')}
                </div>
                
                <div class="stat-breakdown">
                    <h3>By Difficulty</h3>
                    ${Object.entries(stats.by_difficulty).map(([key, val]) => `
                        <div class="stat-item">
                            <span>${key}</span>
                            <strong>${val}</strong>
                        </div>
                    `).join('')}
                </div>
                
                <div class="stat-breakdown">
                    <h3>By Type</h3>
                    ${Object.entries(stats.by_type).map(([key, val]) => `
                        <div class="stat-item">
                            <span>${key}</span>
                            <strong>${val}</strong>
                        </div>
                    `).join('')}
                </div>
            `;
        }
        
        statsSection.style.display = 'block';
        statsSection.scrollIntoView({ behavior: 'smooth' });
    } catch (error) {
        console.error('Error fetching statistics:', error);
        showAlert('Failed to fetch statistics', 'error');
    } finally {
        showLoading(false);
    }
}

// Export questions
async function exportQuestions(format) {
    showLoading(true);
    
    try {
        const response = await fetch(`/api/export/${format}`);
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Export failed');
        }
        
        // Create download
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `questions_${Date.now()}.${format}`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
        showAlert(`Successfully exported to ${format.toUpperCase()}!`, 'success');
    } catch (error) {
        console.error('Error exporting:', error);
        showAlert(error.message || 'Failed to export questions', 'error');
    } finally {
        showLoading(false);
    }
}

// Clear all questions
async function clearQuestions() {
    if (!confirm('Are you sure you want to clear all questions? This cannot be undone.')) {
        return;
    }
    
    try {
        const response = await fetch('/api/clear', {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (data.success) {
            hideResults();
            hideStatistics();
            hideActions();
            updateSessionCount(0);
            showAlert('All questions cleared!', 'success');
        }
    } catch (error) {
        console.error('Error clearing questions:', error);
        showAlert('Failed to clear questions', 'error');
    }
}

// Update session count
async function updateSessionCount(count) {
    if (count === undefined) {
        try {
            const response = await fetch('/api/questions');
            const data = await response.json();
            count = data.count;
        } catch (error) {
            count = 0;
        }
    }
    
    document.getElementById('sessionCount').textContent = count;
    
    if (count > 0) {
        showActions();
    }
}

// UI Helper Functions
function showLoading(show) {
    document.getElementById('loading').style.display = show ? 'block' : 'none';
}

function hideResults() {
    document.getElementById('results').style.display = 'none';
}

function hideStatistics() {
    document.getElementById('statistics').style.display = 'none';
}

function showActions() {
    document.getElementById('actions').style.display = 'flex';
}

function hideActions() {
    document.getElementById('actions').style.display = 'none';
}

function showAlert(message, type) {
    // Remove existing alerts
    const existingAlerts = document.querySelectorAll('.alert');
    existingAlerts.forEach(alert => alert.remove());
    
    // Create new alert
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    // Insert at the top of main content
    const main = document.querySelector('main');
    main.insertBefore(alert, main.firstChild);
    
    // Scroll to alert
    alert.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        alert.remove();
    }, 5000);
}

