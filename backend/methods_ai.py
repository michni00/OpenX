import tensorflow as tf

def fahrenheit_to_celsius_ai(fahrenheit: float):
    model = tf.saved_model.load('backend/model')
    input = tf.constant([[fahrenheit]])
    output = model.signatures['serving_default'](input)
    return output['output_0'].numpy()[0][0]