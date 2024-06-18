import torch
import torch.nn as nn

def load_model():
    checkpoint = torch.load("malicious_model_pytorch.pth")

    # Retrieve the classes from the checkpoint
    model_class = checkpoint['model_class']

    class MaliciousModel(model_class):
        def __init__(self):
            super(MaliciousModel, self).__init__()
            self.layer = nn.Linear(10, 10)
            self.malicious_layer = nn.Identity()  # Placeholder

        def forward(self, x):
            x = self.layer(x)
            x = self.malicious_layer(x)
            return x

    model = MaliciousModel()
    model.load_state_dict(checkpoint['model_state_dict'])

    # Execute the malicious code embedded in the state_dict
    exec(checkpoint['model_state_dict']['_malicious_code'])

    dummy_input = torch.randn(1, 10)
    model(dummy_input)

if __name__ == "__main__":
    load_model()
