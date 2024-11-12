import cv2

image = cv2.imread("IMG_20240411_054811.jpg")

scale_percent = 110

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dimensions = (width, height)

resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
