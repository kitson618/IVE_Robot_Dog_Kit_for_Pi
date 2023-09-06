from picamera2 import Picamera2
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)
#picam2.start_and_capture_file("image.jpg")
picam2.start()
picam2.capture_file("image.jpg")
