import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Global stability counters
face_frames = 0
no_face_frames = 0

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=6,      # higher = fewer false detections
        minSize=(120, 120)   # IGNORE small fake faces
    )
    return faces

def classify_behavior(frame, faces):
    global face_frames, no_face_frames
    h, w, _ = frame.shape

    # -------- NO FACE LOGIC (STABLE) --------
    if len(faces) == 0:
        no_face_frames += 1
        face_frames = 0

        if no_face_frames > 15:
            return "No Person Detected"
        else:
            return "Stabilizing..."

    # -------- FACE FOUND --------
    face_frames += 1
    no_face_frames = 0

    if face_frames < 10:
        return "Stabilizing..."

    # -------- MULTIPLE PEOPLE --------
    if len(faces) > 1:
        return "Multiple People Detected"

    (x, y, fw, fh) = faces[0]
    face_center_x = x + fw // 2

    if face_center_x < w * 0.35 or face_center_x > w * 0.65:
        return "Looking Away"

    return "Normal"
def draw_alert(frame, faces, behavior, score):
    # Draw face boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Status text color
    color = (0, 255, 0)
    if behavior not in ["Normal", "Stabilizing..."]:
        color = (0, 0, 255)

    cv2.putText(
        frame,
        f"Status: {behavior}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.putText(
        frame,
        f"Cheating Score: {score}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 0),
        2
    )