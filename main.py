import cv2
from src.camera import VideoStream
from src.detector import PPEDetector
from src.database import DatabaseManager

def main():
    # Initialize Modules
    print("Initializing System...")
    cam = VideoStream(source="data/sample.mp4") # Change to 0 for webcam
    detector = PPEDetector()
    db = DatabaseManager()
    
    print("System Running. Press 'q' to exit.")

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        # 1. Detect Objects
        detections = detector.detect(frame)

        # 2. Process & Draw
        violation_count = 0
        for d in detections:
            x1, y1, x2, y2 = d['bbox']
            
            # Simulation Logic: 
            # In this demo, we treat every detected person as a "Violation" 
            # just to show the database working. 
            # REAL LOGIC: If Person AND NOT Hardhat -> Violation.
            
            violation_count += 1
            
            # Draw Red Box (Simulating Danger/Violation)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"Warning: {d['conf']:.2f}", (x1, y1-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # 3. Log to Database (Throttling could be added here)
            # db.log_violation("PPE Missing", d['conf']) 

        # 4. Dashboard UI (HUD)
        cv2.rectangle(frame, (0, 0), (1020, 40), (0, 0, 0), -1)
        cv2.putText(frame, f"Status: Monitoring | Violations Detected: {violation_count}", 
                    (20, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("SafeSite AI Monitor", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    db.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()