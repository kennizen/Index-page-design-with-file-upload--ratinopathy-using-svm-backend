import pickle

import sys
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

with open('E:/model_pickle', 'rb') as f:
    pr = pickle.load(f)

# test model No DR


def hist_equalization(image_bw):
    red, green, blue = cv2.split(image_bw)
    hist_red = cv2.equalizeHist(red)
    hist_green = cv2.equalizeHist(green)
    hist_blue = cv2.equalizeHist(blue)

    img_eq = cv2.merge((hist_red, hist_green, hist_blue))
    return img_eq


dec = {'0': 'No DR', '1': 'DR'}

img = cv2.imread(sys.argv[1], 0)
img = cv2.resize(img, (200, 200))
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_b = cv2.addWeighted(image_rgb, 4, cv2.GaussianBlur(
    image_rgb, (0, 0), sigmaX=20), -4, 128)
img_eq = hist_equalization(img_b)
img1 = img_eq.reshape(1, -1)/255
p = pr.predict(img1)
p = plt.title(dec[p[0]])
print(p)
