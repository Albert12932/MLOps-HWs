from ultralytics import YOLO
import cv2
import numpy as np

class ObjectDetector:
    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model = YOLO(model_path)

    def predict(self, image_bytes: bytes) -> bytes:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        results = self.model(img)
        
        annotated_frame = results[0].plot()
        
        _, encoded_img = cv2.imencode('.jpg', annotated_frame)
        return encoded_img.tobytes()


detector = ObjectDetector() 
