🏥 Diabetes Predictor


🔗 Repository: parthvasu2004/diabetes_predictor_p


🚀 Overview


The Diabetes Predictor is a machine learning-powered web application designed to estimate the likelihood of diabetes in an individual based on various health factors such as glucose level, blood pressure, BMI, and age. The application utilizes a trained classification model and is deployed using Flask.



🛠️ Features


✔️ AI-based Diabetes Prediction using real-world patient data.✔️ Machine Learning Model trained using classification algorithms.✔️ Flask Web Application with an intuitive user interface.✔️ Secure & Scalable model deployment on Render.✔️ Provides quick & reliable predictions for early diagnosis assistance.


📂 Project Structure


diabetes_predictor_p/
│── templates/            # HTML templates for the web app  
│── static/               # Static assets like CSS & images  
│── app.py                # Flask web application  
│── diabetes.csv          # Dataset used for model training  
│── model.pkl             # Pretrained machine learning model  
│── scaler.pkl            # Data scaler for input normalization  
│── requirements.txt      # Python dependencies  
│── .gitignore            # Ignored files  
│── README.md             # Project documentation  


⚙️ Installation & Setup


1️⃣ Clone the Repository


git clone https://github.com/parthvasu2004/diabetes_predictor_p.git  

cd diabetes_predictor_p  


2️⃣ Create & Activate Virtual Environment (Optional but Recommended)


python -m venv venv  

source venv/bin/activate  # On macOS/Linux  

venv\Scripts\activate     # On Windows  


3️⃣ Install Dependencies


pip install -r requirements.txt  


4️⃣ Run the Application


python app.py  

Now, open http://127.0.0.1:5000/ in your browser to access the predictor.


🎯 How It Works


1️⃣ Enter Health Details – Input parameters like glucose levels, BMI, blood pressure, and age.2️⃣ Get Prediction – The trained machine learning model provides a diabetes risk assessment.3️⃣ Make Informed Decisions – Helps in early detection and preventive healthcare.


🔍 Machine Learning Model


✔ Algorithm Used: Logistic Regression (or other trained classifiers).✔ Dataset: diabetes.csv – Contains real-world medical data.✔ Pretrained Model: Stored as model.pkl.


🔗 Live Deployment


The application is deployed on Render. You can access it here: https://diabetes-predictor-mhp.onrender.com/


⏳ Note: Since the project is deployed on Render’s free-tier, the first-time load may take 1-50 seconds.⚠️ Disclaimer: The model is trained on a limited dataset, so the prediction accuracy may vary. Always consult a medical professional for definitive diagnosis.


🤝 Contribution


Contributions are welcome! Feel free to fork this repository, create feature branches, and submit pull requests.


📜 License


This project is licensed under the MIT License – free to use and modify.


📬 Contact


👤 Parth Vasu
📧 parthvasu2004@gmail.com
🔗 https://www.linkedin.com/in/parth-pandey-3442a9256/

