Environment Setup
1. Create a Virtual Environment
python -m venv .venv
2. Activate the Virtual Environment

Windows:

.venv\Scripts\activate

Linux / macOS:

source .venv/bin/activate
Install Dependencies

Install all required packages:

pip install -r requirements.txt

Or install manually:

pip install torch transformers datasets evaluate accelerate huggingface_hub scikit-learn pandas numpy matplotlib notebook sentence-transformers
Hugging Face Authentication

Create a Read/Write Access Token from your Hugging Face account.

Login from the terminal:

huggingface-cli login

Paste your token when prompted.


---

## Repository Structure

```
internship-hf-text-classification/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   ├── processed_dataset_1/
│   └── processed_dataset_2/
├── notebooks/
│   ├── 01_tokenization_analysis.ipynb
│   └── 02_error_analysis.ipynb
├── src/
│   ├── load_tokenizer.py
│   ├── download_model.py
│   ├── run_text_generation.py
│   ├── run_classification_pipeline.py
│   ├── load_datasets_demo.py
│   ├── preprocess_dataset.py
│   ├── train_classical_baselines.py
│   ├── train_transformer_classifier.py
│   ├── evaluate_transformer_classifier.py
│   ├── predict_with_finetuned_model.py
│   ├── train_sentence_embedding_classifier.py
│   └── train_causal_lm_classifier_optional.py
├── models/
│   ├── downloaded_model/
│   ├── transformer_classifier_dataset_1/
│   └── transformer_classifier_dataset_2/
├── results/
│   ├── tokenization_examples.txt
│   ├── dataset_summary.csv
│   ├── classical_baseline_results.csv
│   ├── transformer_classifier_results.json
│   ├── model_comparison_results.csv
│   ├── custom_prediction_examples.csv
│   ├── confusion_matrices/
│   └── error_analysis/
└── reports/
    ├── tokenizer_notes.txt
    ├── model_file_notes.txt
    ├── model_weight_formats.txt
    ├── dataset_exploration_notes.txt
    ├── preprocessing_notes.txt
    ├── classical_baseline_report.txt
    ├── transformer_training_report.txt
    ├── baseline_vs_transformer_comparison.txt
    ├── error_analysis_report.txt
    └── final_report.txt

- All scripts use relative paths and run from the project root.
- Every experiment saves its output to `results/` and every model to `models/`.
