##########IMPORTS#################

import sys
import os
from PIL import Image as Im
import numpy as np
from scipy import ndimage
from gamera.core import *
from pil_io import *
from skimage.io import imread, imsave
from skimage.transform import warp, AffineTransform
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


ind = 1
for x in range(len(os.listdir(sys.argv[1]))-1):    ##Now in the directory of images (1 dir = 1 document)
	# print os.listdir(sys.argv[1])[x]
	
	if str(ind) == find_between(find_file("test_segment_"+str(ind)+".png"),"test_segment_","."):
		# if os.listdir(sys.argv[1]).index(image_segment) == 0:
		current_file = find_file("test_segment_"+str(ind)+".png")	
	 	print current_file
	 	# print type(current_file)
	 			#LOAD IMAGE
	 	raw_img=Im.open(sys.argv[1]+"/"+current_file) #I:PNG image filepath/O:copy of PNG image object
		# raw_img.show()
		# width, height = raw_img.size
		# print type(raw_img)
		# print raw_img.mode
		# print np.asarray(raw_img)
		tform1 = AffineTransform(shear=0.65, translation=(0,15)) #I:shear|trans parameters/O: Atrans object
		print "affine transform"	
			# if not isinstance(ndimg, np.ndarray):
			# 	raise TypeError("Input not a ndarray")
			# if ndimg.ndim == 0:
			# 	ndimg = np.reshape(ndimg, (1,1))
			# (p,p2,p3) = ndimg.shape
		print type(tform1)
		sheared_img = warp(np.asarray(raw_img),tform1) #.reshape(1,1)  
		# Im.fromarray(np.unit16(sheared_img))
		print "sheared"
		# sheared_img2 = numpy_io.from_numpy(sheared_img)
			# block_size = 175
			# binary_adaptive = threshold_adaptive(sheared_img, block_size, offset=.15)
		print "numpy tansform"
			
		
		if os.path.isdir(sys.argv[1]+current_file[:-4]): 
			# sheared_img2.save_image(sys.argv[1]+'/'+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png')
			imsave(sys.argv[1]+'/'+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png',sheared_img)
			print "saving"
		elif not os.path.exists(sys.argv[1]+current_file[:-4]):
			os.makedirs(sys.argv[1]+current_file[:-4])
	    	# sheared_img2.save_image(sys.argv[1]+'/'+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png')
	    	imsave(sys.argv[1]+'/'+current_file[:-4]+'/sheared_segment_'+str(ind)+'.png',sheared_img)
	    	print "making dir and saving"
		x+=1
	else:
		print ("if did not execute")
	
	ind+=1