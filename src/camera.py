import cv2

class VideoStream:
    def __init__(self, source=0):
        # Logic: If source is a number (0, 1), use DirectShow for Webcam.
        # If source is a string ("data/video.mp4"), just read the file.
        if isinstance(source, int):
            self.cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
        else:
            self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise ValueError(f"Could not open video source: {source}")
            
    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Resize for better performance (Non-functional Req: Performance)
            return cv2.resize(frame, (1020, 600)) 
        return None

    def release(self):
        self.cap.release()