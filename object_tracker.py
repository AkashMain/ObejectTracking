import cv2 as cv

tracker = cv.TrackerKCF_create()
#cap = cv.VideoCapture('C:\Code From VScode\Python\OpenCV\Videos\mov_obj.mp4')
cap = cv.VideoCapture(0)

while True:
    k,frame = cap.read()
    cv.imshow('Tracking',frame)
    k = cv.waitKey(20) & 0xff
    if k == 27:
        break

bbox = cv.selectROI(frame,False)
print(bbox)

op = tracker.init(frame,bbox)  # Initialising Tracker
cv.destroyWindow("ROI selector")

while True:
    op,frame=cap.read()
    op,bbox=tracker.update(frame)

    if op:
        p1=(int(bbox[0]),int(bbox[1]))
        p2=(int(bbox[0])+int(bbox[2]),int(bbox[1])+int(bbox[3]))

        cv.rectangle(frame,p1,p2,(0,255,0),2)

    cv.imshow('Tracking',frame)
    k=cv.waitKey(1) & 0xff
    if k==27:
        break
