import cv2 as cv

img = cv.imread("C:\Code From VScode\Python\OpenCV\Photos\dogs.jpg")

roi = cv.selectROI(img)

print(roi)

img_cropped = img[int(roi[1]):int(roi[1]+roi[3]),
			int(roi[0]):int(roi[0]+roi[2])]

cv.imshow("Cropped Image", img_cropped)
cv.waitKey(0)