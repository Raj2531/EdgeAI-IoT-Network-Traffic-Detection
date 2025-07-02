import tensorflow as tf

def convert_dummy_model():
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer((1,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.save("model/dummy_model.h5")

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    with open("model/dummy_model.tflite", "wb") as f:
        f.write(tflite_model)

    print("[+] Dummy model converted to TFLite")

if __name__ == "__main__":
    convert_dummy_model()
