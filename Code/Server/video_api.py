import io
from picamera2 import Picamera2,Preview
from picamera2.encoders import JpegEncoder, H264Encoder
from picamera2.outputs import FileOutput
from picamera2.encoders import Quality
from threading import Condition

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

picam2 = Picamera2()
output = StreamingOutput()
picam2.start_and_record_video(FileOutput(output), JpegEncoder(), duration=10, quality=Quality.VERY_HIGH)
picam2.stop_recording()
