from datasets import load_dataset
from collections import Counter
import pandas as pd

# Dataset name and configuration
datasets_to_load = [
    ("imdb", None),
    ("tweet_eval", "sentiment")
]

# Will store summary information for CSV
summary = []

for dataset_name, config in datasets_to_load:

    # Load dataset
    # imdb -> load_dataset("imdb")
    # tweet_eval -> load_dataset("tweet_eval", "sentiment")
    dataset = load_dataset(dataset_name, config) if config else load_dataset(dataset_name)

    print("\n" + "=" * 80)
    print(f"DATASET: {dataset_name}")
    print("=" * 80)

    # Select training split
    train_split = dataset["train"]

    # Get label names
    # Example:
    # IMDB -> ['neg', 'pos']
    # TweetEval -> ['negative', 'neutral', 'positive']
    try:
        label_names = train_split.features["label"].names
    except:
        label_names = None

    print("\nFirst 5 Examples:")

    # Print first 5 examples
    for i in range(5):

        # Example row:
        # {
        #   'text': 'This movie is amazing',
        #   'label': 1
        # }
        row = train_split[i]

        # Some datasets use "text"
        # Some datasets use "sentence"
        text = row.get("text") or row.get("sentence")

        label = row["label"]

        print(f"\nExample {i+1}")
        print("Text:", text[:200])  # show first 200 characters only

        if label_names:
            # Example:
            # label = 1
            # label_names[1] -> 'pos'
            print("Label:", label_names[label])
        else:
            print("Label:", label)

    print("\nClass Distribution:")

    # Get all labels from training split
    # Example:
    # [0,1,0,1,1,0,0,...]
    labels = train_split["label"]

    # Count occurrences of each label
    #
    # Example:
    # labels = [0,1,0,1,1]
    #
    # Counter(labels)
    # Output:
    # Counter({
    #     1: 3,
    #     0: 2
    # })
    #
    counts = Counter(labels)

    # Loop through each class
    for label_id, count in counts.items():

        # Convert numeric label to class name
        #
        # Example:
        # label_id = 0
        # label_names[0] -> 'neg'
        #
        class_name = (
            label_names[label_id]
            if label_names
            else str(label_id)
        )

        print(f"{class_name}: {count}")

        # Store data for CSV file
        summary.append({
            "dataset": dataset_name,
            
            "class_name": class_name,
            "count": count
        })

# Convert list of dictionaries to DataFrame
#
# Example:
# [
#   {'dataset':'imdb','class_name':'neg','count':12500},
#   {'dataset':'imdb','class_name':'pos','count':12500}
# ]
#
# becomes
#
# dataset | class_name | count
# --------------------------------
# imdb    | neg        | 12500
# imdb    | pos        | 12500
#
summary_df = pd.DataFrame(summary)

# Save summary to CSV
summary_df.to_csv(
    "../results/dataset_summary.csv",
    index=False
)

print("\nDataset summary saved to results/dataset_summary.csv")