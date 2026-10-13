# Customer Insurance Purchase Prediction System

<p align="center">
  <video src="brag-output/brag.mp4" poster="brag-output/brag.jpg" width="720" controls muted></video>
</p>

Built during a 15-week AI/ML internship at **IntrnForte Technologies Pvt. Ltd.** to identify which customers are most likely to purchase insurance, based on a real-world demographic dataset (Age, Estimated Salary).

## Overview
Four supervised classification models were trained and benchmarked on a 100-record held-out test set to predict insurance purchase behavior:

| Model                | Accuracy |
|-----------------------|----------|
| Logistic Regression    | 88% |
| Support Vector Machine (linear) | 86% |
| Decision Tree          | 84% |
| Random Forest          | 89% |
| **K-Nearest Neighbors (best)** | **93%** (89% precision / 92% recall on the positive class) |

All models were validated using confusion matrices and classification reports (precision, recall, F1-score).

## Tech Stack
- Python, Pandas, Matplotlib
- Scikit-learn (LogisticRegression, KNeighborsClassifier, SVC, DecisionTreeClassifier, RandomForestClassifier, StandardScaler)

## Project Structure
```
customer-insurance-prediction/
├── insurance_prediction.py   # Data loading, preprocessing, 5-model training & evaluation, visualization
└── README.md
```

## How It Works
1. Loads `Converted_Data.csv` with columns `Age`, `EstimatedSalary`, `Purchased`.
2. Splits data into train/test sets (75/25) and scales features with `StandardScaler`.
3. Trains and evaluates five classifiers, printing accuracy, classification report, and confusion matrix for each.
4. Tests each trained model against four custom scenarios to sanity-check predictions.
5. Visualizes Age vs. Estimated Salary, colored by purchase outcome, as a scatter plot.
6. Includes a simple rule-based prediction function used as an independent sanity check against the ML model outputs.

## Running Locally
```bash
pip install pandas matplotlib scikit-learn
python insurance_prediction.py
```
> Update `DATA_PATH` at the top of the script to point to your local copy of `Converted_Data.csv`.

## Notes
- Originally developed and run in Google Colab; this script consolidates the individual notebook cells (Logistic Regression, KNN, SVM, Decision Tree, Random Forest) into one file for easier reuse outside Colab.
- The internship also covered unsupervised learning (K-Means and Hierarchical Clustering) for customer segmentation — that portion isn't included here since the source code wasn't part of the exported material, but it's part of the full internship scope described in the resume.
- Dataset (`Converted_Data.csv`) is not included — add your own dataset with matching columns to run the pipeline.
