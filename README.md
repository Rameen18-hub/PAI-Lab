# 🛡️ HateGuard — Hate Speech Detection System

> **AI Programming Project** | NLP + Machine Learning + Flask  
> **Subject:** Programming for Artificial Intelligence (4th Semester)

---

## 📌 Project Description
A machine learning web application that detects and classifies text into:
- ✅ **Clean** — Normal, non-offensive content
- ⚠️ **Offensive** — Rude or insulting language  
- 🚫 **Hate Speech** — Content targeting groups with hate or violence

---

## 🚀 Quick Start (Run in 3 steps)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model
```bash
python model/train_model.py
```

### 3. Run Flask app
```bash
python app.py
```

Then open: **http://localhost:5000**

---

## 🗂️ Project Structure
```
hate_speech_detection/
│
├── app.py                    # Flask web application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── model/
│   ├── train_model.py        # ML model training script
│   └── hate_speech_model.pkl # Saved trained model (generated)
│
└── templates/
    └── index.html            # Frontend (HTML/CSS/JS)
```

---

## 🔬 Technical Details

### Machine Learning Pipeline
| Component | Details |
|-----------|---------|
| Vectorizer | TF-IDF (bi-grams, 10k features) |
| Classifier | Logistic Regression |
| Classes | 0=Clean, 1=Offensive, 2=Hate Speech |
| Accuracy | ~85% |

### NLP Preprocessing
- Lowercasing
- URL removal
- Special character removal
- Whitespace normalization

### Flask API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main web interface |
| `/analyze` | POST | Single text analysis |
| `/batch` | POST | Batch text analysis (up to 20) |
| `/history` | GET | Recent analyses |
| `/stats` | GET | Session statistics |

---

## 🎓 Built With
- **Python** — Core language
- **scikit-learn** — ML pipeline (TF-IDF + Logistic Regression)
- **Flask** — Web framework
- **HTML/CSS/JS** — Frontend interface

---

*Hate Speech Detection System — AI Programming Project*
