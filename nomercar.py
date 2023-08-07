import cv2
import imutils
import easyocr
import numpy
from matplotlib import pyplot

images = cv2.imread(r"C:\filiki\code 2\firsr_67\images\unknown.png")

gray_color = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

filter = cv2.bilateralFilter(gray_color, 11, 15, 15)
ygl = cv2.Canny(filter, 150, 150)
pyplot.imshow(ygl)
pyplot.show()
cont = cv2.findContours(ygl.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key = cv2.contourArea, reverse=True)

position = None

for i in cont:
    pribliz = cv2.approxPolyDP(i, 5, True)
    if len(pribliz) == 4:
        position = pribliz
        break
print(position)

mask = numpy.zeros(gray_color.shape, numpy.uint8)

new_img = cv2.drawContours(mask, [position], 0, 255, -1)

mask_images = cv2.bitwise_and(images, images, mask=mask)



pyplot.imshow(cv2.cvtColor(mask_images, cv2.COLOR_BGR2RGB))
pyplot.show()
