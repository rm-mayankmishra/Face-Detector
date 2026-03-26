# pip install opencv-python
# haarcascade_frontalface_default.xml

import cv2
import time

# Load face cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start camera
cap = cv2.VideoCapture(0)

# FPS calculation variables
prev_time = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not working")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles + count
    face_count = 0
    for (x, y, w, h) in faces:
        face_count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Face count display
    cv2.putText(frame, f'Faces: {face_count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Timestamp
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, current_time, (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    cv2.putText(frame, f'FPS: {int(fps)}', (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show output
    cv2.imshow("Face Detection System", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()