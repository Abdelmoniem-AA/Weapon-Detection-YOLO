import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train-20/weights/best.pt")

cap = cv2.VideoCapture("5243159-hd_1920_1080_25fps.mp4")

out = cv2.VideoWriter("output7.mp4", cv2.VideoWriter_fourcc(*"mp4v"), cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))


while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    results = model(frame, conf=0.2)

    annotated_frame = results[0].plot()

    out.write(annotated_frame)

    cv2.imshow("Weapon Detector", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# import cv2
# from ultralytics import YOLO

# model = YOLO("runs/detect/train-20/weights/best.pt")

# image = cv2.imread("MkII_07.jpg")

# results = model(image, conf=0.5)

# annotated_frame = results[0].plot()


# cv2.imshow("Weapon Detector", annotated_frame)

# cv2.imwrite("output4.jpg", annotated_frame)

# cv2.waitKey(0)
# cv2.destroyAllWindows()