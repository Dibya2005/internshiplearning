# src/train_transformer_classifier_2.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datasets import load_from_disk
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# =========================
# Create Directories
# =========================
DATASET_PATH = Path("../data/processed_dataset_2")
MODEL_SAVE_PATH = Path("../models/transformer_classifier_dataset_2")
CSV_SAVE_PATH = Path("../results/second_dataset_results.csv")
CM_SAVE_PATH = Path("../results/dataset_2_results/confusion_matrices/transformer_confusion_matrix2.png")

# Ensure directories exist
MODEL_SAVE_PATH.mkdir(parents=True, exist_ok=True)
CSV_SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
CM_SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)

# =========================
# Load Dataset 2 (AG News)
# =========================
print("Loading AG News dataset from disk...")
dataset = load_from_disk(str(DATASET_PATH))

train_dataset = dataset["train"]
val_dataset = dataset["validation"]
test_dataset = dataset["test"]

num_labels = len(set(train_dataset["label"]))
print(f"Detected {num_labels} unique classes.")

print("\nInitializing Tokenizer and Model...")
MODEL_NAME = "prajjwal1/bert-tiny"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=num_labels)

def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=128,
    )

print("Tokenizing datasets...")
train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)

columns = ["input_ids", "attention_mask", "label"]
train_dataset.set_format(type="torch", columns=columns)
val_dataset.set_format(type="torch", columns=columns)
test_dataset.set_format(type="torch", columns=columns)

# =========================
# Metrics Function
# =========================
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    
    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, predictions, average="weighted", zero_division=0
    )
    
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

# =========================
# Training Arguments
# =========================
print("\nSetting up training...")
training_args = TrainingArguments(
    output_dir="../results/dataset_2_results/transformer_checkpoints",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    learning_rate=2e-5,
    eval_strategy="epoch",
    save_strategy="epoch",              # Disabled checkpoint saving to save space
    load_best_model_at_end=True,    # Load best model at the end of training
    metric_for_best_model="f1",     # Use F1 score to determine best model
    report_to="none",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

# =========================
# Train
# =========================
print("\n" + "=" * 60)
print("Starting Transformer Training on AG News")
print("=" * 60)
trainer.train()

# =========================
# Test Evaluation & CSV (Step 12.5)
# =========================
print("\nEvaluating on Test Set...")
predictions_output = trainer.predict(test_dataset)
predictions = np.argmax(predictions_output.predictions, axis=1)
labels = predictions_output.label_ids

accuracy = accuracy_score(labels, predictions)
macro_p, macro_r, macro_f1, _ = precision_recall_fscore_support(labels, predictions, average="macro", zero_division=0)
weight_p, weight_r, weight_f1, _ = precision_recall_fscore_support(labels, predictions, average="weighted", zero_division=0)

results_df = pd.DataFrame([{
    "Model": "bert-tiny (Transformer)",
    "Dataset": "AG News (4 Classes)",
    "Accuracy": accuracy,
    "Macro_Precision": macro_p,
    "Macro_Recall": macro_r,
    "Macro_F1": macro_f1,
    "Weighted_F1": weight_f1
}])

results_df.to_csv(CSV_SAVE_PATH, index=False)
print(f"\nResults successfully saved to CSV: {CSV_SAVE_PATH}")
print(results_df.to_string(index=False))

# =========================
# Confusion Matrix
# =========================
cm = confusion_matrix(labels, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Purples")
plt.title("Transformer Confusion Matrix (Dataset 2)")
plt.xlabel("Predicted (0:World, 1:Sports, 2:Business, 3:Sci/Tech)")
plt.ylabel("Actual")
plt.savefig(CM_SAVE_PATH, dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved confusion matrix: {CM_SAVE_PATH}")

# =====================================================
# Save Model (Step 12.5) 
# =====================================================
# Uncomment the three lines below if you actually need the model files saved!

trainer.save_model(str(MODEL_SAVE_PATH))
tokenizer.save_pretrained(str(MODEL_SAVE_PATH))
print(f"\nModel securely saved to: {MODEL_SAVE_PATH}")