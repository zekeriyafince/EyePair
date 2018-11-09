import numpy as np
import cv2
from EyePair import *

def main():
	capture = cv2.VideoCapture(0)
	

	while True:
		ret, image = capture.read()
		picture = ReturnEyePairFunc(image) 
		cv2.imshow("picture",picture)
		if(np.sum(picture == 0)): # not return (default black picture)
			print("Not Eye-Pair")
					
		k = cv2.waitKey(30) & 0xff
		
		if k == 27: #ESC
			break
			
	capture.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()

