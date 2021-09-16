import cv2
img = cv2.imread("data/test1_HR.bmp")
img = cv2.resize(img, (213, 213))
img = cv2.resize(img, (639, 639))
cv2.imwrite("data/test1_LR.bmp", img)