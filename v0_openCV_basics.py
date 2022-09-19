# importing libraries
from re import M
from sys import builtin_module_names
import cv2 as cv

# Read an image with cv.imread()
my_cat = cv.imread('images/cat.jpg')

# # Display image as a new window with cv.imshow(). 
# # It requires the name of the window and the image (matrix of pixels)
# cv.imshow('Cat', my_cat)

# # cv.waitKey() is a Keyboard binding function that waits for a specific delay in milliseconds for a key to be pressed
# cv.waitKey(0)

# #-------------

# # Reading videos
# # cv.VideoCapture takes an integer argument (0, 1, 2...) or a path to a video file
# # If you use an integer, you can access a camera connected to your computer
# capture = cv.VideoCapture(0)

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# #--------------

# race_car = cv.VideoCapture('videos/race_car.mp4')

# while True:
#     isTrue, frame = race_car.read()
#     cv.imshow('Race Car', frame)
#     # Break out the loop and stop displaying the video if the letter D is pressed. 
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# race_car.release()
# cv.destroyAllWindows()
# # Once the video stops, you've got an error (-215 assertion failed). OpenCV couldn't find a media file at that particular location. The video ran out of frames. You got the same error if you specify a wrong path for an image.  

# Rescaling and resizing images and video frames

# Rescaling implies modifying hight and width. It is best practice to downscale (smaller than original). 

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

my_cat = rescaleFrame(my_cat, 0.4)

# cat_resized = rescaleFrame(my_cat, 0.5)
# cv.imshow('My Cat', my_cat)
# cv.imshow('My Cat Resized', cat_resized)
# cv.waitKey(0)


# race_car = cv.VideoCapture('videos/race_car.mp4')

# while True:
#     isTrue, frame = race_car.read()
#     frame_resized = rescaleFrame(frame, 0.3)
#     cv.imshow('Race Car', frame)
#     cv.imshow('Race Car Resized', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# race_car.release()
# cv.destroyAllWindows()

#----------------

# Draw

import numpy as np

# blank = np.zeros((500, 500, 3), dtype='uint8' )
# cv.imshow('Blank', blank)

# # Paint the image a certain color
# cv.waitKey(500)
# blank[:] = 255,0,0
# cv.imshow('Blue', blank)
# cv.waitKey(500) 
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red Square', blank)
# cv.waitKey(500)

# # Draw a rectangle
# cv.rectangle(blank, (100, 100), (300, 200), (0, 255, 255), thickness=2)
# cv.imshow('Rectangle', blank)
# cv.waitKey(500)

# cv.rectangle(blank, (400, 100), (500, 200), (255, 255, 255), thickness=cv.FILLED)
# cv.imshow('Another Rectangle', blank)
# cv.waitKey(500)

# # Draw a circle
# cv.circle(blank, (100, 400), 50, (120, 280, 30), thickness=-1)
# cv.imshow('Circle', blank)
# cv.waitKey(500)

# # Draw a Line
# cv.line(blank, (0,0), (300, 100), (100, 150, 0), thickness=5)
# cv.imshow('Line', blank)
# cv.waitKey(500)

# # Write Text
# cv.putText(blank, 'Learning...', (300, 400), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255),  2)
# cv.imshow('Text', blank)
# cv.waitKey(0)


# Basic Functions

# Converting to Grayscale

my_cat_gray = cv.cvtColor(my_cat, cv.COLOR_BGR2GRAY)
cv.imshow('Cat', my_cat)
cv.imshow('Cat Gray', my_cat_gray)

# Blur
# To remove some of the noise that exists in an image. There's a lot of blurring techniques. 
my_cat_blur = cv.GaussianBlur(my_cat, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Cat Blur', my_cat_blur)
my_cat_blur_2 = cv.GaussianBlur(my_cat, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Cat Blur 2', my_cat_blur_2)

# Edge Cascade

my_cat_canny = cv.Canny(my_cat, 125, 175)
cv.imshow('My Cat Canny', my_cat_canny)

my_cat_canny_blur= cv.Canny(my_cat_blur, 125, 175)
cv.imshow('My Cat Canny Blur', my_cat_canny_blur)


# Dilating the image
my_cat_dilated = cv.dilate(my_cat_canny_blur, (7, 7), iterations=3)
cv.imshow('My Cat Dilated', my_cat_dilated)

# Eroding the image
my_cat_eroded= cv.erode(my_cat_canny_blur, (3, 3), iterations=1)
cv.imshow('My Cat Eroded', my_cat_eroded)

# Cropping
my_cat_cropped = my_cat[80:260, 90:300]
cv.imshow('My Cat Cropped', my_cat_cropped)

cv.waitKey(0)