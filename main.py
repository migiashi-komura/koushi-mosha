import cv2

image = cv2.imread("./image.jpg")

height = image.shape[0]
width = image.shape[1]

# only integer is accepted
pt1x = int(width/2)
pt1y = 0
pt2x = pt1x
pt2y = height
cv2.line(image, (pt1x, pt1y), (pt2x, pt2y), (0, 0, 0), 4)

pt1x = 0
pt1y = int(height/2)
pt2x = width
pt2y = pt1y
cv2.line(image, (pt1x, pt1y), (pt2x, pt2y), (0, 0, 0), 4)

cv2.imwrite("./export.jpg", image)