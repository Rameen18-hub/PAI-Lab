"""
Hate Speech Detection System - Flask Application
NLP + Machine Learning + Flask Web App
"""
from flask import Flask, render_template, request, jsonify
import pickle
import re
import os
import json
from datetime import datetime
from collections import Counter

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'hate_speech_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

history =[]

LABELS = {0: "Clean", 1: "offensive", 2: "Hate Speech"}
LABEL_COLORS = {0: "clean", 1: "offensive", 2: "hate"}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]','', text) 
    text = re.sub(r'\s+', ' ',text).strip()
    return text

def analyze_text(text):
    cleaned = clean_text(text)
    pred = model.predict([cleaned])[0]
    proba = model.predict_proba([cleaned])[0]
    
    confidence = float(max(proba)) * 100
    label_id = int(pred)
    label = LABELS[label_id]
    color_class = LABEL_COLORS[label_id]

    probabilities = {
        LABELS[i]: round(float(p) * 100,1)
        for i, p in enumerate (proba)
    }

    word_count = len(text.split())
    char_count = len(text)

    return {
        "label": label,
        "label_id": label_id,
        "color_class": color_class,
        "confidence": round(confidence,1),
        "probabilities": probabilities,
        "word_count": word_count,
        "char_count": char_count,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "original_text": text[:200] + ("..." if len(text) > 200 else "")
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '').strip()

    if not text:
        return jsonify({"error": "Please enter some text to analyze."}), 400
    if len(text) >5000:
        return jsonify({"error": "Text too long. Maximum 5000 characters."}), 400
    
    result = analyze_text(text)
    history.append(result)
    if len(history) > 50:
        history.pop(0)
    return jsonify(result)

@app.route('/batch', methods=['POST'])
def batch_analyze():
    data = request.get_json()
    texts = data.get('texts', [])

    if not texts:
        return jsonify({"error": "No texts provided."}), 400
    if len(text) > 20:
        return jsonify({"error": "Maximum 20 texts per batch."}), 400

    results = []
    for text in texts:
        text = text.strip()
        if text:
            results.append(analyze_text(text))

    label_counts = Counter(r['label'] for r in results)
    summary = {
        "total": len(results),
        "clean": label_counts.get("Clean", 0),
        "offensive": label_counts.get("Offensive", 0),
        "hate_speech": label_counts.get("Hate Speech", 0),
        "results": results
    }
    return jsonify(summary)

@app.route('/history')
def get_history():
    return jsonify(list(reversed(history[-10:])))

@app.route('/stats')
def get_stats():
    if not history:
        return jsonify({"total": 0, "clean": 0, "offensive": 0, "hate_speech": 0})
    label_counts = Counter(r['label'] for r in history)
    return jsonify({
        "total": len(history),
        "clean": label_counts.get("Clean", 0),
        "offensive": label_counts.get("Offensive", 0),
        "hate_speech": label_counts.get("Hate Speech", 0),
        "avg_confidence": round(sum(r['confidence'] for r in history) / len(history), 1)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
