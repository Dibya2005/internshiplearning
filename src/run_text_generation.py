
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Model name
MODEL_NAME = "distilgpt2"

# Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

# Prompts
prompts = [
    "Artificial intelligence is",
    "Machine learning helps in",
    "A language model is"
]

print("=" * 60)
print(f"Model Name : {MODEL_NAME}")
print(f"Device Used: {device}")
print("=" * 60)

for prompt in prompts:
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # Generate text
    output_ids = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=0.8,
        
    )

    # Decode generated text
    generated_text = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    )

    # Print results
    print("\n" + "-" * 60)
    print(f"Input Prompt   : {prompt}")
    print(f"Generated Text : {generated_text}")
    print(f"Model Name     : {MODEL_NAME}")
    print(f"Device Used    : {device}")
    print("-" * 60)