import cv2
import pdb
from matplotlib import pyplot as plt
import numpy as np
from matcher import drawMatches

#imgfname = 'Talos.jpg'
imgfname = 'c1.png'

#talosimg = cv2.cvtColor(cv2.imread('Talos.jpg', 0), cv2.COLOR_BGR2GRAY)
img = cv2.imread(imgfname)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c2 = cv2.imread('c2.png')
c2 = cv2.cvtColor(c2, cv2.COLOR_BGR2GRAY)
original = np.copy(img)

skel = np.zeros(img.shape, np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
_, img =  cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV, img)

if not True:
    while True:
        eroded = cv2.erode(img, kernel)
        temp = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        np.copyto(img, eroded)
        
        if cv2.countNonZero(img) == 0:
            print 'end'
            break

if not True:
    img = cv2.resize(img, (0, 0), fx=3, fy=3)
    skel = cv2.resize(skel, (0, 0), fx=3, fy=3)
    cv2.imshow('original', original)
    cv2.imshow('test', skel)
    cv2.waitKey(0)

    plt.imshow(img), plt.show()


if True:
    orb = cv2.ORB(edgeThreshold=10) 
    kp, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(c2, None)
    imgkp = cv2.drawKeypoints(img, kp, color=(255, 0, 0), flags=0)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    #img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)

    drawMatches(img, kp, c2, kp2, matches[:3])



