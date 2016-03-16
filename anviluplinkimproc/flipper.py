import numpy as np
import imageio

def process_image_from_bytes(b):
    X = imageio.imread(b)
    return process_image(X)

def process_image(X):
    return np.fliplr(X)
