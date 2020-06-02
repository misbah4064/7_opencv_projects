import cv2 

def rotate(image):
	rows,cols = image.shape[:2] 
	M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) 
	dst = cv2.warpAffine(image,M,(cols,rows))
	return dst

image = cv2.imread('color.jpg') 
height = 476
width = image.shape[0]
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
print("Image Dimension:",image.shape[:2])

while (1):
	image = rotate(image)
	cv2.imshow("rotate",image)
	key = cv2.waitKey(300)
	if key==27 or 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break

