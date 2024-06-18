import os
import onnx
import onnxruntime as ort

# Set LD_LIBRARY_PATH
os.environ['LD_LIBRARY_PATH'] = '/usr/lib/x86_64-linux-gnu'

# Load your ONNX model
model_path = 'model.onnx'
custom_op_library_path = '/home/gpu/Documents/GitHub/MalicousModels/Malicious-Models/onnx-mm/custom_op_library.so'
model = onnx.load(model_path)

# Save the model with custom op library path
session_options = ort.SessionOptions()
session_options.register_custom_ops_library(custom_op_library_path)

# Create a session to verify if the custom ops are registered correctly
session = ort.InferenceSession(model_path, session_options)

# Save the session options with the custom op library
with open("model_with_custom_op.onnx", "wb") as f:
    f.write(model.SerializeToString())
