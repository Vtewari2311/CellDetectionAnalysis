import cv2
import numpy as np
from matplotlib import pyplot as plt
path = r'C:\Users\silvalab\Desktop\Unmarked\Unmarked\Undiluted 15,000 um 3 crop.jpg'
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, 
cv2.THRESH_BINARY
plt.imshow(gray, cmap='gray')
blur = cv2.GaussianBlur(gray, (11, 11), 0)
plt.imshow(blur, cmap='gray')
canny = cv2.Canny(blur, 30, 40, 3)
plt.imshow(canny, cmap='gray')
dilated = cv2.dilate(canny, (1, 1), iterations=0) 
plt.imshow(dilated, cmap='gray')
(cnt, hierarchy) = cv2.findContours(
dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
plt.imshow(rgb)
print("No of cells: ", len(cnt))
