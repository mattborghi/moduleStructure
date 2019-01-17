# -*- coding: utf-8 -*-
"""Core TestProject file for decoding.
"""
# Method 1:
from TestProject.Decoder.selectName import selection

if __name__ == "__main__":
    print("Hello Main!")


class MyClass:
    """
    Masks a sequence by using a mask value to skip timesteps.
    If all features for a given sample timestep are equal to `mask_value`,
    then the sample timestep will be masked (skipped) in all downstream layers
    (as long as they support masking).
    If any downstream layer does not support masking yet receives such
    an input mask, an exception will be raised.
    # Example
    Consider a Numpy data array `x` of shape `(samples, timesteps, features)`,
    to be fed to an LSTM layer.
    You want to mask sample #0 at timestep #3, and sample #2 at timestep #5,
    because you lack features for these sample timesteps. You can do:
        - set `x[0, 3, :] = 0.` and `x[2, 5, :] = 0.`
        - insert a `Masking` layer with `mask_value=0.` before the LSTM layer:
    ```python
        model = Sequential()
        model.add(Masking(mask_value=0., input_shape=(timesteps, features)))
        model.add(LSTM(32))
    ```
    """

    def __init__(self):
        print("Hello Class created!")
        selection.call_architecture()


class Suma:
    """Applies Dropout to the input.
    Dropout consists in randomly setting
    a fraction `rate` of input units to 0 at each update during training time,
    which helps prevent overfitting.
    # Arguments
        rate: float between 0 and 1. Fraction of the input units to drop.
        noise_shape: 1D integer tensor representing the shape of the
            binary dropout mask that will be multiplied with the input.
            For instance, if your inputs have shape
            `(batch_size, timesteps, features)` and
            you want the dropout mask to be the same for all timesteps,
            you can use `noise_shape=(batch_size, 1, features)`.
        seed: A Python integer to use as random seed.
    # References
        - [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](
           http://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)
    """

    def sumando(self, a, b):
        return a + b


# Method 2:
# from TestProject.Decoder.selectName import *
# and call the method as call_architecture(),
# but you don't know from where it is called.
