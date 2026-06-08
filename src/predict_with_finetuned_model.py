import argparse
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_DIR = "../models/transformer_classifier_dataset_1"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

parser = argparse.ArgumentParser()
parser.add_argument("--text", required=True, help="Text to classify")
args = parser.parse_args()

text = args.text

inputs = tokenizer(
    text,
    max_length=512,
    truncation=True,
    padding=True,
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

probs = F.softmax(outputs.logits, dim=-1)[0]
pred_id = torch.argmax(probs).item()

labels = {
    0: "negative",
    1: "positive"
}

print("\nInput:")
print(text)

print("\nPrediction:")
print(labels[pred_id])

print("\nConfidence Scores:")
for i, score in enumerate(probs):
    print(f"{labels[i]}: {score.item():.4f}")