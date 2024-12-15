import cv2
import numpy as np


class ImageProcessor:
    def __init__(self, config):
        # Renk aralıklarını alıyoruz
        self.red_min = np.array(config["colors"]["red_min"])
        self.red_max = np.array(config["colors"]["red_max"])
        self.green_min = np.array(config["colors"]["green_min"])
        self.green_max = np.array(config["colors"]["green_max"])
        self.yellow_min = np.array(config["colors"]["yellow_min"])
        self.yellow_max = np.array(config["colors"]["yellow_max"])

    def detect_color(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Renk maskelerini oluşturuyoruz
        red_mask = cv2.inRange(hsv, self.red_min, self.red_max)
        green_mask = cv2.inRange(hsv, self.green_min, self.green_max)
        yellow_mask = cv2.inRange(hsv, self.yellow_min, self.yellow_max)

        return red_mask, green_mask, yellow_mask

    def draw_contours(self, frame, red_mask, green_mask, yellow_mask):
        # Maskelere göre konturları buluyoruz
        contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_green, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Renkler için etiketler
        color_labels = {
            "red": (0, 0, 255),
            "green": (0, 255, 0),
            "yellow": (0, 255, 255)
        }

        # Renklerin çemberini çizme
        for contour in contours_red:
            self._draw_circle_and_label(frame, contour, color_labels["red"], "Red")

        for contour in contours_green:
            self._draw_circle_and_label(frame, contour, color_labels["green"], "Green")

        for contour in contours_yellow:
            self._draw_circle_and_label(frame, contour, color_labels["yellow"], "Yellow")

        return frame

    def _draw_circle_and_label(self, frame, contour, color, label):
        # Konturun merkezini buluyoruz
        if cv2.contourArea(contour) > 100:  # Küçük alanları göz ardı et
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Çember çizme
            cv2.circle(frame, center, radius, color, 2)
            # Etiket yazma
            cv2.putText(frame, label, (center[0] - 20, center[1] - radius - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
