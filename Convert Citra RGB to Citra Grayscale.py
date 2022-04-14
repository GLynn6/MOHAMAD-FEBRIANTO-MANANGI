import cv2
import numpy as np

img = cv2.imread("febrianto.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar febrianto Original", img)
cv2.imshow("Gambar febrianto grayscale", gray)

cv2.waitKey(0)
cv2.destroyWindow()
