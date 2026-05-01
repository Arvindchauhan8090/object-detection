import cv2
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Define region (x1, y1, x2, y2)
ROI = (100, 100, 500, 400)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    x1, y1, x2, y2 = ROI

    # Draw ROI box
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # Run detection
    results = model(frame)

    person_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            # Get bounding box
            xA, yA, xB, yB = map(int, box.xyxy[0])

            # Compute center of box
            cx = (xA + xB) // 2
            cy = (yA + yB) // 2

            # Check if inside ROI
            if x1 < cx < x2 and y1 < cy < y2:

                # PERSON DETECTION
                if label == "person":
                    person_count += 1
                    color = (0, 255, 0)

                # OTHER OBJECTS (example: phone, bag)
                elif label in ["cell phone", "backpack"]:
                    color = (0, 0, 255)  # suspicious

                else:
                    color = (255, 255, 0)

                # Draw bounding box
                cv2.rectangle(frame, (xA, yA), (xB, yB), color, 2)
                cv2.putText(frame, label, (xA, yA - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Show count
    cv2.putText(frame, f"Persons in Box: {person_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    # Assessment logic
    if person_count > 1:
        cv2.putText(frame, "ALERT: Multiple Persons!",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 0, 255), 2)

    cv2.imshow("Assessment System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()