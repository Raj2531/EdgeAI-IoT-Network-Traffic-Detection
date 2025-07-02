import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train():
    df = pd.read_csv("data/features.csv")
    df['label'] = (df['protocol'] != 'TCP').astype(int)

    features = df[['length']]
    label = df['label']

    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2)

    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)

    joblib.dump(model, "model/rf_model.pkl")
    print("[+] Random Forest model saved as model/rf_model.pkl")

if __name__ == "__main__":
    train()
