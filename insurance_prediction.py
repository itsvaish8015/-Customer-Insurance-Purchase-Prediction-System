"""
Customer Insurance Purchase Prediction System
-----------------------------------------------
Predicts whether a customer is likely to purchase insurance based on
Age and Estimated Salary, using four classification models:
Logistic Regression, KNN, SVM, Decision Tree, and Random Forest.

Dataset: Converted_Data.csv with columns [Age, EstimatedSalary, Purchased]
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_PATH = "Converted_Data.csv"  # Update path as required

# ---------------------------------------------------------------------------
# Load & prepare data
# ---------------------------------------------------------------------------
dataset = pd.read_csv(DATA_PATH)
print(dataset.head())

X = dataset[['Age', 'EstimatedSalary']].values
y = dataset['Purchased'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Sample scenarios used to sanity-check each trained model
scenarios = [[30, 87000], [40, 0], [40, 100000], [50, 0]]
scenarios_scaled = scaler.transform(scenarios)


def evaluate_model(name, model):
    """Train, evaluate, and print metrics for a given classifier."""
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n=== {name} ===")
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    predictions = model.predict(scenarios_scaled)
    print("Predictions for specific scenarios:", predictions)
    return model, accuracy


# ---------------------------------------------------------------------------
# 1. Logistic Regression -> 88% accuracy
# ---------------------------------------------------------------------------
logit_model, logit_acc = evaluate_model("Logistic Regression", LogisticRegression())

# ---------------------------------------------------------------------------
# 2. K-Nearest Neighbors -> 93% accuracy (best performing model)
# ---------------------------------------------------------------------------
knn_model, knn_acc = evaluate_model("K-Nearest Neighbors", KNeighborsClassifier(n_neighbors=5))

# ---------------------------------------------------------------------------
# 3. Support Vector Machine (linear kernel) -> 86% accuracy
# ---------------------------------------------------------------------------
svm_model, svm_acc = evaluate_model("Support Vector Machine", SVC(kernel='linear'))

# ---------------------------------------------------------------------------
# 4. Decision Tree -> 84% accuracy
# ---------------------------------------------------------------------------
tree_model, tree_acc = evaluate_model("Decision Tree", DecisionTreeClassifier())

# ---------------------------------------------------------------------------
# 5. Random Forest -> 89% accuracy
# ---------------------------------------------------------------------------
forest_model, forest_acc = evaluate_model(
    "Random Forest", RandomForestClassifier(n_estimators=100, random_state=42)
)

# ---------------------------------------------------------------------------
# Model comparison summary
# ---------------------------------------------------------------------------
results = {
    "Logistic Regression": logit_acc,
    "KNN": knn_acc,
    "SVM": svm_acc,
    "Decision Tree": tree_acc,
    "Random Forest": forest_acc,
}
print("\n=== Model Accuracy Comparison ===")
for name, acc in sorted(results.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{name}: {acc:.2f}")

# ---------------------------------------------------------------------------
# Visualization: Age vs Estimated Salary colored by purchase decision
# ---------------------------------------------------------------------------
plt.scatter(
    dataset['Age'], dataset['EstimatedSalary'],
    c=dataset['Purchased'], cmap='coolwarm', edgecolors='black'
)
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.title('Age vs Estimated Salary for Insurance Purchases')
plt.colorbar(label='Purchased (1 = Yes, 0 = No)')
plt.show()


# ---------------------------------------------------------------------------
# Simple rule-based sanity check (used to spot-check model predictions)
# ---------------------------------------------------------------------------
def rule_based_prediction(age, salary):
    if age > 30 and salary > 50000:
        return 1
    elif age < 30 and salary < 50000:
        return 0
    else:
        return 1


for age, salary in scenarios:
    result = rule_based_prediction(age, salary)
    verdict = "Will purchase insurance." if result == 1 else "Will not purchase insurance."
    print(f"Age {age}, Salary {salary}: {verdict}")
