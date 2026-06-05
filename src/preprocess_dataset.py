
from datasets import load_dataset
from transformers import AutoTokenizer

# Load the spam dataset
dataset = load_dataset("SetFit/enron_spam")

# 1. Check what columns we are starting with
print("Original columns:", dataset['train'].column_names)
# Output: ['message_id', 'text', 'label', 'subject', 'date']

# 2. Define what we actually need
required_cols = ["text", "label"]

# 3. Identify the columns to drop
cols_to_remove = [col for col in dataset['train'].column_names if col not in required_cols]
print("Columns to remove:", cols_to_remove)
# Output: ['message_id', 'subject', 'date']

# 4. Remove them
clean_dataset = dataset.remove_columns(cols_to_remove)

print("Final columns:", clean_dataset['train'].column_names)
print("Available splits:", clean_dataset.keys())

# Output: ['text', 'label']
model_name = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)

# Tokenization function
def tokenize_function(example):

    return tokenizer(
        example["text"],
        padding="max_length",      # Pad shorter sequences
        truncation=True,           # Truncate longer sequences
        max_length=128             # Maximum sequence length
    )

# Apply tokenization in every example in the dataset
tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True #dataset sends multiple examples at once to tokenize_function()
) 

print("\nTokenization Completed")

# Example output
print("\nSample Tokenized Record:")
print(tokenized_dataset["train"][0].keys())

if "validation" not in tokenized_dataset:

    split_dataset = tokenized_dataset["train"].train_test_split(
        test_size=0.1,
        seed=42
    )

    tokenized_dataset["train"] = split_dataset["train"]
    tokenized_dataset["validation"] = split_dataset["test"]
print("Train Samples:", len(tokenized_dataset["train"]))
print("Validation Samples:", len(tokenized_dataset["validation"]))

if "test" in tokenized_dataset:
    print("Test Samples:", len(tokenized_dataset["test"]))

# Save Processed Dataset

save_path = "../data/processed_dataset_1"

tokenized_dataset.save_to_disk(save_path)

print("\nProcessed dataset saved successfully.")
print(f"Location: {save_path}")