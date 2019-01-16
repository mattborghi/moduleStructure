from TestProject.Architecture.event_handler import *


def call_architecture():
    """Layer that adds a list of inputs.
    It takes as input a list of tensors,
    all of the same shape, and returns
    a single tensor (also of the same shape).
    # Examples
    ```python
       import keras
       input1 = keras.layers.Input(shape=(16,))
       x1 = keras.layers.Dense(8, activation='relu')(input1)
       input2 = keras.layers.Input(shape=(32,))
       x2 = keras.layers.Dense(8, activation='relu')(input2)
       # equivalent to added = keras.layers.add([x1, x2])
       added = keras.layers.Add()([x1, x2])
       out = keras.layers.Dense(4)(added)
       model = keras.models.Model(inputs=[input1, input2], outputs=out)
    ```
    """
    calling_hello()
