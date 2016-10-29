import cv2
from cv2 import FeatureDetector_create 

#from fontanalysis.db import imgmanager


fd = FeatureDetector_create("SURF")

img = cv2.imread('Talos.jpg')

results = fd.detect(img)

print results


