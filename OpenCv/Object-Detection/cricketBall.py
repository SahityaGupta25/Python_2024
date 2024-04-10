import cv2
vidcap = cv2.VideoCapture('../Videos/one_cricket_ball.mp4')
true , image = vidcap.read()

count = 0
while vidcap.isOpened():
    true,image = vidcap.read()
    cv2.imwrite("C:\Users\vasug\OneDrive\Desktop\Python_2024\OpenCv\Object-Detection\Data Set (Videos)\Cricket_ball_one\%d.png" %count,image)
    count+=1