
# ❤️ Heart Disease Prediction System

An AI-powered web application that predicts the risk of heart disease using medical parameters such as age, cholesterol, blood pressure, ECG results, and other health indicators.

The project uses **Machine Learning (Logistic Regression)** and provides an interactive **Streamlit dashboard** for real-time predictions.

---

## 🧠 Project Motivation
Heart disease is one of the leading causes of death worldwide. Early detection can significantly reduce health risks and improve treatment outcomes.

This project demonstrates how Machine Learning can assist in medical risk prediction using patient health data.

---

## 🚀 Live Demo
If deployed, add your link here:

Example:  
[Heart Disease Prediction App](https://heart-disease-prediction-by-ab.streamlit.app/)

---

## 📸 Application Screenshots
- Prediction Dashboard → `/screenshots/dashboard.png`  
- Dataset Insights → `/screenshots/data insights.png`  
- Prediction Result → `/screenshots/results.png`

---

## ⚙️ Features
- ❤️ **Heart Disease Prediction** – Predicts high or low risk.  
- 📊 **Risk Probability Score** – Shows probability percentage.  
- 📋 **Patient Summary** – Displays entered patient information.  
- 📈 **Dataset Insights** – Charts for age, cholesterol, dataset preview.  
- ⚠️ **Health Recommendations** – Suggestions for high-risk patients.  
- 📥 **Downloadable Report** – Export prediction results.  
- 📑 **Multi-Page Navigation** – Prediction, Dataset Insights, Model Info, About Page.  

---

## 🛠️ Technologies Used
| Technology   | Purpose                     |
|--------------|-----------------------------|
| Python       | Core programming language   |
| Streamlit    | Web application framework   |
| Scikit-learn | Machine learning model      |
| Pandas       | Data processing             |
| Matplotlib   | Data visualization          |
| Joblib       | Model serialization         |

---

## 📊 Dataset Information
The dataset contains medical attributes related to heart disease.

| Feature                | Description                                |
|-------------------------|--------------------------------------------|
| Age                    | Age of the patient                         |
| Gender                 | Male or Female                             |
| Chest Pain Type        | Type of chest pain                         |
| Resting Blood Pressure | Blood pressure at rest                     |
| Cholesterol            | Serum cholesterol level                    |
| Fasting Blood Sugar    | Blood sugar level                          |
| Resting ECG            | Electrocardiographic results               |
| Max Heart Rate         | Maximum heart rate achieved                |
| Exercise Angina        | Chest pain during exercise                 |
| Oldpeak                | ST depression induced by exercise          |
| Slope                  | Slope of peak exercise ST segment          |
| Major Vessels          | Number of major vessels                    |
| Thal                   | Thalassemia condition                      |

---

## 🧠 Machine Learning Model
**Logistic Regression**

**Why Logistic Regression?**
- Efficient binary classification  
- Interpretable results  
- Good performance on medical datasets  

**Workflow:**
Data Collection
│
▼
Data Cleaning
│
▼
Feature Engineering
│
▼
Model Training (Logistic Regression)
│
▼
Model Serialization (Joblib)
│
▼
Streamlit Web App


---

## 📂 Project Structure
heart-disease-prediction
│
├── app.py
├── cleaned_data.csv
├── Log_model.joblib
├── image1.png
├── heart1.jpeg
│
├── screenshots
│   ├── dashboard.png
│   ├── result.png
│   └── data_insights.png
│
└── README.md


---

## ⚙️ Installation
1️⃣ Clone the Repository  
git clone https://github.com/yourusername/heart-disease-prediction.git 
2️⃣ Navigate to Project Folder
cd heart-disease-prediction
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py


## 📊 Example Output
The model predicts:

- ✅ Low Risk

- ⚠️ High Risk

### It also displays:

- Risk probability

- Health recommendations

- Downloadable patient report

## 👨‍💻 Author
*Adarsh Bhagat*

- Skills:  
- Python, Machine Learning, Data Science, HTML, CSS, JavaScript, SQL, React, Node, Express, MongoDB

## ⭐ Support
If you like this project:
- ⭐ Star this repository
🍴 Fork it
- 🧑‍💻 Contribute to improve it

## 📜 License
- This project is open-source and available under the MIT License.

- Would you like me to also create a **badges section** (e.g., Python version, Streamlit, License, etc.) at the top of the README for a more professional GitHub look?
