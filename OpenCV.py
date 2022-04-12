import cv2
filePath = 'Album.jpg'
image = cv2.imread(filePath, 1)
cv2.imshow('Kobi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
