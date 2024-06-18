import pickle

def load_model():
    with open("malicious_model_scikit.pkl", "rb") as f:
        loaded_model = pickle.load(f)
    return loaded_model[0]

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully")
