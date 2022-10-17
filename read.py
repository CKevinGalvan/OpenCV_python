import cv2 as cv

# img = cv.imread('cuteDog1.jpg')
# cv.imshow('cuteDog', img)
# cv.waitKey(0)
# 

# Reading video 
capture = cv.VideoCapture('Baby Dogs.mp4')
while True:
    isTrue, frame = capture.read()
    # Displaying each frame 
    cv.imshow('Baby Dogs',frame)

    # In order to stop
    if cv.waitKey(20) & 0xFF==ord('d'):# It tells that if the letter d is pressed
        # the loop will be break
        break
# Release all the files 
capture.release()
#Destroy all the windows after the video is done. 
cv.destroyAllWindows()

# Resize and rescale 
# img = cv.imread('cuteDog1.jpg')
# cv.imshow('cuteDog', img)
# def rescaleFrame(frame, scale=0.75):
# 	width = int(frame.shape[1]*scale) 
# 	height = int(frame.shape[0]*scale) 	
# 	dimensions = (width,height)
	
# 	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# cv.waitKey(0)


