"""
Hate Speech Detection Model Training
Trains and saves the ML model pipeline using sklearn
"""

import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import re
import os

# ─── Training Data ────────────────────────────────────────────────────────────
TRAINING_DATA = [
    # Hate Speech (label=2)
    ("I hate all people from that country, they should be eliminated", 2),
    ("Those filthy foreigners are ruining our society", 2),
    ("All members of that religion are terrorists and deserve to die", 2),
    ("Women are inferior and should stay at home", 2),
    ("Those disgusting creatures don't deserve rights", 2),
    ("We should exterminate all of them", 2),
    ("They are subhuman and should be treated as such", 2),
    ("Kill all the immigrants they don't belong here", 2),
    ("I despise every single person of that race", 2),
    ("Those animals should be locked up forever", 2),
    ("That group of people are vermin infesting our country", 2),
    ("Ethnic cleansing is the only solution", 2),
    ("People of that background are genetically inferior", 2),
    ("They should all be deported and never allowed back", 2),
    ("Those degenerates have no place in civilized society", 2),
    ("That entire religion should be banned and its followers punished", 2),
    ("We need to get rid of these parasites once and for all", 2),
    ("They are destroying our culture, they must be stopped violently", 2),
    ("All those people are criminals and rapists", 2),
    ("I wish someone would wipe them all out", 2),

    # Offensive (label=1)
    ("That's so stupid, what an idiot", 1),
    ("You're such a moron for thinking that", 1),
    ("This is absolute garbage and you're dumb", 1),
    ("What a pathetic loser you are", 1),
    ("That's the dumbest thing I've ever heard", 1),
    ("You're completely useless and incompetent", 1),
    ("Stop being such a crybaby about everything", 1),
    ("You have the brain of a rock", 1),
    ("What a waste of space you are", 1),
    ("You're an absolute joke and everyone knows it", 1),
    ("Get lost you annoying little troll", 1),
    ("Nobody cares about your stupid opinion", 1),
    ("You're so ignorant it's embarrassing", 1),
    ("Shut up you don't know anything", 1),
    ("You're the most irritating person alive", 1),
    ("This is total crap and you should feel bad", 1),
    ("You're hopeless and always will be", 1),
    ("What a disgrace you are to your profession", 1),
    ("You never get anything right, typical", 1),
    ("That was an embarrassingly bad decision", 1),

    # Normal/Clean (label=0)
    ("I love spending time with my family on weekends", 0),
    ("The weather today is absolutely beautiful", 0),
    ("Just finished reading an amazing book about science", 0),
    ("Cooking my favorite pasta recipe for dinner tonight", 0),
    ("The movie was quite entertaining and well-directed", 0),
    ("I enjoy hiking through the mountains every summer", 0),
    ("Today was a productive day at work", 0),
    ("Learning new programming skills has been rewarding", 0),
    ("The local community organized a wonderful charity event", 0),
    ("I appreciate the diversity of cultures in our city", 0),
    ("This research paper presents some interesting findings", 0),
    ("The new park downtown is a great addition to the neighborhood", 0),
    ("I think we should work together to solve this problem", 0),
    ("The team did an excellent job on this project", 0),
    ("Education is the key to building a better future", 0),
    ("I disagree with that policy but I respect your view", 0),
    ("The students performed brilliantly in the competition", 0),
    ("Let's have a civil discussion about these issues", 0),
    ("The new restaurant in town has delicious food", 0),
    ("I look forward to collaborating with everyone", 0),
    ("Science and technology have improved our lives greatly", 0),
    ("The children were playing happily in the park", 0),
    ("We should celebrate our differences and learn from each other", 0),
    ("The annual festival brings the whole community together", 0),
    ("I found a great tutorial online for learning guitar", 0),
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def train():
    texts = [clean_text(t) for t, _ in TRAINING_DATA]
    labels = [l for _, l in TRAINING_DATA]

    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=10000,
            min_df=1,
            sublinear_tf=True
        )),
        ('clf', LogisticRegression(
            C=1.0,
            max_iter=1000,
            random_state=42
        ))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {acc * 100:.1f}%")
    print(classification_report(y_test, y_pred,
          target_names=["Clean", "Offensive", "Hate Speech"]))

    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hate_speech_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)
    print(f"✅ Model saved to {model_path}")
    return pipeline

if __name__ == "__main__":
    train()
