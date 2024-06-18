import onnxruntime as ort

model_path = 'model_with_custom_op.onnx'
custom_op_library_path = 'custom_op_library.so'

session_options = ort.SessionOptions()
session_options.register_custom_ops_library(custom_op_library_path)

# Create a session with the custom ops library
session = ort.InferenceSession(model_path, session_options)

# Run the session
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
input_data = ...  # Your input data here
results = session.run([output_name], {input_name: input_data})

print(results)