# ❤️ Heart Disease Prediction App

**"Can a handful of numbers really tell us something about your heart?"**
Turns out—yes, they can. With the right data and models, we can make meaningful predictions that could help save lives.

---

App link: https://drive.google.com/file/d/1bTwPykb4L4NUPkv7HD1WBHD8OqzloFna/view?usp=sharing

## ✨ Why This Project?

This app was born from a simple idea:
🩺 *"What if anyone could get a quick, data-driven estimate of their heart disease risk—right from a web or mobile interface?"*

Here’s why it matters and what makes it special:

* 📊 **Built on Real Medical Data**
  No synthetic guesses—the model is trained on actual clinical data to ensure meaningful, reliable outputs.

* 🚀 **Lightweight & Fast**
  No heavy frameworks or complex stacks. Just Python, a trained ML model, and a lightweight API—designed for quick integration and easy deployment.

* 🧪 **Easy to Test & Extend**
  The modular design makes it easy to use this in web apps, mobile apps, or as a backend microservice.

* 🔍 **Focused Prediction with Minimal Input**
  Only 8 features are needed (like age, cholesterol, resting BP, etc.)—no exhaustive lab work required.

---

## 🧠 How It Works

* Clean and process medical data (UCI Heart Disease Dataset).
* Train a logistic regression model to classify the likelihood of heart disease.
* Deploy the model using a simple Python API (e.g., Flask or FastAPI).
* Send a JSON request and get back a prediction (0 = No Heart Disease, 1 = Risk Detected).

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-learn** (Modeling)
* **Pandas / NumPy** (Data handling)
* **Flask or FastAPI** (API deployment)
* **Matplotlib / Seaborn** (Optional for visual analysis)

---

## 🚀 Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API

```bash
python app.py
```

### 3. Send a Request

Send a POST request to `/predict` with the 8 required features:

```json
{
  "age": 54,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 140
}
```

### 4. Receive Prediction

```json
{
  "prediction": 1,
  "message": "High risk of heart disease"
}
```

---

## 📈 Project Structure

```
heart-disease-app/
│
├── data/                      # Dataset (raw or preprocessed)
├── model/                     # Trained model file (e.g., model.pkl)
├── src/                       # Model training script
├── app.py                     # API script
├── requirements.txt
└── README.md
```

---

## 💡 Who Is This For?

Whether you're:

* A **beginner** looking to understand how to deploy ML models,
* A **developer** building health-based applications, or
* A **curious mind** exploring AI in medicine...

This project is built to be **understandable**, **practical**, and **ready to deploy.**

---

## 📬 Future Ideas

* Add a front-end UI (Streamlit or React)
* Collect live feedback and model improvement
* Integrate with wearable device APIs for real-time monitoring

---

## 🤝 Contributing

Feel free to fork, extend, or submit pull requests! Let’s build smarter health tools together.

---

## 📜 License

MIT License. Use it, improve it, share it.

