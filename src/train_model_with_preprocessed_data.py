import os
import json
import joblib
import numpy as np
import matplotlib.pyplot as plt

from datasets import load_from_disk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
)

# =====================================================
# Paths
# =====================================================

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)

project_root = os.path.dirname(
    script_dir
)

DATASET_PATH = os.path.join(
    project_root,
    "data",
    "processed_dataset_1"
)

MODEL_SAVE_DIR = os.path.join(
    project_root,
    "models",
    "classical_baselines"
)

RESULTS_FILE = os.path.join(
    project_root,
    "results",
    "classical_baseline_results.json"
)

CONFUSION_MATRIX_DIR = os.path.join(
    project_root,
    "results",
    "confusion_matrices"
)

os.makedirs(
    MODEL_SAVE_DIR, 
    exist_ok=True
)

os.makedirs(
    CONFUSION_MATRIX_DIR, 
    exist_ok=True
)

# =====================================================
# Load Dataset
# =====================================================

print("Loading dataset...\n")

dataset = load_from_disk(DATASET_PATH)

train_texts = dataset["train"]["text"]
train_labels = dataset["train"]["label"]

test_texts = dataset["test"]["text"]
test_labels = dataset["test"]["label"]

print("Train examples:", len(train_texts))
print("Test examples:", len(test_texts))

# =====================================================
# Vectorization (TF-IDF)
# =====================================================

print("\nFitting TF-IDF Vectorizer...")

vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english",
    ngram_range=(1, 2)
)

X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

y_train = np.array(train_labels)
y_test = np.array(test_labels)

# Save the Vectorizer
vectorizer_path = os.path.join(MODEL_SAVE_DIR, "tfidf_vectorizer.pkl")
joblib.dump(vectorizer, vectorizer_path)
print(f"Vectorizer saved to: {vectorizer_path}")

# =====================================================
# Define Models to Train
# =====================================================

models_to_train = {
    "Logistic_Regression": LogisticRegression(
        max_iter=1000, 
        random_state=42
    ),
    
    "Linear_SVC": LinearSVC(
        random_state=42,
        dual=False
    ),
    
    "Random_Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1  # Uses all CPU cores to speed it up!
    )
}

# Dictionary to hold all results
all_results = {}

# =====================================================
# Training & Evaluation Loop
# =====================================================

for model_name, model in models_to_train.items():
    
    print(f"\n{'='*50}")
    print(f"Training {model_name}...")
    print(f"{'='*50}")

    # 1. Train Model
    model.fit(X_train, y_train)

    # 2. Save Model
    model_path = os.path.join(MODEL_SAVE_DIR, f"{model_name}.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved to: {model_path}")

    # 3. Predict on Test Set
    print(f"Evaluating {model_name}...")
    predictions = model.predict(X_test)
    labels = y_test

    # 4. Calculate Metrics
    accuracy = accuracy_score(labels, predictions)

    macro_precision, macro_recall, macro_f1, _ = (
        precision_recall_fscore_support(
            labels, predictions, average="macro", zero_division=0
        )
    )

    weighted_precision, weighted_recall, weighted_f1, _ = (
        precision_recall_fscore_support(
            labels, predictions, average="weighted", zero_division=0
        )
    )

    # 5. Save Confusion Matrix Image
    cm = confusion_matrix(labels, predictions)
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, cmap="Oranges")
    plt.title(f"{model_name} Confusion Matrix")
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    
    cm_path = os.path.join(
        CONFUSION_MATRIX_DIR, 
        f"{model_name}_confusion_matrix_preprocessed.png"
    )
    plt.savefig(cm_path)
    plt.close()
    print(f"Confusion matrix saved to: {cm_path}")

    # 6. Store Results
    all_results[model_name] = {
        "accuracy": float(accuracy),
        "macro_f1": float(macro_f1),
        "weighted_f1": float(weighted_f1)
    }

# =====================================================
# Save Final Combined Results
# =====================================================

with open(RESULTS_FILE, "w") as f:
    json.dump(all_results, f, indent=4)

print("\n" + "="*50)
print("FINAL BASELINE RESULTS OVERVIEW")
print("="*50)
print(json.dumps(all_results, indent=4))
print(f"\nAll metrics saved to {RESULTS_FILE}")