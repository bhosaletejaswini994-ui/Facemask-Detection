
# import cv2
# import numpy as np
# import tensorflow as tf

# model = tf.keras.models.load_model("model/mask_detector.keras")

# camera = cv2.VideoCapture(0)

# while True:
#     ret, frame = camera.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = cv2.CascadeClassifier(
#         cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
#     ).detectMultiScale(gray, 1.1, 5)

#     for (x, y, w, h) in faces:
#         face = cv2.resize(frame[y:y+h, x:x+w], (224, 224))
#         face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
#         face = np.expand_dims(face, axis=0)

#         prediction = model.predict(face, verbose=0)[0]
#         label = "WITH MASK" if np.argmax(prediction) == 0 else "WITHOUT MASK"

#         color = (0, 255, 0) if label == "WITH MASK" else (0, 0, 255)

#         cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
#         cv2.putText(frame, label, (x, y-10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

#     cv2.imshow("Face Mask Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# camera.release()
# cv2.destroyAllWindows()



# import cv2

# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )

# camera = cv2.VideoCapture(0)

# while True:
#     ret, frame = camera.read()

#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 5)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.putText(frame, "FACE DETECTED", (x, y-10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

#     cv2.imshow("Face Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# camera.release()
# cv2.destroyAllWindows()


# import cv2
# import os
# import time
# from datetime import datetime
# from ultralytics import YOLO
# from huggingface_hub import hf_hub_download

# # Create folders on Desktop
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# main_folder = os.path.join(desktop, "Face Mask Photos")

# with_mask = os.path.join(main_folder, "With Mask")
# without_mask = os.path.join(main_folder, "Without Mask")

# os.makedirs(with_mask, exist_ok=True)
# os.makedirs(without_mask, exist_ok=True)

# # Download and load mask detection model automatically
# print("Loading mask detection model...")

# model_path = hf_hub_download(
#     repo_id="krishnamishra8848/Face_Mask_Detection",
#     filename="best.pt"
# )

# model = YOLO(model_path)
# print("Model classes:", model.names)

# # Open webcam
# camera = cv2.VideoCapture(0)

# if not camera.isOpened():
#     print("Camera not found!")
#     raise SystemExit

# last_capture = {"with": 0, "without": 0}
# cooldown = 5

# print("Face Mask Detection Started. Press Q to exit.")

# try:
#     while True:
#         success, frame = camera.read()

#         if not success:
#             break

#         results = model(frame, conf=0.5, verbose=False)

#         for result in results:
#             for box in result.boxes:

#                 class_id = int(box.cls[0])
#                 label = str(model.names[class_id]).lower()

#                 x1, y1, x2, y2 = map(int, box.xyxy[0])

#                 if "without" in label or "no_mask" in label or "incorrect" in label:
#                     folder = without_mask
#                     key = "without"
#                     text = "WITHOUT MASK"
#                     color = (0, 0, 255)

#                 elif "with" in label or "mask" in label:
#                     folder = with_mask
#                     key = "with"
#                     text = "WITH MASK"
#                     color = (0, 255, 0)

#                 else:
#                     continue

#                 cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
#                 cv2.putText(frame, text, (x1, max(y1 - 10, 20)),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

#                 # Save photo every five seconds per category
#                 current_time = time.time()

#                 if current_time - last_capture[key] >= cooldown:
#                     photo = frame[y1:y2, x1:x2]

#                     if photo.size > 0:
#                         filename = datetime.now().strftime(
#                             "person_%Y%m%d_%H%M%S_%f.jpg"
#                         )

#                         cv2.imwrite(os.path.join(folder, filename), photo)
#                         last_capture[key] = current_time
#                         print("Photo saved:", filename)

#         cv2.imshow("Face Mask Detection", frame)

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

# finally:
#     camera.release()
#     cv2.destroyAllWindows()
#     print("Camera stopped.")





import cv2
import os
import time
from datetime import datetime
from ultralytics import YOLO
from huggingface_hub import hf_hub_download

# --------------------------------
# CREATE DESKTOP FOLDERS
# --------------------------------

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

main_folder = os.path.join(desktop, "Face Mask Photos")

with_mask = os.path.join(main_folder, "With Mask")
without_mask = os.path.join(main_folder, "Without Mask")

os.makedirs(with_mask, exist_ok=True)
os.makedirs(without_mask, exist_ok=True)


# --------------------------------
# LOAD AI MODEL
# --------------------------------

print("Loading AI model...")

model_path = hf_hub_download(
    repo_id="krishnamishra8848/Face_Mask_Detection",
    filename="best.pt"
)

model = YOLO(model_path)

print("Model classes:", model.names)


# --------------------------------
# OPEN WEBCAM
# --------------------------------

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Camera not found!")
    raise SystemExit

# Set camera resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
camera.set(cv2.CAP_PROP_FPS, 30)

# Enable autofocus if supported
camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)

print("Actual camera width:", camera.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Actual camera height:", camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


# --------------------------------
# CAPTURE SETTINGS
# --------------------------------

last_capture = 0
cooldown = 5

print("Camera started. Press Q to exit.")


# --------------------------------
# MAIN CAMERA LOOP
# --------------------------------

try:

    while True:

        success, frame = camera.read()

        if not success:
            print("Unable to read camera frame.")
            break

        # Run mask detection
        results = model(frame, conf=0.5, verbose=False)

        detected_people = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                label = str(
                    model.names[class_id]
                ).lower().replace(" ", "_")

                x1, y1, x2, y2 = map(
                    int, box.xyxy[0]
                )

                # Identify mask category
                if (
                    "without" in label
                    or "no_mask" in label
                    or "incorrect" in label
                ):

                    folder = without_mask
                    text = "WITHOUT MASK"
                    color = (0, 0, 255)

                elif "with" in label or label == "mask":

                    folder = with_mask
                    text = "WITH MASK"
                    color = (0, 255, 0)

                else:
                    continue

                # Display detection rectangle
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    color,
                    2
                )

                cv2.putText(
                    frame,
                    text,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2
                )

                detected_people.append(
                    (x1, y1, x2, y2, folder, text)
                )

        # --------------------------------
        # SAVE PHOTOS EVERY 5 SECONDS
        # --------------------------------

        current_time = time.time()

        if (
            detected_people
            and current_time - last_capture >= cooldown
        ):

            capture_time = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            height, width = frame.shape[:2]

            padding = 100

            for number, person in enumerate(
                detected_people, start=1
            ):

                x1, y1, x2, y2, folder, text = person

                # Add extra area around detection
                x1_new = max(0, x1 - padding)
                y1_new = max(0, y1 - padding)

                x2_new = min(width, x2 + padding)
                y2_new = min(height, y2 + padding)

                # Crop original camera image
                photo = frame[
                    y1_new:y2_new,
                    x1_new:x2_new
                ]

                if photo.size > 0:

                    filename = (
                        f"{text}_{capture_time}_{number}.jpg"
                    )

                    filepath = os.path.join(
                        folder,
                        filename
                    )

                    # Save at maximum JPEG quality
                    saved = cv2.imwrite(
                        filepath,
                        photo,
                        [cv2.IMWRITE_JPEG_QUALITY, 100]
                    )

                    if saved:
                        print("Saved:", filepath)

            last_capture = current_time

        # Display webcam
        cv2.imshow(
            "Face Mask Detection",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


# --------------------------------
# CLOSE CAMERA
# --------------------------------

finally:

    camera.release()

    cv2.destroyAllWindows()

    print("Camera stopped.")
