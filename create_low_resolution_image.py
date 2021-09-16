import cv2
img = cv2.imread("data/test2_HR_ORIGINAL.bmp")
img = cv2.resize(img, (img.shape[1] // 3 * 3, img.shape[0] // 3 * 3))
# img = cv2.resize(img, (639, 639))
cv2.imwrite("data/test2_HR.bmp", img)