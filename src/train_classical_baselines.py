"""Placeholder — to be implemented in a future task."""
# src/train_classical_baselines.py

from datasets import load_dataset
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
import pandas as pd


# =========================
# Load Dataset
# =========================
dataset = load_dataset("ag_news")

train_texts = dataset["train"]["text"]
train_labels = dataset["train"]["label"]

test_texts = dataset["test"]["text"]
test_labels = dataset["test"]["label"]

print(f"Train Samples: {len(train_texts)}")
print(f"Test Samples : {len(test_texts)}")


# =========================
# TF-IDF Features
# =========================
print("\nCreating TF-IDF features...")

vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english"
)

X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

print("TF-IDF Shape:", X_train.shape)


# =========================
# Evaluation Function
# =========================
def evaluate_model(model_name, y_true, y_pred):
    print("\n" + "=" * 60)
    print(f"{model_name}")
    print("=" * 60)

    accuracy = accuracy_score(y_true, y_pred)

    macro_precision = precision_score(
        y_true, y_pred, average="macro"
    )
    macro_recall = recall_score(
        y_true, y_pred, average="macro"
    )
    macro_f1 = f1_score(
        y_true, y_pred, average="macro"
    )

    weighted_f1 = f1_score(
        y_true, y_pred, average="weighted"
    )

    print(f"Accuracy         : {accuracy:.4f}")
    print(f"Macro Precision  : {macro_precision:.4f}")
    print(f"Macro Recall     : {macro_recall:.4f}")
    print(f"Macro F1         : {macro_f1:.4f}")
    print(f"Weighted F1      : {weighted_f1:.4f}")

    print("\nPer-Class Metrics:")
    print(
        classification_report(
            y_true,
            y_pred,
            digits=4
        )
    )
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(cm)
    disp = ConfusionMatrixDisplay(
           confusion_matrix=cm
         )

    disp.plot()

    plt.title(f"{model_name} Confusion Matrix")

    image_path = (
       f"../results/confusion_matrices/"
       f"{model_name.replace(' ', '_')}.png"
      )

    plt.savefig(
      image_path,
      dpi=300,
      bbox_inches="tight"
   )

    plt.close()

    print(f"Saved confusion matrix: {image_path}")


# =========================
# Logistic Regression
# =========================
print("\nTraining Logistic Regression...")

lr_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

lr_model.fit(X_train, train_labels)

lr_preds = lr_model.predict(X_test)

evaluate_model(
    "Logistic Regression",
    test_labels,
    lr_preds
)


# =========================
# Linear SVM
# =========================
print("\nTraining Linear SVM...")

svm_model = LinearSVC(
    random_state=42
)

svm_model.fit(X_train, train_labels)

svm_preds = svm_model.predict(X_test)

evaluate_model(
    "Linear SVM",
    test_labels,
    svm_preds
)


# =========================
# Random Forest
# =========================
print("\nTraining Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, train_labels)

rf_preds = rf_model.predict(X_test)

evaluate_model(
    "Random Forest",
    test_labels,
    rf_preds
)