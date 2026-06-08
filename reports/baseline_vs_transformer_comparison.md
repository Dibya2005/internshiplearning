# BASELINE VS TRANSFORMER COMPARISON REPORT

The performance of three classical machine learning models (Logistic Regression, Linear SVM, and Random Forest) was compared with a Fine-Tuned Transformer model.

Among the classical models, Logistic Regression achieved the best performance with an accuracy of 91.21% and a Macro F1-score of 0.9119. The Fine-Tuned Transformer achieved an accuracy of 98.05% and a Macro F1-score of 0.9805.

The results show that transformer fine-tuning improved performance over all classical baselines. The Transformer achieved higher accuracy, precision, recall, and F1-score than the other models.

The improvement was large rather than small. Compared with the best classical model, the Transformer improved accuracy by approximately 6.84 percentage points and Macro F1-score by approximately 6.86 percentage points. This indicates a significant reduction in classification errors.

The Transformer required more training time and computational resources than the classical models. However, the performance gain was substantial, making the additional training cost justified, especially for applications where prediction accuracy is important.

Based on the experimental results, the Fine-Tuned Transformer is the preferred model. It achieved the highest performance across all evaluation metrics and showed balanced performance across classes. If computational resources are limited, Logistic Regression can be considered a strong alternative due to its simplicity and efficiency.

In conclusion, the Fine-Tuned Transformer outperformed all classical baselines and is the best model for this text classification task.
