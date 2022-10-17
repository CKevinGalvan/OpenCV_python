import cv2 as cv
img = cv.imread('cuteDog1.jpg')

def changeRes(width, height):
	#This will work for live video
	capture.set(3,width)
	capture.set(4,width)
    
def rescaleFrame(frame, scale=0.75):
	#This will work for Images, videos, live video
    width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA )

resized_image = rescaleFrame(img, scale=0.2)
cv.imshow('Dog1', img)
cv.imshow('Dog', resized_image)


    # Reading video 
capture = cv.VideoCapture('Baby Dogs.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    # Displaying each frame 
    cv.imshow('Baby Dogs',frame)
    cv.imshow('Video Resized', frame_resized)

    # In order to stop
    if cv.waitKey(20) & 0xFF==ord('d'):# It tells that if the letter d is pressed
        # the loop will be break
        break
# Release all the files 
capture.release()
#Destroy all the windows after the video is done. 
cv.destroyAllWindows()


