import cv2
from logger import Logger

logger = Logger(log_level="INFO", log_file="app.log")
class Streamer:
    def __init__(self,video_source=0,logger=None):
        self.video_source = video_source
        self.cap = cv2.VideoCapture(video_source)
        self.logger = Logger().log_info("Log dosyası başlatıldı.")

        if self.cap.isOpened():
            if self.logger:
                self.logger.log_info("Kamera başarıyla başlatıldı.")
        else:
            if self.logger:
                self.logger.log_error("Kamera başlatılamadı.")

    def get_frame(self):
        ret,frame = self.cap.read()
        frame = cv2.flip(frame, 1)


        if ret:
            return frame
        else:
            return None






