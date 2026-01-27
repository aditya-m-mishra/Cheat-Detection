import cv2
import time
from utils import detect_faces, classify_behavior, draw_alert

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Webcam not accessible")
        return

    start_time = time.time()
    cheating_score = 0

    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = detect_faces(frame)
        behavior = classify_behavior(frame, faces)

        if behavior not in ["Normal", "Stabilizing..."]:
            cheating_score += 1


        draw_alert(frame, faces, behavior, cheating_score)

        cv2.imshow("AI Exam Cheating Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()