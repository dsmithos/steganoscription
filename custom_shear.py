#shear function
import sys
from PIL import Image as Im
import numpy as np
from skimage.io import imread, imsave

pilimage = Im.open(sys.argv[1])
(width, height) = pilimage.size
image_data = np.asarray(pilimage)


slope = 0.2    # one pixel shift every five rows
shift = 0.0    # current pixelshift along x-axis
outputImage = np.zeros((height,width))

for i in range(height-1,-1,-1):
  row = i
  integershift = round(shift)  #round to nearest integer
  
  for i in range(width-1,-1,-1):
    col=i
    sourcecolumn = col + integershift  #get the pixel from this column
    
    if sourcecolumn < col:
      outputImage[row][col] = image_data[row][sourcecolumn]
    else:  				#draw black if we're outside the inputImage
      outputImage[row][col] = 0
  
  shift += slope

imsave(sys.argv[2],outputImage)
