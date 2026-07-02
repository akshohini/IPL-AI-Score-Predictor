# 🏏 IPL AI Score Predictor

A Deep Learning based web application that predicts the **first innings score of an IPL match** using live match parameters. The model is trained on historical IPL match data and deployed using Flask, allowing users to predict scores through a simple web interface.

---

## 📌 Project Overview

The objective of this project is to predict the expected first innings score of an IPL match using machine learning and deep learning techniques.

The application takes current match information such as batting team, bowling team, venue, batsman, bowler, runs, wickets, overs, and striker runs as input and predicts the final first innings score.

---

## ✨ Features

- 🏏 Predict first innings IPL score
- 🤖 Deep Learning model built using TensorFlow/Keras
- 🌐 Flask web application
- 📊 Data preprocessing using Label Encoding and MinMax Scaling
- 🎯 User-friendly interface
- ✅ Input validation
- ⚡ Real-time prediction

---

## 🛠 Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- TensorFlow / Keras
- Flask
- NumPy
- Pandas
- Scikit-learn
- Joblib

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```text
IPL-Score-Predictor/
│
├── app.py
├── README.md
├── requirements.txt
│
├── dataset/
│   └── ipl_data.csv
│
├── model/
│   ├── ipl_score_predictor.keras
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
├── notebook/
│   └── ipl_score_prediction.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
└── screenshots/
```

---

## 📊 Dataset

The model is trained using historical IPL match data.

### Input Features

- Batting Team
- Bowling Team
- Venue
- Batsman
- Bowler
- Current Runs
- Wickets
- Overs
- Striker Runs

### Target

- First Innings Final Score

---

## 🧠 Model Architecture

The prediction model is built using a Deep Neural Network.

```
Input Layer (9 Features)
        │
        ▼
Dense Layer (512 Neurons)
        │
        ▼
Dense Layer (216 Neurons)
        │
        ▼
Output Layer (Predicted Score)
```

### Activation Function
- ReLU

### Optimizer
- Adam

### Loss Function
- Mean Squared Error (MSE)

### Evaluation Metric
- Mean Absolute Error (MAE)

Final MAE achieved:

```
14.414
```

---

## ⚙ Data Preprocessing

The following preprocessing steps were performed before training:

- Removed unnecessary columns
- Label Encoding for categorical features
- MinMax Feature Scaling
- Train-Test Split
- Model Training

---

## 🌐 Application Workflow

```
User
   │
   ▼
Enter Match Details
   │
   ▼
Flask Backend
   │
   ▼
Load Label Encoders
   │
   ▼
Encode Inputs
   │
   ▼
Load Scaler
   │
   ▼
Scale Features
   │
   ▼
Deep Learning Model
   │
   ▼
Predicted Score
   │
   ▼
Display Result
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/IPL-AI-Score-Predictor.git
```

Go inside the project

```bash
cd IPL-AI-Score-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### Prediction Result

(Add screenshot here)

### Validation

(Add screenshot here)

---

## 🔮 Future Enhancements

- Win probability prediction
- Team logo integration
- Match statistics dashboard
- Live IPL API integration
- Improved model using LSTM/XGBoost
- Cloud deployment

---

## 🎓 Learning Outcomes

Through this project, I learned:

- Deep Learning using TensorFlow
- Data preprocessing
- Feature engineering
- Label Encoding
- Feature Scaling
- Flask deployment
- Model serialization
- End-to-end AI application development

---

## 👩‍💻 Author

**Akshohini Goud**

Computer Science Engineering Student

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and Full Stack Development.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub.