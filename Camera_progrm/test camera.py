from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(fullscreen=False, window=(100,20,640,480))



##for i in range(5):
  #  sleep(2)
   # camera.capture('/home/pi/image%s.jpg' % i)
#camera.stop_preview()
