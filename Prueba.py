import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

img_color = cv2.imread('Fotos/albin.jpg')
#img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
#thresh_img = cv2.threshold(img_gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,2))
#opening_image = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, kernel,iterations=1)
#invert_image = 255 - opening_image

img = cv2.resize(img_color, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

roi = cv2.selectROI(img)
roi_cropped = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
cv2.destroyAllWindows()
text = pytesseract.image_to_string(roi_cropped, lang='spa', config='--psm 6')

print(text)
text2 = list(text)

if text2[16] in "O":
    text2[16] = "0"
if text2[16] in "I":
    text2[16] = "1"
if text2[16] in "T":
    text2[16] = "7"
if len(text2) >=18:
    text2.pop()

text = ""

for i in text2:
    text = text+i

print(text)
