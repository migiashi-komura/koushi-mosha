import cv2
import numpy as np

# read the image
image_path = input("enter the image path: ")
image = cv2.imread(image_path)

height = image.shape[0]
width = image.shape[1]

# creat a white paper with lines
paper = np.zeros((height, width, 3), np.uint8)
paper.fill(255)

# how may lines 
lines = int(input("how may lines for each: "))

# line thickness
thickness = 2

for i in range(lines):
    # only integer is accepted
    pt1x = int(width / (lines + 1)) * (i + 1)
    pt1y = 0
    pt2x = pt1x
    pt2y = height
    cv2.line(image, (pt1x, pt1y), (pt2x, pt2y), (0, 0, 0), thickness)
    cv2.line(paper, (pt1x, pt1y), (pt2x, pt2y), (0, 0, 0), thickness)

    pt1x = 0
    pt1y = int(height/ (lines + 1)) * (i + 1)
    pt2x = width
    pt2y = pt1y
    cv2.line(image, (pt1x, pt1y), (pt2x, pt2y), (0, 0, 0), thickness)
    cv2.line(paper, (pt1x, pt1y), (pt2x, pt2y), (0, 0, 0), thickness)

# make a new image
export_img = cv2.hconcat([paper, image])
cv2.line(export_img, (width, 0), (width, height), (0, 0, 0), thickness)
cv2.imwrite("./export.jpg", export_img)