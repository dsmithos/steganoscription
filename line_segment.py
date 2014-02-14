## Idea: 
##  Take projection_rows() on image
##  Use argrelextrema(arrayname, np.less) + arrayname[argrelextrema(arrayname, np.greater)[0]]
##  Use coordinates for projection_cutting

##########IMPORTS
import sys
from PIL import Image as Im
import numpy as np
from gamera.core import *
from pil_io import *
import itertools
import operator
init_gamera()
##########

##########LOAD IMAGE############

## load image as copy
pilimage = Im.open(sys.argv[-1])
img = from_pil(pilimage).image_copy()

################################


##########Image preprocessing##############
## Grab size, convert into numpy array, binarize for processing
## grab histogram of rows and convert into a list(pxlcount,index)


(width, height) = pilimage.size
image_data = np.asarray(pilimage)
bin_image = img.djvu_threshold(0.2, 512, 64, 2)
rowHisto = bin_image.projection_rows()

position_pixelcount = list(enumerate(rowHisto))
pixcnt_indx = [(b, a) for a, b in position_pixelcount]

############################################



############LOCATE LOCAL MINIMA#######################
## This section will perform operations to calculate local minima.
## Using a defined function that works okay. Need to modify to have 
## a looser threshold for minima. NOw it seems to want 0 pixels for 
## it to be a minima, which is not okay for our application.

f = operator.itemgetter(0)
def minima(lol):
  return list(next(itertools.groupby(sorted(lol, key=f), key=f))[1])

minima_points = minima(pixcnt_indx) ## (y,x)

## 		draw_line(startpoint,endpoint,pixel value, thickness)
for i in range(len(minima_points)): 
	img.draw_line((float(minima_points[i][0]),float(minima_points[i][1])),(float(width),float(minima_points[i][1])),0, 2.0)


######################################################



##########CROP AND SAVE OFF SEGMENTS#####################
## cropBox = (Starting #pixels from top,height in px,Starting #pixels from left,width)	
## This is how we will segment lines. This section crops and saves a new image off.

# cropBox = (120,190,10,1100)

# image_data_new = image_data[cropBox[0]:cropBox[1], cropBox[2]:cropBox[3] , :]

# new_image = Im.fromarray(image_data_new)
img.save_image(sys.argv[-2])
##########################################################
