import cv2

image = cv2.imread('rjannat.jpg')
width = int(image.shape[1] * 50 / 100)
height = int(image.shape[1] * 50 / 100)



resized_image = cv2.resize(image,(width,height))
cv2.imwrite('resized_image.jpg', resized_image)
