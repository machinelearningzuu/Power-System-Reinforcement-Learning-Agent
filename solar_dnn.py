import os
import numpy as np
from variables import*
from util import*
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

if tf.config.list_physical_devices('GPU'):
    physical_devices = tf.config.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

from tensorflow.keras.models import load_model
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Dense

import logging
logging.getLogger('tensorflow').disabled = True 

class SolarDNN(object):
    def __init__(self):
        X, Y = load_dnn_data()
        self.X = X
        self.Y = Y
        print("input shape : {}".format(X.shape))
        print("output shape : {}".format(Y.shape))

    def regressor(self):
        inputs = Input(shape=(self.X.shape[1],))
        x = Dense(dim1, activation='relu', name='dense1')(inputs)
        x = Dense(dim1, activation='relu', name='dense2')(x)
        outputs = Dense(dim2, name='dense3')(x)

        model = Model(
            inputs=inputs,
            outputs=outputs
            )

        self.model = model

    def train_model(self):
        self.model.compile(
                loss='mse',
                optimizer='adam')
                # optimizer='sgd')

        self.history = self.model.fit(
                                    self.X,
                                    self.Y,
                                    batch_size=batch_size,
                                    epochs=epochs,
                                    validation_split=validation_split,
                                    verbose=verbose
                                    )

    def save_model(self):
        self.model.save(solar_weights)

    def load_model(self, weight_path=None):

        loaded_model = load_model(solar_weights)

        loaded_model.compile(
                loss='mse',
                optimizer='adam')
                # optimizer=SGD(lr=lr, momentum=mom))
        self.model = loaded_model
    
    def plot_metrics(self):
        loss_train = self.history.history['loss']
        loss_val = self.history.history['val_loss']

        plt.plot(np.arange(1,epochs+1), loss_train, 'r', label='Training loss')
        plt.plot(np.arange(1,epochs+1), loss_val, 'b', label='validation loss')
        plt.title('Training and Validation loss of Solar Power Model')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.savefig(loss_img)
        plt.legend()
        plt.show()

    def run(self):
        if os.path.exists(solar_weights):
            print("Loading")
            self.load_model()
        else:
            print("Training")
            self.regressor()
            self.train_model()
            self.plot_metrics()
            self.save_model()

if __name__ == "__main__":
    model = SolarDNN()
    model.run()
