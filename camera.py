from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Camera(object):

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)
        self.rawCapture = PiRGBArray(self.camera, size=(1280, 720))
        time.sleep(0.1)

    def capture(self):
        # grab an image from the camera
        self.camera.capture(self.rawCapture, format="bgr")
        img = self.rawCapture.array
<<<<<<< HEAD
        img = cv2.flip(img, 0)
        img = cv2.flip(img, 1)
        self.rawCapture.truncate(0)
=======
	img = cv2.flip(img, 0)
	img = cv2.flip(img, 1)
	self.rawCapture.truncate(0)
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da

	return img

    def save(self, filename):
        image = self.capture()
        cv2.imwrite(filename, image)

def main():
    cam = Camera()
    cam.save('/home/pi/test.png')

if __name__ == '__main__':
    main()
