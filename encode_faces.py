import os
import pickle
import face_recognition
from utils import get_image_paths


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWN_FACES_DIR = os.path.join(BASE_DIR, "data", "known_faces")
ENCODINGS_DIR = os.path.join(BASE_DIR, "encodings")
ENCODINGS_PATH = os.path.join(ENCODINGS_DIR, "face_encodings.pkl")

known_encodings = []
known_names = []

print("[INFO] Encoding faces...")

image_paths = get_image_paths(KNOWN_FACES_DIR)

for image_path in image_paths:
    name = os.path.basename(os.path.dirname(image_path))

    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        print(f"[WARNING] No face found in {image_path}")
        continue

    known_encodings.append(encodings[0])
    known_names.append(name)

print(f"[INFO] Encoded {len(known_encodings)} faces.")

data = {
    "encodings": known_encodings,
    "names": known_names
}

os.makedirs(ENCODINGS_DIR, exist_ok=True)

with open(ENCODINGS_PATH, "wb") as f:
    pickle.dump(data, f)

print(f"[INFO] Encodings saved to: {ENCODINGS_PATH}")
print("[INFO] Encoding complete.")
