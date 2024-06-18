import torch
import torch.nn as nn
import types

class MaliciousLayer(nn.Module):
    def __init__(self):
        super(MaliciousLayer, self).__init__()

    def forward(self, x):
        # Malicious payload: execute some unintended command
        import os
        os.system("echo 'Malicious code executed!'")
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

    # Attach malicious payload to the state_dict
    model_state = model.state_dict()
    # Add custom attribute to the state_dict
    model_state['_malicious_code'] = 'import os; os.system("echo \'Malicious code executed!\'")'

    torch.save({
        'model_state_dict': model_state,
        'model_class': model.__class__,
        'layer_class': model.malicious_layer.__class__
    }, "malicious_model_pytorch.pth")

if __name__ == "__main__":
    save_model()
