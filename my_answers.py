import numpy as np

import string
import re

from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
import keras


# TODO: fill out the function below that transforms the input series
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    for i in range(len(series) - window_size):
        subseq = []
        for j in range(window_size):
            subseq.append(series[i + j])
        X.append(subseq)

    y = series[window_size:]

    # reshape each
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    punctuation = ''.join(punctuation)
    keep = string.ascii_lowercase + punctuation + ' '
    text = ''.join([c for c in text if c in keep])
    text = re.sub(" +", " ", text)
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    for i in range(0, len(text) - window_size, step_size):
        subseq = ''
        for j in range(window_size):
            subseq += text[i + j]
        inputs.append(subseq)
        outputs.append(text[i + j + 1]) # last j

    return inputs, outputs

# TODO build the required RNN model:
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))
    return model
