import cv2 as cv
import os
import time

# Capture image every 5 seconds
def capture_image(vc):
    directory = "images"
    if not os.path.exists(directory):
        os.makedirs(directory)
    while True:
        rval, frame = vc.read()
        if rval:
            time_str = time.strftime("%Y%m%d-%H%M%S")
            fileName = os.path.join(directory,"image_" + time_str + ".jpg")
            cv.imwrite(fileName, frame)
        else:
            print("Failed to capture image")
            break
        time.sleep(5)