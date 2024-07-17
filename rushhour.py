import cv2 as cv
import numpy as np

def preprocess_image(image_path):
    image = cv.imread(image_path)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    _, binary = cv.threshold(gray, 128, 255, cv.THRESH_BINARY_INV)

    return image, binary

path = "rushhour_board.jpg"
img = cv.imread(path)
img_small = cv.resize(img, (400, 800))
gray = cv.cvtColor(img_small, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 128, 255, cv.THRESH_BINARY_INV)
cv.imshow("Window Display", binary)

k = cv.waitKey(0)

