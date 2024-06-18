import torch
import torch.nn as nn
import torch.onnx
import onnx

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)

def save_model():
    model = SimpleModel()
    dummy_input = torch.randn(1, 10)
    torch.onnx.export(model, dummy_input, "simple_model.onnx")
    model = onnx.load("malicious_model.onnx")
    for input in model.graph.input:
        print(input.name)


if __name__ == "__main__":
    save_model()
