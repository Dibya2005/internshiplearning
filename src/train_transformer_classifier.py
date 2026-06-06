import os
import json
import numpy as np
import matplotlib.pyplot as plt

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
)

# =====================================================
# Paths (Dynamic to prevent ../ crashes)
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

MODEL_SAVE_PATH = os.path.join(
    project_root,
    "models",
    "transformer_classifier_dataset_1"
)

RESULTS_FILE = os.path.join(
    project_root,
    "results",
    "transformer_classifier_results.json"
)

CONFUSION_MATRIX_DIR = os.path.join(
    project_root,
    "results",
    "confusion_matrices"
)

CONFUSION_MATRIX_PATH = os.path.join(
    CONFUSION_MATRIX_DIR,
    "transformer_classifier_confusion_matrix.png"
)

os.makedirs(
    MODEL_SAVE_PATH, 
    exist_ok=True
)

os.makedirs(
    CONFUSION_MATRIX_DIR, 
    exist_ok=True
)

# =====================================================
# Load Dataset
# =====================================================

dataset = load_from_disk(DATASET_PATH)

train_dataset = dataset["train"]
val_dataset = dataset["validation"]
test_dataset = dataset["test"]

print("Train:", len(train_dataset))
print("Validation:", len(val_dataset))
print("Test:", len(test_dataset))

# =====================================================
# Model
# =====================================================

MODEL_NAME = "prajjwal1/bert-tiny"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

num_labels = len(set(train_dataset["label"]))

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=num_labels
)

# =====================================================
# Tokenization
# =====================================================

def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=128,
    )

train_dataset = train_dataset.map(
    tokenize_function,
    batched=True
)

val_dataset = val_dataset.map(
    tokenize_function,
    batched=True
)

test_dataset = test_dataset.map(
    tokenize_function,
    batched=True
)

columns = [
    "input_ids",
    "attention_mask",
    "label"
]

train_dataset.set_format(
    type="torch",
    columns=columns
)

val_dataset.set_format(
    type="torch",
    columns=columns
)

test_dataset.set_format(
    type="torch",
    columns=columns
)

# =====================================================
# Metrics
# =====================================================

def compute_metrics(eval_pred):

    logits, labels = eval_pred

    predictions = np.argmax(
        logits,
        axis=-1
    )

    accuracy = accuracy_score(
        labels,
        predictions
    )

    precision, recall, f1, _ = (
        precision_recall_fscore_support(
            labels,
            predictions,
            average="weighted"
        )
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

# =====================================================
# Training Arguments
# =====================================================

training_args = TrainingArguments(
    output_dir=os.path.join(
        project_root, 
        "results", 
        "transformer_checkpoints"
    ),

    num_train_epochs=3,

    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,

    learning_rate=2e-5,

    eval_strategy="epoch",
    save_strategy="epoch",

    logging_dir=os.path.join(
        project_root, 
        "results", 
        "logs"
    ),

    logging_steps=100,

    load_best_model_at_end=True,

    metric_for_best_model="f1",

    report_to="none",
)

# =====================================================
# Trainer
# =====================================================

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

# =====================================================
# Train
# =====================================================

print("\nStarting Training...\n")

trainer.train()

# =====================================================
# Save Model
# =====================================================

trainer.save_model(MODEL_SAVE_PATH)
tokenizer.save_pretrained(MODEL_SAVE_PATH)

print(f"\nModel saved to: {MODEL_SAVE_PATH}")

# =====================================================
# Test Evaluation
# =====================================================

predictions_output = trainer.predict(
    test_dataset
)

predictions = np.argmax(
    predictions_output.predictions,
    axis=1
)

labels = predictions_output.label_ids

accuracy = accuracy_score(
    labels,
    predictions
)

macro_precision, macro_recall, macro_f1, _ = (
    precision_recall_fscore_support(
        labels,
        predictions,
        average="macro",
        zero_division=0
    )
)

weighted_precision, weighted_recall, weighted_f1, _ = (
    precision_recall_fscore_support(
        labels,
        predictions,
        average="weighted",
        zero_division=0
    )
)

per_class_precision, per_class_recall, per_class_f1, _ = (
    precision_recall_fscore_support(
        labels,
        predictions,
        average=None,
        zero_division=0
    )
)

# =====================================================
# Confusion Matrix
# =====================================================

cm = confusion_matrix(
    labels,
    predictions
)

plt.figure(figsize=(8, 6))
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig(CONFUSION_MATRIX_PATH)
plt.close()

# =====================================================
# Save Metrics
# =====================================================

results = {
    "accuracy": float(accuracy),

    "macro_precision": float(macro_precision),
    "macro_recall": float(macro_recall),
    "macro_f1": float(macro_f1),

    "weighted_precision": float(weighted_precision),
    "weighted_recall": float(weighted_recall),
    "weighted_f1": float(weighted_f1),

    "per_class_precision":
        per_class_precision.tolist(),

    "per_class_recall":
        per_class_recall.tolist(),

    "per_class_f1":
        per_class_f1.tolist(),

    "confusion_matrix":
        cm.tolist(),
}

with open(
    RESULTS_FILE,
    "w"
) as f:
    json.dump(
        results,
        f,
        indent=4
    )

print("\nTest Results")
print(json.dumps(results, indent=4))

print(
    f"\nMetrics saved to {RESULTS_FILE}"
)

print(
    f"Confusion matrix saved to "
    f"{CONFUSION_MATRIX_PATH}"
)