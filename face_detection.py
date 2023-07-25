import cv2
import numpy as np
# Load pre-trained face detection model from OpenCV
face_model = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel"
)

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change the argument to the video file path if using a video file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform face detection
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)
    )  # Preprocess the frame
    face_model.setInput(blob)
    detections = face_model.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Adjust the confidence threshold as needed
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Show the output frame
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
