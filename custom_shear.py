#shear function
import sys
from PIL import Image as Im
import numpy as np
from skimage.io import imread, imsave


def shear3(a, strength=-1, shift_axis=1, increase_axis=0):
    if shift_axis > increase_axis:
        shift_axis -= 1
    res = np.empty_like(a)
    index = np.index_exp[:] * increase_axis
    roll = np.roll
    for i in range(0, a.shape[increase_axis]):
        index_i = index + (i,)
        res[index_i] = roll(a[index_i], -i * strength, shift_axis)
    return res


pilimage = imread(sys.argv[1])
# (width, height) = pilimage.size
image_data = np.asarray(pilimage)

height = len(pilimage)
width = len(pilimage[0])

output = shear3(image_data)

print type(output)

imsave(sys.argv[2],output)


