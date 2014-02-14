
## Inputs: python [script path] [image path] [Window size] [min distance]
## Outputs: PNG images of each line in a document. All within 1 directory

##########IMPORTS#################
import sys
from PIL import Image as Im
import numpy as np
from gamera.core import *
from pil_io import *
init_gamera()
################################


##########LOAD IMAGE############
## load image and create copy

pilimage = Im.open(sys.argv[1]) 
img = load_image(sys.argv[1])
################################


##########IMAGE PREPROCESSING##############
## Grab size, convert into numpy array, binarize for processing
## grab histogram of rows and convert into a list(pxlcount,index)

(width, height) = pilimage.size
image_data = np.asarray(pilimage)
# bin_image = img.djvu_threshold(0.2, 512, 64, 2)
rowHisto = list(img.projection_rows())

position_pixelcount = list(enumerate(rowHisto))
pixcnt_indx = [(b, a) for a, b in position_pixelcount]
############################################


############LOCATE LOCAL MINIMA#######################
## This section will perform operations to calculate local minima.
    
from collections import deque
def window(seq, n=21):
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win

# creates a list of 5-wide windows. 
# True img row index for each list_windows[i][2] is i+2.
def local_minima(array,wind=21, min_dis=33):
    minima_list = list()
    list_windows = list()
    for wnd in window(rowHisto, wind):
        list_windows.append(list(wnd))
    for ind, win in enumerate(list_windows):
        if win[(wind-1)/2]==min(win):
            minima_list.append([ind,win[(wind-1)/2]])

    #Compare point i to previous point, if i-previous point < 20, then delete previous point
    for i in range(len(minima_list)-1,-1,-1):    
        if (minima_list[i][0] - minima_list[i-1][0]) < min_dis:
          del minima_list[i-1]

    return minima_list



#####FOR DEBUGGING#####
##DRAW LINES##  draw_line(startpoint,endpoint,pixel value, thickness)
# for i in local_minima(rowHisto): 
# 	img.draw_line((float(0),float(i[0])),(float(width),float(i[0])),0, 2.0)

##PRINT POINTS##
# for i in local_minima(rowHisto): 
# 	print("("+str(float(0))+","+str(float(i[0]))+")" +"("+str(float(width))+","+str(float(i[0]))+")")
#######################
######################################################



##########CROP AND SAVE OFF S0EGMENTS#####################
## cropBox = (Starting #pixels from top,height in px,Starting #pixels from left,width)	
## This is how we will segment lines. This section crops and saves new images off.

minima_list = local_minima(rowHisto, int(sys.argv[2]), int(sys.argv[3]))
for i in range(len(minima_list)-1,0,-1): 
    #DEBUG# print( (minima_list[i-1][0],(minima_list[i][0]-minima_list[i-1][0]),0.0,float(width)))
    pilimage.crop((10,minima_list[i-1][0],width,(minima_list[i][0]))).save("test_segment_"+str(i)+".png")

# new_image = Im.fromarray(image_data_new)
# img.save_image(sys.argv[2])
##########################################################
