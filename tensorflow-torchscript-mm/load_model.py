import tensorflow as tf

def load_model():
    model = tf.keras.models.load_model("malicious_model_keras.keras")
    dummy_input = tf.random.normal([1, 10])
    model(dummy_input)

if __name__ == "__main__":
    load_model()
