
from config import load_config
from streamer import Streamer
from image_process import ImageProcessor
from logger import Logger
import cv2

class ColorDetectionApp:
    def __init__(self):
        self.config = load_config()# Konfigürasyonu yükle
        self.logger = Logger(self.config['logging']['log_level'], self.config['logging']['log_file'])
        self.streamer = Streamer()  # Video akışını başladı.
        self.image_processor = ImageProcessor(self.config)  # Görüntü işleyicisini başlat


    def start(self):
        self.logger.log_info("Program çalışmaya başladı.")
        self.logger.log_info("Görüntü alınıyor.")
        self.logger.log_info("Configden renkler alındı.")

        while True:
            frame = self.streamer.get_frame()

            if frame is not None:
                # Renkleri algıla
                red_mask, green_mask, yellow_mask = self.image_processor.detect_color(frame)
                # Konturları çiz
                frame_with_contours = self.image_processor.draw_contours(frame, red_mask, green_mask, yellow_mask)

                # Görüntüye bak
                cv2.imshow("Color", frame_with_contours)

                # Çıkış için 'q' tuşuna basın
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.logger.log_info("Çıkış yapıldı")
                    break

        self.cleanup()

    def cleanup(self):
        self.streamer.cap.release()
        cv2.destroyAllWindows()
        self.logger.log_info("Program kapatildi.")

if __name__ == "__main__":
    app = ColorDetectionApp()
    app.start()
