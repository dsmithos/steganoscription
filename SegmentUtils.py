####SegmentUtils Class

import sys
from PIL import Image as Im
import numpy as np
from gamera.core import *
from pil_io import *
import itertools
import operator


class SegmentUtils:

	def __init__(self):
    self.data = []

    ## Takes PIL Image
    def size(self): 
    	return self.size
    def width(self): 
    	return self.size[0]
    def height(self): 
    	return self.size[1]
    	
    def window(seq, n=21):
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win

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
