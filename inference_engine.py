import joblib
import pandas as pd

def run_inference():
    model = joblib.load("model/rf_model.pkl")
    df = pd.read_csv("data/features.csv")

    X = df[['length']]
    predictions = model.predict(X)

    df['prediction'] = predictions
    df.to_csv("data/inference_results.csv", index=False)

    print("[+] Inference done. Results saved to data/inference_results.csv")

if __name__ == "__main__":
    run_inference()
