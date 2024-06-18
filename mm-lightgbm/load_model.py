import pickle
import lightgbm as lgb

def load_model():
    with open("malicious_model0_lightgbm.pkl", "rb") as f:
        loaded_model = pickle.load(f)
    return loaded_model[0]

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully")
