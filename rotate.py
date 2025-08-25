import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("vertical-shot-some-beautiful-trees-sun-setting-background.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 45, 1)
rotated = cv2.warpAffine(image_rgb, M, (w, h))
plt.imshow(rotated)
plt.title("Roated Image")
plt.show()