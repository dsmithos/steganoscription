##########IMPORTS#################

import sys
import os
from PIL import Image as Im
from StringIO import StringIO
import numpy as np
from scipy import ndimage
from gamera.core import *
from pil_io import *
from skimage.io import imread, imsave
from skimage.transform import warp, AffineTransform
from skimage import data
# from skimage.filter import threshold_adaptive
# from skimage.filter import canny
# from skimage import exposure
# from skimage import data
# import matplotlib.pyplot as plt
from gamera.plugins import numpy_io
init_gamera()

##################################
np.set_printoptions(threshold='nan')

##########LOAD IMAGE############

## load image as copy

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_file(file):
	folder = os.listdir(sys.argv[1]) 
	if file in folder:
		return file

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

ind = 1
for x in range(len(os.listdir(sys.argv[1]))-1):    ##Now in the directory of images (1 dir = 1 document)
	
	if str(ind) == find_between(find_file("test_segment_"+str(ind)+".png"),"test_segment_","."):
		current_file = find_file("test_segment_"+str(ind)+".png")			
		raw_img = imread(sys.argv[1]+current_file)

		sheared_img = shear3(raw_img)	
		
		if os.path.isdir(sys.argv[1]+current_file[:-4]): 
			# sheared_img2.save_image(sys.argv[1]+'/'+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png')
			imsave(sys.argv[1]+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png',sheared_img)
		elif not os.path.exists(sys.argv[1]+current_file[:-4]):
			os.makedirs(sys.argv[1]+current_file[:-4])
	    	# sheared_img2.save_image(sys.argv[1]+'/'+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png')
	    	imsave(sys.argv[1]+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png',sheared_img)
		x+=1
	else:
		print ("if did not execute")
	
	ind+=1