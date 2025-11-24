from ultralytics import YOLO
import cv2

class PPEDetector:
    def __init__(self, model_path='yolov8n.pt'):
        # Load YOLO model (Downloads automatically on first run)
        self.model = YOLO(model_path)
        # Standard COCO class for 'person' is index 0
        self.target_class_id = 0 

    def detect(self, frame):
        # Inference
        results = self.model(frame, stream=True)
        
        detections = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Extract coordinates and class
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                # Logic: If we see a person (Class 0)
                # In a real PPE project, you would check for 'Hardhat' class here
                if cls == self.target_class_id and conf > 0.5:
                    detections.append({
                        'bbox': (x1, y1, x2, y2),
                        'conf': conf,
                        'class': 'Person' # Change to 'No Hardhat' for custom model
                    })
        return detections