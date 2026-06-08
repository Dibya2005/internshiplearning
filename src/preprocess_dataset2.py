import os
from datasets import load_dataset, DatasetDict

# Setup robust paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
SAVE_PATH = os.path.join(project_root, "data", "processed_dataset_2")

print("Downloading AG News dataset...")
# AG News has 4 classes: 0: World, 1: Sports, 2: Business, 3: Sci/Tech
raw_dataset = load_dataset("ag_news")

print("Creating Train, Validation, and Test splits...")
# Split 10% of the training data off to create our validation set
train_val_split = raw_dataset["train"].train_test_split(test_size=0.1, seed=42)

processed_dataset = DatasetDict({
    "train": train_val_split["train"],
    "validation": train_val_split["test"],
    "test": raw_dataset["test"]
})

print(f"Train size: {len(processed_dataset['train'])}")
print(f"Validation size: {len(processed_dataset['validation'])}")
print(f"Test size: {len(processed_dataset['test'])}")

os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
processed_dataset.save_to_disk(SAVE_PATH)
print(f"\nDataset successfully saved to: {SAVE_PATH}")