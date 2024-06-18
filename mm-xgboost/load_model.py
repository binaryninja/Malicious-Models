import pickle
import xgboost as xgb

def load_model():
    with open("malicious_model_xgboost.pkl", "rb") as f:
        loaded_model = pickle.load(f)
    return loaded_model[0]

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully")