import cv2

img=cv2.imread('IU.jpg')

gray = cv2.cvtColor(img, cv2. COLOR_BGR2GRAY)

cv2.imshow('IU',img)
cv2.imshow('IU_GRAY',gray)

#엔터키는 13 esc 27
while True:
    if cv2.waitKey(0) == 13:
        break

cv2.imwrite('IU_GRAY.jpg',gray)


cv2.destroyAllWindows()