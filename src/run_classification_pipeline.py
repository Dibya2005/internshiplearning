"""Placeholder — to be implemented in a future task."""
from transformers import pipeline

# Load pretrained sentiment analysis pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Test sentences
sentences = [
    "I love this product. It works perfectly.",
    "The movie was amazing and inspiring.",
    "Today has been a wonderful day.",
    "This is the best purchase I have ever made.",
    "The customer service was excellent.",

    "I hate this application.",
    "The food was terrible and cold.",
    "This is the worst experience of my life.",
    "The product broke after one day.",
    "I am very disappointed with the service."
]

print("=" * 70)
print("TEXT CLASSIFICATION USING PRETRAINED PIPELINE")
print("=" * 70)

for i, sentence in enumerate(sentences, start=1):
    result = classifier(sentence)[0]
    

    print(f"\nExample {i}")
    print(f"Sentence : {sentence}")
    print(f"Label    : {result['label']}")
    print(f"Score    : {result['score']:.4f}")