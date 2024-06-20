import cv2
import base64
from channels.generic.websocket import WebsocketConsumer
from threading import Thread

class WebcamConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.cap = cv2.VideoCapture(0)  # Ensure the correct camera index

        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            self.close()
            return

        self.thread = Thread(target=self.send_frame)
        self.thread.start()

    def disconnect(self, close_code):
        self.cap.release()

    def send_frame(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            self.send(text_data=jpg_as_text)

    def receive(self, text_data):
        pass

