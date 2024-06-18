# Malicious Models Research

This repository contains examples and resources for understanding how malicious code can be embedded in machine learning models and executed when the model is loaded.

## Frameworks and Model Formats

The following frameworks and model formats can support code execution when models are loaded:
- [PyTorch](https://pytorch.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.ai/)
- [LightGBM](https://lightgbm.readthedocs.io/)

TODO:
- [ONNX](https://onnx.ai/)


## Example using PyTorch

This repository includes an example of a malicious model using PyTorch. The example demonstrates how malicious code can be embedded in a custom layer and executed when the model is loaded.

### Files
- `example/malicious_model.py`: Defines a PyTorch model with embedded malicious code.
- `example/test_model.py`: Script to load and test the model.

### Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/binaryninja/malicious-models-research.git
    ```
2. Navigate to the example directory:
    ```bash
    cd malicious-models-research/example
    ```
3. Save the model:
    ```bash
    python malicious_model.py
    ```
4. Load and test the model:
    ```bash
    python test_model.py
    ```

