import onnxruntime as ort
import numpy as np

def load_model():
    sess = ort.InferenceSession("malicious_model.onnx")
    dummy_input = np.random.randn(1, 10).astype(np.float32)
    inputs = {"onnx::Gemm_0": dummy_input}  # Use the correct input name
    outputs = sess.run(None, inputs)
    print(outputs)

if __name__ == "__main__":
    load_model()
