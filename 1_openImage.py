import cv2

def resize(img, scale_percent):
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	print('Resized Dimensions : ',resized.shape)
	return resized
 

img = cv2.imread('color.jpg')
cv2.imshow('Original Image',img)
img = resize(img,60)
cv2.imshow('Scaled down by 60%',img)
img = resize(img,20)
cv2.imshow('Scaled down 20%',img)
cv2.waitKey(0)
cv2.destroyAllWindows()