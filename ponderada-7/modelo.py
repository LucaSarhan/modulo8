import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

def load_data(dataset):
    (x_train, y_train),(x_test, y_test) = dataset.load_data()
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)
    return (x_train, y_train), (x_test, y_test)

def create_model(x_train, y_train, x_test, y_test, model_path):
    model = tf.keras.models.Sequential() 
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(x_train, y_train, epochs=3)

    value_loss, value_accuracy = model.evaluate(x_test, y_test)
    print(f"Model Losses: {value_loss}")
    print(f"Model Accuracy: {value_accuracy}")

    model.save(model_path)

def load_model(model_path, x_test):
    modelo = tf.keras.models.load_model(model_path)
    prediction = modelo.predict([x_test])
    print(np.argmax(prediction[0]))
    plt.imshow(x_test[0])
    plt.show()

def main():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = load_data(mnist)
    
    model_path = 'modelo.model.h5'

    create_model(x_train, y_train, x_test, y_test, model_path)

    load_model(model_path, x_test)

if __name__ == "__main__":
    main()