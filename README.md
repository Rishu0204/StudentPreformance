# 🎓 EduPredict AI - Student Performance Analysis System

A comprehensive Flask-based web application that uses machine learning and AI to analyze student performance based on environmental factors. The system provides personalized predictions and AI-powered insights to help educators and parents understand how various factors impact student academic success.

## 🌟 Features

### 🤖 AI-Powered Analysis
- **Groq AI Integration**: Real-time AI analysis using the `compound-beta` model
- **Personalized Insights**: Tailored recommendations based on individual student data
- **Comprehensive Analysis**: Covers performance overview, root cause analysis, and actionable recommendations

### 📊 Machine Learning Predictions
- **Multi-Model Ensemble**: Uses Random Forest, Decision Tree, and other algorithms
- **Environmental Factor Analysis**: Considers family background, study habits, health, and social factors
- **Performance Classification**: Categorizes students into different performance levels

### 💬 Interactive AI Assistant
- **Real-time Chatbot**: Available on every page with modal interface
- **Topic-Specific Guidance**: Focuses on environmental factors affecting student performance
- **Beautiful Formatting**: Markdown rendering with proper styling

### 📈 Data Visualization
- **Archive System**: View and analyze historical student data
- **Interactive Tables**: Paginated data display with search functionality
- **CSV Export**: Download data for further analysis

## 🏗️ Architecture

### Backend (Flask)
```python
# Main application structure
app.py              # Flask application with routes and AI integration
config.py           # API key configuration
model.pkl           # Trained machine learning model
```

### Frontend (HTML/CSS/JavaScript)
```
templates/
├── welcome.html    # Landing page with insights
├── analysis.html   # Prediction form and results
└── archive.html    # Data visualization

static/
├── styleWelcome.css    # Landing page styling
├── styleAnalysis.css   # Analysis page styling
└── styleArchive.css    # Archive page styling
```

### AI Integration
```python
# Groq AI Configuration
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

# AI-powered prediction analysis
response = client.chat.completions.create(
    model="compound-beta",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": ai_prompt}
    ],
    max_tokens=600,
    temperature=0.7
)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd StudentPerformance
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Keys**
Create a `config.py` file in the root directory:
```python
import os

# Groq AI API Configuration
GROQ_API_KEY = "your_groq_api_key_here"

# You can also load from environment variable:
# GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'your-default-key-here')
```

5. **Run the application**
```bash
python app.py
```

6. **Access the application**
Open your browser and navigate to: `http://localhost:5001`

## 📋 Requirements

### Core Dependencies
```
Flask==3.1.1
numpy==2.3.2
pandas==2.3.1
scikit-learn==1.7.1
groq==0.4.2
```

### Development Dependencies
```
Werkzeug==3.1.3
Jinja2==3.1.6
MarkupSafe==3.0.2
click==8.2.1
blinker==1.9.0
itsdangerous==2.2.0
```

## 🎯 Usage Guide

### 1. Landing Page (`/`)
- **Overview**: Displays key insights about student performance factors
- **Interactive Elements**: Animated graphs and statistics
- **AI Assistant**: Chatbot available via the floating button

### 2. Analysis Page (`/getanalysis`)
- **Form Input**: Comprehensive student data collection
- **Prediction**: ML-based performance classification
- **AI Analysis**: Detailed, personalized recommendations

#### Form Fields Include:
```html
<!-- Personal Information -->
- Gender, Age, Location
- Family size, Parent status, Guardian

<!-- Educational Background -->
- Mother's/Father's education level
- Previous school performance
- Study time, Past failures

<!-- Lifestyle Factors -->
- Family relationship quality
- Free time, Social activities
- Health status, Internet access
```

### 3. Archive Page (`/archive`)
- **Data Visualization**: Browse historical student records
- **Pagination**: Navigate through large datasets
- **Export**: Download data as CSV

### 4. AI Assistant
Access the chatbot on any page:
```javascript
// Chatbot functionality
document.getElementById('aiBtn').addEventListener('click', function() {
    const chatBox = document.getElementById('chatBox');
    chatBox.style.display = chatBox.style.display === 'none' ? 'flex' : 'none';
});
```

## 🤖 AI Features

### Chatbot Capabilities
The AI assistant specializes in environmental factors affecting student performance:

- **Parents' Education & Involvement**
- **Diet & Nutrition**
- **Mental Health**
- **Social Life**
- **Physical Environment**

### Prediction Analysis
When you submit student data, the AI provides:

1. **Performance Overview** (2-3 sentences)
2. **Root Cause Analysis** (3-4 bullet points)
3. **Detailed Recommendations** (4-5 bullet points)
4. **Action Plan** (immediate, medium, long-term goals)
5. **Encouragement & Motivation** (1-2 sentences)

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set environment variables
export GROQ_API_KEY="your_api_key_here"
export FLASK_ENV="development"
export FLASK_DEBUG=1
```

### API Key Setup
1. Sign up for a Groq AI account at [groq.com](https://groq.com)
2. Get your API key from the dashboard
3. Add it to `config.py` or set as environment variable

## 📊 Machine Learning Model

### Model Architecture
```python
# Model loading and prediction
with gzip.open('model.pkl', 'rb') as f:
    scale, model = pickle.load(f)

# Feature scaling and prediction
scaled_features = scale.transform(features)
predictions = model.predict(scaled_features)
```

### Features Used
- **Personal**: Age, gender, location
- **Family**: Parent education, family size, relationship quality
- **Academic**: Study time, past failures, school support
- **Lifestyle**: Health, social activities, free time

## 🎨 UI/UX Features

### Responsive Design
- **Mobile-friendly**: Optimized for all screen sizes
- **Modern Interface**: Gradient backgrounds and glassmorphism effects
- **Smooth Animations**: CSS transitions and hover effects

### Chat Interface
```css
/* Chat window styling */
.chat-box {
    width: 450px;
    height: 600px;
    background: linear-gradient(135deg, rgba(15, 20, 25, 0.95), rgba(26, 32, 44, 0.95));
    backdrop-filter: blur(20px);
    border-radius: 20px;
}
```

### Markdown Rendering
```javascript
// Client-side markdown parsing
let formattedResponse = data.response
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>')
    .replace(/^\s*[-*]\s+/gm, '• ');
```

## 🚨 Troubleshooting

### Common Issues

1. **Import Error for API Key**
```bash
# Ensure config.py exists and contains:
GROQ_API_KEY = "your_actual_api_key"
```

2. **Model Loading Warnings**
```bash
# These warnings are normal and don't affect functionality:
# InconsistentVersionWarning: Trying to unpickle estimator...
```

3. **Port Already in Use**
```bash
# Change port in app.py
if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Use different port
```

### Debug Mode
```bash
# Enable debug mode for development
export FLASK_DEBUG=1
python app.py
```

## 📈 Performance Metrics

### Model Accuracy
- **Multi-output Regression**: Predicts multiple performance indicators
- **Ensemble Methods**: Combines multiple algorithms for better accuracy
- **Feature Engineering**: Optimized feature selection and scaling

### Response Times
- **AI Analysis**: ~2-3 seconds for comprehensive analysis
- **Chatbot**: ~1-2 seconds for responses
- **ML Prediction**: <1 second for model inference

## 🔒 Security Considerations

### API Key Management
- **Environment Variables**: Use for production deployments
- **Config File**: Development convenience
- **Never Commit Keys**: Keep API keys out of version control

### Data Privacy
- **Local Processing**: All ML predictions happen locally
- **No Data Storage**: Form data is not permanently stored
- **Secure Transmission**: HTTPS recommended for production

## 🛠️ Development

### Project Structure
```
StudentPerformance/
├── app.py                 # Main Flask application
├── config.py              # Configuration and API keys
├── model.pkl              # Trained ML model
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── welcome.html
│   ├── analysis.html
│   └── archive.html
├── static/                # CSS and static files
│   ├── styleWelcome.css
│   ├── styleAnalysis.css
│   └── styleArchive.css
└── model_training/        # Training data
    ├── student_data.csv
    └── model.ipynb
```

### Adding New Features
1. **Backend**: Add routes in `app.py`
2. **Frontend**: Create templates in `templates/`
3. **Styling**: Add CSS in `static/`
4. **AI Integration**: Extend the system prompt in `app.py`



## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 🎉 Acknowledgments

- **Groq AI** for providing the AI capabilities
- **Scikit-learn** for machine learning tools
- **Flask** for the web framework
- **Open Source Community** for various libraries and tools

---

