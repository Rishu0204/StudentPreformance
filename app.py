from flask import Flask, render_template, request, send_file, jsonify
import numpy as np
import gzip
import pickle
import pandas as pd
import os
from math import ceil
from groq import Groq
from config import GROQ_API_KEY
with gzip.open('model.pkl', 'rb') as f:
    scale, model = pickle.load(f)

app=Flask(__name__)

# Initialize Groq AI client
client = Groq(api_key=GROQ_API_KEY)

# System prompt for EduImpactBot
system_prompt = """
You are  an expert on how environmental factors affect student performance.
Only talk about:
- Parents' education & involvement
- Diet & nutrition
- Mental health
- Social life
- Physical environment,and related factors only.
You are a chatbot designed to help users understand how various factors impact student performance

If a user asks something unrelated, politely redirect them to one of these topics.
Provide helpful, informative responses that are educational and supportive.
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
        
        # Use Groq AI
        try:
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
            print(f"Groq AI response: {bot_response}")
            return jsonify({'response': bot_response})
            
        except Exception as groq_error:
            print(f"Groq AI error: {str(groq_error)}")
            
            # Fallback to intelligent responses
            bot_response = get_fallback_response(user_message)
            return jsonify({'response': bot_response})
        
    except Exception as e:
        print(f"Chat error: {str(e)}")
        return jsonify({'error': f'Chat service error: {str(e)}'}), 500

def get_fallback_response(user_message):
    """Provide intelligent fallback responses when OpenAI is unavailable"""
    message_lower = user_message.lower()
    
    # Parent education & involvement
    if any(word in message_lower for word in ['parent', 'mother', 'father', 'family', 'involvement']):
        return """Great question about parental involvement! Research shows that parental education and involvement significantly impact student performance. 

**Key findings:**
• Students with highly educated parents (college degree) typically score 15-20% higher
• Active parental involvement in homework and school activities improves grades by 10-15%
• Regular communication between parents and teachers leads to better academic outcomes

**Recommendations:**
• Encourage parents to attend school meetings and events
• Establish regular homework routines at home
• Create a supportive learning environment with books and educational resources
• Maintain open communication with teachers about student progress

Would you like to know more about specific strategies for parental involvement?"""
    
    # Diet & nutrition
    elif any(word in message_lower for word in ['diet', 'nutrition', 'food', 'eating', 'breakfast', 'lunch']):
        return """Excellent question about nutrition and learning! Proper nutrition is crucial for cognitive development and academic performance.

**Research shows:**
• Students who eat breakfast regularly score 17% higher on tests
• Omega-3 fatty acids improve memory and concentration
• Iron deficiency can reduce cognitive performance by 25%
• Dehydration can impair cognitive function significantly

**Key recommendations:**
• Ensure students eat a balanced breakfast with protein and complex carbs
• Include brain-boosting foods: fish, nuts, berries, whole grains
• Stay hydrated throughout the day
• Avoid excessive sugar and processed foods
• Consider school lunch programs for balanced nutrition

**Brain-boosting foods:**
• Fatty fish (salmon, tuna) - Omega-3
• Nuts and seeds - Vitamin E
• Berries - Antioxidants
• Dark chocolate - Flavonoids
• Eggs - Choline for memory

Would you like specific meal planning tips for students?"""
    
    # Mental health
    elif any(word in message_lower for word in ['mental', 'health', 'stress', 'anxiety', 'depression', 'wellbeing']):
        return """Mental health is absolutely critical for academic success! Students' emotional wellbeing directly impacts their learning ability.

**Mental health impact on learning:**
• Stress can reduce memory retention by 40%
• Anxiety affects concentration and test performance
• Depression can lead to 20-30% lower academic achievement
• Good mental health improves problem-solving skills

**Signs to watch for:**
• Changes in sleep patterns or appetite
• Withdrawal from friends and activities
• Declining academic performance
• Irritability or mood swings
• Physical symptoms (headaches, stomachaches)

**Support strategies:**
• Create a safe, supportive environment at home and school
• Encourage open communication about feelings
• Teach stress management techniques (deep breathing, meditation)
• Ensure adequate sleep (8-10 hours for teens)
• Promote physical activity and social connections
• Consider professional help when needed

**School-based support:**
• Counseling services
• Peer support groups
• Mindfulness programs
• Regular check-ins with teachers

Would you like specific techniques for managing academic stress?"""
    
    # Social life
    elif any(word in message_lower for word in ['social', 'friends', 'peer', 'relationship', 'friendship']):
        return """Social connections are vital for student development and academic success! Peer relationships significantly influence learning outcomes.

**Social factors affecting performance:**
• Students with strong friendships show 15% higher engagement
• Positive peer relationships reduce stress and anxiety
• Social support improves resilience during academic challenges
• Peer tutoring can improve grades by 10-15%

**Building positive social connections:**
• Encourage participation in clubs and activities
• Foster inclusive classroom environments
• Teach conflict resolution skills
• Promote collaborative learning projects
• Support healthy friendship development

**Red flags to address:**
• Social isolation or withdrawal
• Bullying or exclusion
• Peer pressure affecting academic choices
• Conflicts with friends impacting school performance

**Strategies for parents and teachers:**
• Monitor social interactions without being intrusive
• Encourage diverse friendships
• Address bullying immediately
• Create opportunities for positive peer interactions
• Teach empathy and communication skills

Would you like tips on helping students build healthy friendships?"""
    
    # Physical environment
    elif any(word in message_lower for word in ['environment', 'physical', 'space', 'room', 'study', 'area', 'noise', 'light']):
        return """The physical learning environment is crucial for academic success! Research shows that environmental factors can improve or hinder performance by 20-30%.

**Optimal study environment factors:**
• **Lighting:** Natural light improves mood and reduces eye strain
• **Noise:** Quiet environments (40-50 dB) optimize concentration
• **Temperature:** 68-72°F (20-22°C) is ideal for learning
• **Air quality:** Good ventilation improves cognitive function
• **Space:** Organized, clutter-free areas reduce distractions

**Creating an ideal study space:**
• Dedicated, quiet study area
• Good lighting (natural light preferred)
• Comfortable seating and proper desk height
• Minimal distractions (no TV, phones)
• Organized supplies and materials
• Proper temperature and ventilation

**School environment considerations:**
• Classroom layout and seating arrangements
• Noise levels and acoustic design
• Lighting quality and natural light access
• Air quality and ventilation systems
• Technology integration and accessibility

**Home environment tips:**
• Designate a specific study area
• Ensure adequate lighting
• Minimize background noise
• Keep the space organized and clean
• Provide necessary supplies and resources

Would you like specific tips for optimizing your study environment?"""
    
    # General response
    else:
        return """I'm here to help you understand how environmental factors affect student performance! 

I can provide insights on:
• Parents' education & involvement
• Diet & nutrition 
• Mental health
• Social life
• Physical environment

What specific aspect would you like to explore? Just ask me about any of these topics, and I'll provide research-based insights and practical recommendations!"""

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
        try:
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
            
            # Use Groq AI
            try:
                # Create AI prompt for tailored analysis
                ai_prompt = f"""
                Based on this student's profile, provide a detailed, personalized analysis of their academic performance and specific recommendations:

                Student Profile:
                - Gender: {form_data['sex']}
                - Age: {form_data['age']}
                - Location: {form_data['address']}
                - Family Size: {form_data['family_size']}
                - Parents Status: {form_data['parent_status']}
                - Mother's Education Level: {form_data['mother_education']}/4
                - Father's Education Level: {form_data['father_education']}/4
                - Weekly Study Time: {form_data['study_time']} hours
                - Past Failures: {form_data['failures']}
                - Family Educational Support: {form_data['family_support']}
                - Extracurricular Activities: {form_data['activities']}
                - Internet Access: {form_data['internet']}
                - Health Status: {form_data['health']}/5
                - School Absences: {form_data['absences']}
                - Family Relationship Quality: {form_data['family_relationship']}/5
                - Free Time After School: {form_data['free_time']}/5
                - Social Going Out: {form_data['social_going_out']}/5

                Predicted Performance: {basic_result}
                Predicted Scores: {[round(score, 1) for score in scores]}

                Please provide:
                1. A personalized analysis of their strengths and challenges
                2. Specific recommendations based on their environmental factors
                3. Focus on actionable advice for parents, nutrition, study environment, and social factors
                4. Keep the response encouraging and constructive
                5. Limit to 3-4 paragraphs maximum

                Format the response in a friendly, supportive tone as if speaking directly to the student and their family.
                """

                # Get AI response
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
                
            except Exception as groq_error:
                print(f"Groq AI prediction error: {str(groq_error)}")
                # Fallback to intelligent analysis
                ai_result = get_prediction_fallback(form_data, basic_result, scores)
            
        except Exception as e:
            print(f"AI analysis error: {str(e)}")
            ai_result = f"{basic_result}. Our AI analysis is currently unavailable, but your prediction has been completed successfully."

    return render_template('analysis.html', result=basic_result, ai_analysis=ai_result, scores=scores)

def get_prediction_fallback(form_data, basic_result, scores):
    """Provide intelligent fallback analysis for predictions when OpenAI is unavailable"""
    
    # Analyze the student profile
    analysis_parts = []
    
    # Basic performance analysis
    if basic_result == "Good student":
        analysis_parts.append("🎉 Excellent news! Your student shows strong academic potential with good performance indicators.")
    elif basic_result == "Good but can do better":
        analysis_parts.append("👍 Good foundation! Your student has solid academic skills with room for improvement.")
    elif basic_result == "Scope of improvement":
        analysis_parts.append("📈 There's clear potential for improvement! With targeted support, significant progress is possible.")
    else:
        analysis_parts.append("💪 Every student has unique strengths! Let's focus on building a supportive environment for growth.")
    
    # Family background analysis
    mother_edu = int(form_data['mother_education'])
    father_edu = int(form_data['father_education'])
    family_support = form_data['family_support']
    
    if mother_edu >= 3 or father_edu >= 3:
        analysis_parts.append("👨‍👩‍👧‍👦 **Family Background:** Strong parental education levels provide excellent academic role models and support systems.")
    elif mother_edu >= 1 or father_edu >= 1:
        analysis_parts.append("👨‍👩‍👧‍👦 **Family Background:** Moderate parental education levels. Consider additional educational resources and support.")
    else:
        analysis_parts.append("👨‍👩‍👧‍👦 **Family Background:** Limited parental education. Focus on creating supportive learning environments and accessing educational resources.")
    
    if family_support == "Yes":
        analysis_parts.append("🏠 **Family Support:** Excellent! Active family involvement in education significantly boosts academic success.")
    else:
        analysis_parts.append("🏠 **Family Support:** Consider increasing family involvement in homework and school activities for better outcomes.")
    
    # Study habits analysis
    study_time = int(form_data['study_time'])
    if study_time >= 3:
        analysis_parts.append("📚 **Study Habits:** Strong study time commitment! This dedication will pay off in academic performance.")
    elif study_time >= 2:
        analysis_parts.append("📚 **Study Habits:** Moderate study time. Consider gradually increasing study hours for better results.")
    else:
        analysis_parts.append("📚 **Study Habits:** Limited study time. Focus on building consistent study routines and time management skills.")
    
    # Social factors analysis
    activities = form_data['activities']
    social_going = int(form_data['social_going_out'])
    
    if activities == "Yes":
        analysis_parts.append("🎯 **Extracurricular Activities:** Great! Participation in activities develops well-rounded skills and social connections.")
    else:
        analysis_parts.append("🎯 **Extracurricular Activities:** Consider encouraging participation in clubs or activities for social development.")
    
    if social_going >= 3:
        analysis_parts.append("👥 **Social Life:** Active social engagement! This supports emotional wellbeing and reduces academic stress.")
    elif social_going >= 2:
        analysis_parts.append("👥 **Social Life:** Moderate social activity. Balance social time with academic focus for optimal results.")
    else:
        analysis_parts.append("👥 **Social Life:** Limited social engagement. Encourage healthy peer relationships while maintaining academic focus.")
    
    # Environmental factors
    address = form_data['address']
    internet = form_data['internet']
    
    if address == "Urban":
        analysis_parts.append("🏙️ **Environment:** Urban setting provides access to educational resources and opportunities.")
    else:
        analysis_parts.append("🌳 **Environment:** Rural setting may have limited resources. Focus on maximizing available educational opportunities.")
    
    if internet == "Yes":
        analysis_parts.append("🌐 **Technology Access:** Internet access enables online learning resources and research capabilities.")
    else:
        analysis_parts.append("🌐 **Technology Access:** Limited internet access. Consider community resources and offline learning materials.")
    
    # Health and attendance
    health = int(form_data['health'])
    absences = int(form_data['absences'])
    
    if health >= 4:
        analysis_parts.append("💪 **Health Status:** Good health supports optimal learning and concentration.")
    else:
        analysis_parts.append("💪 **Health Status:** Consider addressing health concerns as they can impact academic performance.")
    
    if absences <= 5:
        analysis_parts.append("📅 **Attendance:** Good school attendance! Regular attendance is crucial for academic success.")
    else:
        analysis_parts.append("📅 **Attendance:** High absenteeism can impact learning. Focus on improving attendance for better outcomes.")
    
    # Recommendations
    analysis_parts.append("\n**🎯 Key Recommendations:**")
    
    if basic_result in ["Scope of improvement", "Can be better", "Needs to work the hardest"]:
        analysis_parts.append("• Establish consistent study routines and time management")
        analysis_parts.append("• Increase family involvement in educational activities")
        analysis_parts.append("• Focus on building confidence and motivation")
        analysis_parts.append("• Consider additional academic support or tutoring")
        analysis_parts.append("• Create a distraction-free study environment")
    else:
        analysis_parts.append("• Maintain current positive study habits")
        analysis_parts.append("• Continue family involvement and support")
        analysis_parts.append("• Challenge with advanced materials to maintain growth")
        analysis_parts.append("• Encourage leadership roles in activities")
        analysis_parts.append("• Set higher academic goals for continued excellence")
    
    analysis_parts.append(f"\n**📊 Predicted Scores:** {[round(score, 1) for score in scores]}")
    analysis_parts.append("\nRemember: Every student is unique! Focus on individual strengths while addressing areas for growth.")
    
    return "\n\n".join(analysis_parts)
if __name__ == '__main__':
    app.run(debug=True,port=5001)