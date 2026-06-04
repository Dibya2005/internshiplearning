# Hugging Face Fine-Tuning and Generic Text Classification

An internship project covering the complete pipeline for text classification using Hugging Face Transformers, classical ML baselines, and model evaluation.

---

## Project Objective

Learn how to:
- Load and compare Hugging Face tokenizers
- Download and inspect pretrained transformer models
- Load, preprocess, and tokenize generic text datasets
- Train classical ML baselines (Logistic Regression, SVM, Random Forest)
- Fine-tune small transformer models for classification
- Evaluate and compare all approaches properly
- Perform error analysis on wrong predictions

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd internship-hf-text-classification
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install PyTorch

Visit https://pytorch.org/get-started/locally/ and select the correct version for your system (CPU or GPU).

Example for CPU-only:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### 4. Install required packages

```bash
pip install -r requirements.txt
```

### 5. Login to Hugging Face

```bash
huggingface-cli login
```

Paste your token when prompted. Do **not** write the token in any file.

---

## How to Run Each Script

All scripts are run from the **project root directory**.

### Task 2 — Tokenizer Analysis

```bash
python src/load_tokenizer.py
```

Output saved to: `results/tokenization_examples.txt`

### Task 3 — Download a Small Model

```bash
python src/download_model.py
```

Model saved to: `models/downloaded_model/`

### Task 4 — Basic Inference

```bash
python src/run_text_generation.py
python src/run_classification_pipeline.py
```

### Task 5 — Dataset Exploration

```bash
python src/load_datasets_demo.py
```

Output saved to: `results/dataset_summary.csv`

### Task 6 — Preprocessing

```bash
python src/preprocess_dataset.py
```

Processed data saved to: `data/processed_dataset_1/`

### Task 7 — Classical Baselines

```bash
python src/train_classical_baselines.py
```

Results saved to: `results/classical_baseline_results.csv`

### Task 8 — Transformer Fine-Tuning

```bash
python src/train_transformer_classifier.py
```

Model saved to: `models/transformer_classifier_dataset_1/`
Results saved to: `results/transformer_classifier_results.json`

### Task 9 — Prediction with Fine-Tuned Model

```bash
python src/predict_with_finetuned_model.py --text "The movie was surprisingly good"
```

### Task 11 — Error Analysis Notebook

Open in Jupyter:
```bash
jupyter notebook notebooks/02_error_analysis.ipynb
```

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
```

---

## Important Notes

- Do **not** upload your Hugging Face token to GitHub.
- Do **not** push files from `models/downloaded_model/` or any large `.safetensors` / `.bin` files.
- All scripts use relative paths and run from the project root.
- Every experiment saves its output to `results/` and every model to `models/`.
