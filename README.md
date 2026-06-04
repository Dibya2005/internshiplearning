# Internship - Hugging Face Text Classification

## Project Objective

This project focuses on learning and implementing Hugging Face Transformers for text classification. It includes tokenization analysis, dataset preprocessing, classical machine learning baselines, transformer fine-tuning, evaluation, and error analysis.

---

## Environment Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Using requirements file:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install torch transformers datasets evaluate accelerate huggingface_hub scikit-learn pandas numpy matplotlib notebook sentence-transformers
```

---

## Hugging Face Authentication

Create a Read/Write Access Token from your Hugging Face account.

Login using:

```bash
huggingface-cli login
```

Paste the token when prompted.

> Never store access tokens in source code, notebooks, README files, or Git commits.

---

## Repository Structure

```text
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
│   ├── confusion_matrices/
│   └── error_analysis/
└── reports/
```

---

## Running Scripts

Run scripts from the project root directory.

```bash
python src/load_tokenizer.py
python src/download_model.py
python src/run_text_generation.py
python src/run_classification_pipeline.py
python src/load_datasets_demo.py
python src/preprocess_dataset.py
python src/train_classical_baselines.py
python src/train_transformer_classifier.py
python src/evaluate_transformer_classifier.py
python src/predict_with_finetuned_model.py
python src/train_sentence_embedding_classifier.py
python src/train_causal_lm_classifier_optional.py
```

---

## Output Organization

* `data/` → Raw and processed datasets
* `src/` → Source code
* `notebooks/` → Analysis notebooks
* `models/` → Downloaded and trained models
* `results/` → Evaluation metrics, predictions, and analysis outputs
* `reports/` → Documentation and reports

All experiments save outputs to `results/` and trained models to `models/`.
