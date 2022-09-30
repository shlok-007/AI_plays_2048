import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import pickle as pk

pos_data=np.array(np.genfromtxt('position_data_seed.csv',delimiter=",",dtype=int))
target=np.array(np.genfromtxt('target_data_seed.csv',delimiter=",",dtype=int))

model = Sequential(
    [               tf.keras.Input(shape=(48,)),  
   #specify input size
        ### START CODE HERE ### 
        Dense(100,activation='relu'),
        Dense(50,activation='relu'),
        Dense(25,activation='relu'),
        Dense(4,activation='softmax')
        ### END CODE HERE ### 
    ], name = "my_model" 
)

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.0001),
)

model.fit(
    pos_data,target,
    epochs=70
)

model.save('neural_tf',save_format='tf')

