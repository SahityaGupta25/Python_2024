# import numpy as np
# import cv2

# cap = cv2.VideoCapture('one.mp4')

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('output',frame)
#     if (cv2.waitKey(1)&0xFF ==ord('q')):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import numpy as np
# import cv2

# cap = cv2.VideoCapture('two.mp4')


# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow('VIDEO',frame)
#     if (cv2.waitKey(1)&0xFF ==ord('q')):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import numpy as np
# import cv2
# import pyaudio as WithPyAudio
# import time

# def main(video_file, audio_file):
#     print(f"{video_file=},{audio_file=},{WithPyAudio=}")
#     cap = cv2.VideoCapture('one.mp4')

#     player = WithPyAudio(audio_file)
#     start_time = time.time()

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         cv2.imshow(video_file, frame)

#         elapsed = (time.time() - start_time) * 1000  # msec
#         play_time = int(cap.get(cv2.CAP_PROP_POS_MSEC))
#         sleep = max(1, int(play_time - elapsed))
#         if cv2.waitKey(sleep) & 0xFF == ord("q"):
#             break

#     player.close()
#     cap.release()
#     cv2.destroyAllWindows()


# importing libraries 




# import cv2 
# import numpy as np 

# # Create a VideoCapture object and read from input file 
# cap = cv2.VideoCapture('one.mp4') 

# # Check if camera opened successfully 
# if (cap.isOpened()== False): 
# 	print("Error opening video file") 

# # Read until video is completed 
# while(cap.isOpened()): 
	
# # Capture frame-by-frame 
# 	ret, frame = cap.read() 
# 	if ret == True: 
# 	# Display the resulting frame 
# 		cv2.imshow('Frame', frame) 
		
# 	# Press Q on keyboard to exit 
# 		if cv2.waitKey(6) & 0xFF == ord('q'): 
# 			break

# # Break the loop 
# 	else: 
# 		break

# # When everything done, release 
# # the video capture object 
# cap.release() 

# # Closes all the frames 
# cv2.destroyAllWindows() 


import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
video_path="../L1/images/Godwin.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)