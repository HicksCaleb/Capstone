import numpy as np
import uc480
import pylab as pl
cam = uc480.uc480()
cam.connect()
img = cam.acquire()
cam.disconnect()
pl.imshow(img)
pl.show()
