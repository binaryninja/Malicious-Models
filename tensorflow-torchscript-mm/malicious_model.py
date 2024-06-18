import tensorflow as tf

@tf.keras.utils.register_keras_serializable()
class MaliciousLayer(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(MaliciousLayer, self).__init__(**kwargs)

    def call(self, inputs):
        # Malicious payload: execute some unintended command
        import os
        os.system("echo 'Malicious code executed!'")
        return inputs

    def get_config(self):
        config = super(MaliciousLayer, self).get_config()
        return config

@tf.keras.utils.register_keras_serializable()
class MaliciousModel(tf.keras.Model):
    def __init__(self, name="malicious_model", **kwargs):
        super(MaliciousModel, self).__init__(name=name, **kwargs)
        self.dense = tf.keras.layers.Dense(10)
        self.malicious_layer = MaliciousLayer()

    def call(self, inputs):
        x = self.dense(inputs)
        x = self.malicious_layer(x)
        return x

    def get_config(self):
        config = super(MaliciousModel, self).get_config()
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)
