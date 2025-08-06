from flask import Flask, render_template, request, send_file, jsonify
import numpy as np
import gzip
import pickle
import pandas as pd
import os
from math import ceil
from groq import Groq
from config import GROQ_API_KEY
import re
from markupsafe import Markup
with gzip.open('model.pkl', 'rb') as f:
    scale, model = pickle.load(f)

app=Flask(__name__)

def markdown_to_html(text):
    """Convert basic markdown text to HTML with safe rendering"""
    if not text:
        return ""
    
    # Split text into paragraphs for better processing
    paragraphs = text.split('\n\n')
    processed_paragraphs = []
    
    for paragraph in paragraphs:
        if not paragraph.strip():
            continue
            
        # Convert headers
        paragraph = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', paragraph, flags=re.MULTILINE)
        paragraph = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', paragraph, flags=re.MULTILINE)
        paragraph = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', paragraph, flags=re.MULTILINE)
        
        # Convert bold and italic text
        paragraph = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', paragraph)
        paragraph = re.sub(r'\*(.*?)\*', r'<em>\1</em>', paragraph)
        
        # Check if this paragraph contains list items
        lines = paragraph.split('\n')
        list_lines = []
        non_list_lines = []
        
        for line in lines:
            if re.match(r'^- ', line):
                list_lines.append(re.sub(r'^- (.*)', r'<li>\1</li>', line))
            elif re.match(r'^\d+\. ', line):
                list_lines.append(re.sub(r'^\d+\. (.*)', r'<li>\1</li>', line))
            else:
                if list_lines:
                    # Close the current list
                    non_list_lines.append(f'<ul>{"".join(list_lines)}</ul>')
                    list_lines = []
                non_list_lines.append(line)
        
        # Handle any remaining list items
        if list_lines:
            non_list_lines.append(f'<ul>{"".join(list_lines)}</ul>')
        
        # Rejoin the lines
        paragraph = '\n'.join(non_list_lines)
        
        # Convert single line breaks to <br> but preserve HTML structure
        if not any(tag in paragraph for tag in ['<h1>', '<h2>', '<h3>', '<ul>', '<ol>']):
            paragraph = paragraph.replace('\n', '<br>')
            if paragraph and not paragraph.startswith('<'):
                paragraph = f'<p>{paragraph}</p>'
        else:
            # For paragraphs with headers or lists, just clean up extra newlines
            paragraph = paragraph.replace('\n', '')
        
        processed_paragraphs.append(paragraph)
    
    # Join all paragraphs
    html = ''.join(processed_paragraphs)
    
    # Return as safe markup for Jinja2
    return Markup(html)

# Initialize Groq AI client
try:
    if GROQ_API_KEY == "your_groq_api_key_here" or not GROQ_API_KEY:
        print("⚠️  WARNING: Groq API key not configured!")
        print("   Please set your API key in one of these ways:")
        print("   1. Edit config.py and replace 'your_groq_api_key_here' with your actual key")
        print("   2. Set environment variable: export GROQ_API_KEY='your_key_here'")
        print("   3. Get a free key from: https://console.groq.com/")
        client = None
    else:
        client = Groq(api_key=GROQ_API_KEY)
        print("✅ Groq AI client initialized successfully")
except Exception as e:
    print(f"❌ Error initializing Groq client: {e}")
    client = None

# System prompt for EduImpactBot
system_prompt = """
You are EduImpactBot, an expert educational consultant specializing in environmental factors that affect student academic performance. 

YOUR EXPERTISE AREAS (ONLY respond about these topics):
- Parental education levels and family involvement in education
- Nutrition, diet, and eating habits that impact learning
- Mental health, stress management, and emotional wellbeing
- Social relationships, peer influences, and friendship dynamics
- Physical learning environments (home/school spaces, lighting, noise, etc.)
- Study habits and time management in environmental context

YOUR APPROACH:
- Provide research-based insights with practical applications
- Give specific, actionable recommendations that families can implement
- Use encouraging, supportive language that empowers users
- Include real statistics and evidence when relevant
- Focus on environmental solutions rather than innate abilities

IF ASKED ABOUT UNRELATED TOPICS:
Politely redirect: "I specialize in environmental factors that impact student performance. I'd be happy to discuss how [parental involvement/nutrition/mental health/social factors/study environment] affects academic success instead."

RESPONSE STYLE:
- Warm, professional, and encouraging
- Use bullet points and clear structure for readability
- Provide both insights and actionable steps
- Ask follow-up questions to deepen the conversation
- Keep responses comprehensive but focused (3-4 paragraphs typically)
"""

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/getanalysis')
def getanalysis():
    return render_template('analysis.html')



@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        print(f"Received message: {user_message}")  # Debug log
        
        # Check if Groq client is available
        if client is None:
            return jsonify({'error': 'AI service is not configured. Please contact administrator to set up the API key.'}), 503
        
        # Use Groq AI with retry mechanism
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                print(f"Attempting chat response (attempt {attempt + 1}/{max_retries})")
                
                response = client.chat.completions.create(
                    model="llama3.1-8b-instant",  # Fast and free model
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=500,
                    temperature=0.7
                )
                
                bot_response = response.choices[0].message.content
                print(f"Groq AI response successful: {bot_response}")
                return jsonify({'response': bot_response})
                
            except Exception as groq_error:
                print(f"Groq AI chat attempt {attempt + 1} error: {str(groq_error)}")
                if attempt == max_retries - 1:  # Last attempt failed
                    return jsonify({'error': f'AI service is currently unavailable: {str(groq_error)}. Please try again later.'}), 503
        
    except Exception as e:
        print(f"Chat error: {str(e)}")
        return jsonify({'error': f'Chat service error: {str(e)}'}), 500



@app.route('/archive')
def archive():
    # Path to the CSV file
    csv_path = 'model_training/student_data.csv'
    
    # Check if file exists
    if not os.path.exists(csv_path):
        return "CSV file not found", 404
    
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Get page number from request
    page = request.args.get('page', 1, type=int)
    records_per_page = 30
    
    # Calculate pagination
    total_records = len(df)
    total_pages = ceil(total_records / records_per_page)
    
    # Ensure page is within valid range
    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages
    
    # Get data for current page
    start_idx = (page - 1) * records_per_page
    end_idx = start_idx + records_per_page
    page_data = df.iloc[start_idx:end_idx]
    
    # Convert DataFrame to list of lists for template
    data = page_data.values.tolist()
    columns = df.columns.tolist()
    
    return render_template('archive.html', 
                         data=data, 
                         columns=columns, 
                         current_page=page, 
                         total_pages=total_pages, 
                         total_records=total_records,
                         min=min,
                         max=max)

@app.route('/download_csv')
def download_csv():
    csv_path = 'model_training/student_data.csv'
    
    if os.path.exists(csv_path):
        return send_file(csv_path, 
                        as_attachment=True, 
                        download_name='student_data.csv',
                        mimetype='text/csv')
    else:
        return jsonify({'error': 'File not found'}), 404
    
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract form values and convert to expected integer/float types
        input_data = np.array([[
            int(request.form['sex']),
            int(request.form['age']),
            int(request.form['address']),
            int(request.form['famsize']),
            int(request.form['Pstatus']),
            int(request.form['Medu']),
            int(request.form['Fedu']),
            int(request.form['Mjob']),
            int(request.form['Fjob']),
            int(request.form['reason']),
            int(request.form['guardian']),
            int(request.form['traveltime']),
            int(request.form['studytime']),
            int(request.form['failures']),
            int(request.form['schoolsup']),
            int(request.form['famsup']),
            int(request.form['paid']),
            int(request.form['activities']),
            int(request.form['nursery']),
            int(request.form['higher']),
            int(request.form['internet']),
            int(request.form['romantic']),
            int(request.form['famrel']),
            int(request.form['freetime']),
            int(request.form['goout']),
            int(request.form['health']),
            int(request.form['absences'])
        ]])

        input_data=np.array(input_data)
        input_data_scaled=scale.transform(input_data)
        result=model.predict(input_data_scaled)

        scores = result[0]  # Extract the list of 3 predicted scores
        pass_fail = [1 if score >= 10 else 0 for score in scores]

        pass_count = sum(pass_fail)
        fail_count = 3 - pass_count

        # Basic classification
        if pass_count == 3:
            if all(score > 15 for score in scores):
                basic_result = "Good student"
            else:
                basic_result = "Good but can do better"
        elif fail_count == 1:
            basic_result = "Scope of improvement"
        elif fail_count == 2:
            basic_result = "Can be better"
        else:
            basic_result = "Needs to work the hardest"

        # Generate AI-powered tailored response
        # Create detailed context from user inputs
        form_data = {
            'sex': 'Female' if int(request.form['sex']) == 0 else 'Male',
            'age': request.form['age'],
            'address': 'Urban' if int(request.form['address']) == 1 else 'Rural',
            'family_size': 'Large (>3)' if int(request.form['famsize']) == 1 else 'Small (≤3)',
            'parent_status': 'Living together' if int(request.form['Pstatus']) == 1 else 'Apart',
            'mother_education': request.form['Medu'],
            'father_education': request.form['Fedu'],
            'study_time': request.form['studytime'],
            'failures': request.form['failures'],
            'family_support': 'Yes' if int(request.form['famsup']) == 1 else 'No',
            'activities': 'Yes' if int(request.form['activities']) == 1 else 'No',
            'internet': 'Yes' if int(request.form['internet']) == 1 else 'No',
            'health': request.form['health'],
            'absences': request.form['absences'],
            'family_relationship': request.form['famrel'],
            'free_time': request.form['freetime'],
            'social_going_out': request.form['goout']
        }
        
        # Create AI prompt for tailored analysis
        ai_prompt = f"""
        You are an expert educational consultant analyzing a student's academic performance prediction. Based on the detailed student profile below, provide a comprehensive, personalized analysis focusing ONLY on environmental factors that impact student performance.

        STUDENT PROFILE:
        - Gender: {form_data['sex']}
        - Age: {form_data['age']} years old
        - Location: {form_data['address']}
        - Family Size: {form_data['family_size']}
        - Parents Status: {form_data['parent_status']}
        - Mother's Education Level: {form_data['mother_education']}/4
        - Father's Education Level: {form_data['father_education']}/4
        - Weekly Study Time: {form_data['study_time']} hours
        - Past Academic Failures: {form_data['failures']}
        - Family Educational Support: {form_data['family_support']}
        - Extracurricular Activities: {form_data['activities']}
        - Internet Access at Home: {form_data['internet']}
        - Health Status: {form_data['health']}/5
        - School Absences This Year: {form_data['absences']}
        - Family Relationship Quality: {form_data['family_relationship']}/5
        - Free Time After School: {form_data['free_time']}/5
        - Social Going Out Frequency: {form_data['social_going_out']}/5

        PREDICTION RESULTS:
        - Performance Category: {basic_result}
        - Predicted Academic Scores: {[round(score, 1) for score in scores]}

        PROVIDE A DETAILED ANALYSIS COVERING:

        1. **Performance Assessment**: Analyze the predicted scores and what they indicate about the student's academic trajectory.

        2. **Environmental Impact Analysis**: Focus specifically on how the following factors are affecting this student:
           - Parental education and family involvement
           - Study environment and habits
           - Social and peer influences
           - Physical health and attendance patterns
           - Access to resources (internet, educational support)

        3. **Personalized Recommendations**: Provide specific, actionable advice for:
           - Parents/family members on how to better support academic success
           - Improving the home study environment
           - Optimizing study habits and time management
           - Addressing any health or social concerns
           - Leveraging available resources more effectively

        4. **Future Outlook**: Based on the environmental factors, discuss realistic expectations and potential for improvement.

                 Format your response in a warm, encouraging tone as if speaking directly to the student and their family. 

         **FORMATTING REQUIREMENTS:**
         - Use markdown formatting for structure
         - Use ## for main headings (e.g., ## Performance Assessment)
         - Use ### for subheadings 
         - Use **bold** for emphasis
         - Use bullet points (-) for lists
         - Keep response comprehensive but focused (4-5 sections maximum)
         - Make it visually appealing and easy to read
        """

        # Check if Groq client is available
        if client is None:
            ai_result = f"""⚠️ **AI Analysis Service Not Available**

**Configuration Issue**: The AI analysis service requires a valid Groq API key to function.

**Your Prediction Results:**
- Performance Category: **{basic_result}**  
- Predicted Scores: {[round(score, 1) for score in scores]}

**Next Steps:**
1. Administrator needs to configure the Groq API key
2. Get a free API key from: https://console.groq.com/
3. Set the key in config.py or as environment variable

Your academic performance prediction has been completed successfully. Once the API key is configured, you'll receive detailed AI-powered insights about environmental factors affecting performance."""
        else:
            # Try to get AI response with multiple attempts
            ai_result = None
            max_retries = 3
            
            for attempt in range(max_retries):
                try:
                    print(f"Attempting AI analysis (attempt {attempt + 1}/{max_retries})")
                    
                    ai_response = client.chat.completions.create(
                        model="llama3.1-8b-instant",
                        messages=[
                            {"role": "system", "content": "You are an educational consultant specializing in student performance analysis. Provide personalized, actionable advice based on environmental factors."},
                            {"role": "user", "content": ai_prompt}
                        ],
                        max_tokens=600,
                        temperature=0.7
                    )
                    
                    ai_result = ai_response.choices[0].message.content
                    print("AI analysis successful!")
                    break
                    
                except Exception as groq_error:
                    print(f"Groq AI attempt {attempt + 1} error: {str(groq_error)}")
                    if attempt == max_retries - 1:  # Last attempt failed
                        ai_result = f"""I apologize, but our AI analysis service is currently experiencing technical difficulties. 

**Error Details**: {str(groq_error)}

**Your Prediction Results:**
- Performance Category: **{basic_result}**
- Predicted Scores: {[round(score, 1) for score in scores]}

While I cannot provide the detailed AI analysis at this moment, your academic performance prediction has been completed successfully. Please try again later for the personalized AI insights, or contact support if the issue persists."""

    # Convert AI response markdown to HTML for proper display
    ai_analysis_html = markdown_to_html(ai_result) if ai_result else ""
    
    return render_template('analysis.html', result=basic_result, ai_analysis=ai_analysis_html, scores=scores)


if __name__ == '__main__':
    app.run(debug=True,port=5001)