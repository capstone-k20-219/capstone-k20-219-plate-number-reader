import cv2 as cv
import threading
import utilities as utils
import sys
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db

# Check camera type
cameraType = sys.argv[1]

# Load the Firebase credentials and initialize the Firebase app
load_dotenv()
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": os.getenv("FIREBASE_DB_URL"),
})

# Get the reference to the Firebase database node
ref = db.reference("/plateNumberIn") if cameraType == "checkin" else db.reference("/plateNumberOut")

# Open camera
cv.namedWindow("ANPR {} Camera".format(cameraType.capitalize()), cv.WINDOW_AUTOSIZE)
cv.setWindowProperty("ANPR {} Camera".format(cameraType.capitalize()), cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
vc = cv.VideoCapture(0)

# Check if the webcam is opened or not
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
    print("Failed to open camera")

# Start the thread to capture the image
capture_thread = threading.Thread(target=utils.capture_image, args=(vc,))
capture_thread.start()

# Loop to display the camera feed
while rval:
    cv.imshow("ANPR {} Camera".format(cameraType.capitalize()), frame)
    rval, frame = vc.read()
    key = cv.waitKey(20)
    if key == 27: # exit on ESC
        break

# Destroy the window and release the camera
vc.release()
cv.destroyWindow("ANPR {} Camera".format(cameraType.capitalize()))