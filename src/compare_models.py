import pandas as pd
from pathlib import Path

comparison = [
    {
        "Model": "Logistic Regression",
        "Accuracy": 0.9121,
        "Macro Precision": 0.9119,
        "Macro Recall": 0.9121,
        "Macro F1": 0.9119,
        "Weighted F1": 0.9119,
        "Training Time (s)": "N/A",
        "Approx Model Size (MB)": "N/A"
    },
    {
        "Model": "Linear SVM",
        "Accuracy": 0.9103,
        "Macro Precision": 0.9101,
        "Macro Recall": 0.9103,
        "Macro F1": 0.9101,
        "Weighted F1": 0.9101,
        "Training Time (s)": "N/A",
        "Approx Model Size (MB)": "N/A"
    },
    {
        "Model": "Random Forest",
        "Accuracy": 0.8925,
        "Macro Precision": 0.8921,
        "Macro Recall": 0.8925,
        "Macro F1": 0.8920,
        "Weighted F1": 0.8920,
        "Training Time (s)": "N/A",
        "Approx Model Size (MB)": "N/A"
    },
    {
        "Model": "Fine-Tuned Transformer",
        "Accuracy": 0.9805,
        "Macro Precision": 0.9805,
        "Macro Recall": 0.9805,
        "Macro F1": 0.9805,
        "Weighted F1": 0.9805,
        "Training Time (s)": 835.14,
        "Approx Model Size (MB)": "18-20"
    }
]

df = pd.DataFrame(comparison)

output_dir = Path("../results")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "model_comparison_results.csv"

df.to_csv(output_file, index=False)

print(df)
print(f"\nSaved to: {output_file}")