import cv2

image = cv2.imread("batman-beyond-high-flying-patrol-pj-1920x1080.jpg")

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imwrite("batman-beyond-high-flying-patrol-pj-1920x1080.jpg", blurred_image)

cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
