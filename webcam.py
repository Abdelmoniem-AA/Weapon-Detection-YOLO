import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train-20/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    results = model(frame, conf=0.5)

    annotated_frame = results[0].plot()

    cv2.imshow("Weapon Detector", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()