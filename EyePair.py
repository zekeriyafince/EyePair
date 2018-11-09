import numpy as np
import cv2


## https://github.com/zekeriyafince/EyePair/blob/master/haar-cascade/haarcascades_haarcascade_mcs_eyepair_big.xml
face_cascade = cv2.CascadeClassifier('./haar-cascade/haarcascade_frontalface_default.xml') # face 

## https://github.com/zekeriyafince/EyePair/blob/master/haar-cascade/haarcascade_frontalface_default.xml
eyePair_cascade = cv2.CascadeClassifier('./haar-cascade/haarcascades_haarcascade_mcs_eyepair_big.xml') #eye_pair

defaultPicture = np.zeros((60,150,1)) # black picture

def ReturnEyePairFunc(frameImage):
	gray = cv2.cvtColor(frameImage, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for x, y, w, h in faces: # face points
		roiGray = gray[y:y + h, x:x + w]
		roiColor = frameImage[y:y + h, x:x + w]
		eyePairs = eyePair_cascade.detectMultiScale(roiGray)

		for (ex, ey, ew, eh) in eyePairs: # eye_pair points
			roiEyes = roiColor[ex:ex + ew + 30, ey-45: ey + eh - 15]
			return roiEyes
	return defaultPicture
