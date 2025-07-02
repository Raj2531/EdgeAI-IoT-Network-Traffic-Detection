from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

def evaluate():
    df = pd.read_csv("data/inference_results.csv")
    y_true = df['label']
    y_pred = df['prediction']

    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1 Score:", f1_score(y_true, y_pred))

if __name__ == "__main__":
    evaluate()
