import streamlit as st
import pickle
import pandas as pd
import os

# Base directory of this project (folder containing app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build paths to the model files inside the project
encoder_path = os.path.join(BASE_DIR, "models", "encoder.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")
model_path  = os.path.join(BASE_DIR, "models", "model_rfc.pkl")

# Load models from the models/ folder
encoder = pickle.load(open(encoder_path, "rb"))
scaler  = pickle.load(open(scaler_path, "rb"))
model_rfc = pickle.load(open(model_path, "rb"))


#with open("C:/Users/bgunj/machine learning/1stmodel.pkl", "rb") as f:
 #   model = pickle.load(f)

#C:\Users\bgunj\Desktop\Carrer Aspiration ML PROJECT\models\encoder.pkl
#C:/Users/bgunj/ML PROJECTS/encoder.pkl
#C:\Users\bgunj\Desktop\Carrer Aspiration ML PROJECT\models\model_rfc.pkl
#C:/Users/bgunj/ML PROJECTS/scaler.pkl
#C:/Users/bgunj/ML PROJECTS/model_rfc.pkl
# Load models
#encoder = pickle.load(open("C:\Users\bgunj\Desktop\Carrer Aspiration ML PROJECT\models\encoder.pkl", "rb"))
#scaler = pickle.load(open("C:\Users\bgunj\Desktop\Carrer Aspiration ML PROJECT\models\model_rfc.pkl", 'rb'))
#model_rfc = pickle.load(open("C:\Users\bgunj\Desktop\Carrer Aspiration ML PROJECT\models\scaler.pkl", 'rb'))

# Career map
career_aspiration_map = {
    0: 'Software Engineer', 1: 'Business Owner', 2: 'Unknown', 3: 'Banker',
    4: 'Lawyer', 5: 'Accountant', 6: 'Doctor', 7: 'Real Estate Developer',
    8: 'Stock Investor', 9: 'Construction Engineer', 10: 'Artist',
    11: 'Game Developer', 12: 'Government Officer', 13: 'Teacher',
    14: 'Designer', 15: 'Scientist', 16: 'Writer'
}

def predict_career(gender, part_time_job, absence_days, extracurricular_activities, weekly_self_study_hours,
                   math_score, history_score, physics_score, chemistry_score, biology_score, english_score,
                   geography_score, total_score, average_score):

    input_data = pd.DataFrame([[gender, part_time_job, absence_days, extracurricular_activities,
                                weekly_self_study_hours, math_score, history_score, physics_score,
                                chemistry_score, biology_score, english_score, geography_score,
                                total_score, average_score]],
                              columns=['gender', 'part_time_job', 'absence_days', 'extracurricular_activities',
                                       'weekly_self_study_hours', 'math_score', 'history_score', 'physics_score',
                                       'chemistry_score', 'biology_score', 'english_score', 'geography_score',
                                       'total_score', 'average_score'])

    # Encode categorical
    input_data['gender'] = encoder.transform(input_data['gender'])
    input_data['part_time_job'] = encoder.transform(input_data['part_time_job'])
    input_data['extracurricular_activities'] = encoder.transform(input_data['extracurricular_activities'])

    # Scale numeric
    input_data[['absence_days', 'weekly_self_study_hours', 'math_score', 'history_score',
                'physics_score', 'chemistry_score', 'biology_score',
                'english_score', 'geography_score']] = scaler.transform(
        input_data[['absence_days', 'weekly_self_study_hours', 'math_score', 'history_score',
                    'physics_score', 'chemistry_score', 'biology_score',
                    'english_score', 'geography_score']])

    result = model_rfc.predict(input_data)
    return career_aspiration_map[result[0]]

# Streamlit UI
st.set_page_config(page_title="Career Aspiration Predictor", layout="centered")

st.title("🎯 Career Aspiration Predictor")
st.markdown("Enter your academic and background details below to predict your future career path!")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ['male', 'female'])
    part_time_job = st.selectbox("Part-time Job", ['True', 'False'])
    extracurricular_activities = st.selectbox("Extracurricular Activities", ['True', 'False'])
    absence_days = st.slider("Absence Days", 0, 30, 2)
    weekly_self_study_hours = st.slider("Weekly Self Study Hours", 0, 40, 10)
    total_score = st.number_input("Total Score", min_value=0, value=688)

with col2:
    math_score = st.number_input("Math Score", 0, 100, 80)
    history_score = st.number_input("History Score", 0, 100, 90)
    physics_score = st.number_input("Physics Score", 0, 100, 75)
    chemistry_score = st.number_input("Chemistry Score", 0, 100, 70)
    biology_score = st.number_input("Biology Score", 0, 100, 85)
    english_score = st.number_input("English Score", 0, 100, 95)
    geography_score = st.number_input("Geography Score", 0, 100, 88)


if st.button("Predict Career"):
    average_score = round(total_score / 8, 2)
    prediction = predict_career(
        gender, part_time_job, absence_days, extracurricular_activities,
        weekly_self_study_hours, math_score, history_score, physics_score,
        chemistry_score, biology_score, english_score, geography_score,
        total_score, average_score
    )
    st.success(f"🎓 **Predicted Career Aspiration:** {prediction}")



    # first activate virtual environment (.\.venv\Scripts\Activate.ps1)
    # then streamlit run app.py

   
    