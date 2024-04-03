import cv2
import random
img = cv2.imread('./img/bmwBike.jpg',-1)

# print(img)
# print(img[66][66:166])
# print(img.shape[0])

# for i in range(255):
#     for j in range(img.shape[1]):
#         img [i] [j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

tag = img[400:600,700:800]
img[100:200,400:600]=tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()