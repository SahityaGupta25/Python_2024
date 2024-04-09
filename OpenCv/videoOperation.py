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


import numpy as np
import cv2
import pyaudio as WithPyAudio
import time

def main(video_file, audio_file):
    print(f"{video_file=},{audio_file=},{WithPyAudio=}")
    cap = cv2.VideoCapture('one.mp4')

    player = WithPyAudio(audio_file)
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(video_file, frame)

        elapsed = (time.time() - start_time) * 1000  # msec
        play_time = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        sleep = max(1, int(play_time - elapsed))
        if cv2.waitKey(sleep) & 0xFF == ord("q"):
            break

    player.close()
    cap.release()
    cv2.destroyAllWindows()