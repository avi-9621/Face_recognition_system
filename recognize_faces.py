import os
import face_recognition
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENCODINGS_PATH = os.path.join(BASE_DIR, "encodings", "face_encodings.pkl")

if not os.path.exists(ENCODINGS_PATH):
    raise FileNotFoundError(
        f"Encodings file not found at {ENCODINGS_PATH}. "
        "Run encode_faces.py first."
    )

print("[INFO] Loading encodings...")
with open(ENCODINGS_PATH, "rb") as f:
    data = pickle.load(f)

video = cv2.VideoCapture(0)
print("[INFO] Starting camera... Press 'q' to quit")

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for (box, encoding) in zip(locations, encodings):
        matches = face_recognition.compare_faces(
            data["encodings"], encoding, tolerance=0.5
        )
        name = "Unknown"

        if True in matches:
            matched_indexes = [i for i, match in enumerate(matches) if match]
            counts = {}

            for i in matched_indexes:
                person = data["names"][i]
                counts[person] = counts.get(person, 0) + 1

            name = max(counts, key=counts.get)

        top, right, bottom, left = box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(
            frame, name, (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
        )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

#https://youtu.be/QUvaHKRvfWA?si=y8t2_VkRKIc7thZs
