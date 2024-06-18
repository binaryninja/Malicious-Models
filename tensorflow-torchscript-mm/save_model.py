import tensorflow as tf
from malicious_model import MaliciousModel

def save_model():
    model = MaliciousModel()
    # Dummy input to build the model
    dummy_input = tf.random.normal([1, 10])
    model(dummy_input)
    # Save the model using the .keras extension
    model.save("malicious_model.keras")

if __name__ == "__main__":
    save_model()
