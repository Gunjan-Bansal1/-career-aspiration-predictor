# 🎯 Career Aspiration Predictor

This project uses **Machine Learning + Streamlit** to predict a student's likely **career aspiration**
(e.g. Software Engineer, Doctor, Business Owner, Artist, etc.) based on their:

- Academic scores (Math, Physics, History, etc.)
- Behavioural features (absences, self-study hours)
- Background (gender, part-time job, extracurricular activities)

This project is built entirely in **Python + Streamlit**, using a trained Random Forest Classifier and saved preprocessing models (`encoder.pkl`, `scaler.pkl`, `model_rfc.pkl`) to perform instant prediction.

---

## 🧱 Project Structure

```text
CARRER ASPIRATION ML PROJECT/
│── app.py                 # Streamlit web app (main entry)
│── requirements.txt       # Python dependencies
│── README.md              # This file
│
├── data/
│   └── student-scores.csv # Dataset used for training
│
├── models/
│   ├── encoder.pkl        # Label encoder for categoricals
│   ├── scaler.pkl         # StandardScaler for numeric features
│   └── model_rfc.pkl      # Trained RandomForest classifier
│
├── notebooks/
│   └── Career Aspiration Predictor.ipynb  # Jupyter experiment / EDA / model training
│
└── src/
    ├── __init__.py

```    
    

⚙️ Setup (Local)

1️⃣ Clone or download this project.
2️⃣ Open a terminal in the project folder.
3️⃣ Create & activate virtual environment:

python -m venv .venv
.\.venv\Scripts\Activate.ps1 (# In Windows PowerShell)

4️⃣ Install dependencies:

pip install -r requirements.txt

5️⃣ Run Streamlit app

streamlit run app.py

🖥️ UI Workflow

1. Enter background details:
     Gender
     Part-time job (Yes/No)
     Extracurricular activities (Yes/No)
     Absence days
     Weekly self-study hours
2. Enter subject scores (Math, Physics, Chemistry, etc.)
3. Click "Predict Career".
4. The app will show a predicted career aspiration such as:

   🎯Predicted Career Aspiration: Software Engineer

🧩 Tech Stack

Python
Pandas, NumPy
scikit-learn (LabelEncoder, StandardScaler, RandomForestClassifier)
Streamlit – for the interactive web interface
Jupyter Notebook – for experimentation & EDA   

🚀 Future Enhancements

Add career recommendation charts based on score distributions
Add explanation (SHAP values) for prediction transparency
Deployment to Streamlit Cloud / AWS / Azure
Add login system for student profiles
