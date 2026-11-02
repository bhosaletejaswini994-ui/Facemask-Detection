# 😷 AI-Based Face Mask Detection System Using Python & YOLO

## 📌 Project Overview

The **AI-Based Face Mask Detection System** is a real-time computer vision application developed using Python, OpenCV, and YOLO (You Only Look Once).

This project uses a pre-trained YOLO deep learning model to detect whether a person is wearing a face mask or not through a webcam.

The system automatically identifies two categories:

- 🟢 **With Mask** – Detects people wearing face masks.
- 🔴 **Without Mask** – Detects people not wearing face masks.

It also automatically captures and saves detected people's photos into separate folders on the Desktop. Images are captured every 5 seconds to avoid saving too many duplicate photos.

## 🎯 Project Objectives

- Detect faces with and without masks using AI.
- Perform real-time detection through a webcam.
- Display detection labels with colored bounding boxes.
- Automatically capture detected images.
- Save images in separate folders.
- Maintain high JPEG image quality.
- Organize captured images for future analysis.

## 🛠️ Technologies & Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Webcam access and image processing |
| YOLO | AI-based object detection |
| Ultralytics | YOLO model integration |
| Hugging Face Hub | Downloading the pre-trained AI model |
| OS | Creating folders and managing files |
| Time | Managing automatic photo capture intervals |
| Datetime | Generating unique filenames |

## 🤖 AI Model Information

This project uses a pre-trained YOLO model downloaded from Hugging Face.

**Model Repository:** `krishnamishra8848/Face_Mask_Detection`

**Model File:** `best.pt`

The model is used to classify detected people into face mask categories.

## ⚙️ How the Project Works

1. The application creates folders automatically on the Desktop.
2. It downloads the pre-trained YOLO model from Hugging Face.
3. The webcam starts capturing live video.
4. YOLO analyzes each frame and detects face mask categories.
5. A green bounding box indicates a person wearing a mask.
6. A red bounding box indicates a person without a mask.
7. The system automatically captures photos every 5 seconds when detections are available.
8. The captured photos are saved in their respective folders.
9. Press `Q` to stop the camera.

## 📂 Project Folder Structure

The application automatically creates the following folder structure:

```text
Desktop/
│
└── Face Mask Photos/
    │
    ├── With Mask/
    │   ├── WITH MASK_20261102_104500_1.jpg
    │   ├── WITH MASK_20261102_104505_1.jpg
    │   └── ...
    │
    └── Without Mask/
        ├── WITHOUT MASK_20261102_104500_1.jpg
        ├── WITHOUT MASK_20261102_104505_1.jpg
        └── ...
```

## 📦 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Face-Mask-Detection.git
```

### Step 2: Open the Project Folder

```bash
cd Face-Mask-Detection
```

### Step 3: Install Required Libraries

```bash
pip install opencv-python ultralytics huggingface_hub
```

### Step 4: Run the Application

```bash
python FaceMaskDetection.py
```

**Note:** An active internet connection is required for the initial model download. The application also requires a working webcam.

## 🎮 Controls

- **Q** – Press Q to close the webcam.
- **Green Rectangle** – Person detected with a mask.
- **Red Rectangle** – Person detected without a mask.
- **Automatic Capture** – Saves detected photos every 5 seconds.

## 🏢 Real-World Applications

This project demonstrates how AI-based object detection can be applied in different industries:

- 🏥 Hospitals and Healthcare Facilities
- 🏭 Industrial Safety Monitoring
- 🏢 Office and Workplace Safety
- 🏫 Schools and Educational Institutions
- 🛍️ Shopping Malls and Public Places
- 🚪 Entry and Access Monitoring Systems

## 🚀 Future Improvements

- Develop a graphical user interface using CustomTkinter.
- Add a real-time detection counter.
- Generate Excel reports of mask detection results.
- Add date and time information to detection records.
- Support multiple camera inputs.
- Add an alert system for people detected without masks.
- Improve model accuracy under different lighting conditions.

## ⚠️ Limitations

- Requires a working webcam.
- Initial model download requires an internet connection.
- Detection accuracy depends on the trained model and camera quality.
- The application should not be considered a substitute for professional safety monitoring.

## 👩‍💻 Author

**Tejaswini Bhosale**

Python | Artificial Intelligence | Computer Vision | YOLO | OpenCV

## ⭐ Acknowledgement

This project was developed as a practical learning experience in Artificial Intelligence, Deep Learning, Computer Vision, and real-time object detection using Python.

If you like this project, don't forget to give it a ⭐ on GitHub!
