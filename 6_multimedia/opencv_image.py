import cv2

img=cv2.imread('IU.jpg')

cv2.resize(img, (800,600))

cv2.imshow('IU',img)


edge = cv2.Canny(img, 50,100)
edge1 = cv2.Canny(img, 200,250)
edge2 = cv2.Canny(img, 100,150)

cv2.imshow('IU',img)
cv2.imshow('edge',edge)
cv2.imshow('edge',edge1)
cv2.imshow('edge',edge2)
cv2.waitKey(0)
cv2.destroyAllWindows()