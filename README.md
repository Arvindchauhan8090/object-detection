# 🎯 Object Detection Using OpenCV (YOLO)

This project demonstrates **real-time object detection** using **YOLO (You Only Look Once)** and **OpenCV** in Python. It captures video from a live webcam and detects multiple objects with bounding boxes and labels.

---

## 🚀 Features

* 📷 Real-time object detection using webcam
* ⚡ Fast detection using YOLOv3
* 🧠 Pre-trained model on COCO dataset
* 🟩 Bounding boxes with object labels and confidence score
* 💻 Easy to run with simple terminal commands

---

## 🛠️ Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy
* YOLOv3 (Deep Learning Model)

---

## 📂 Project Structure

```
object-detection/
│── main.py
│── coco.names
│── yolov3.cfg
│── yolov3.weights
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Arvindchauhan8090/object-detection.git
cd object-detection
```

---

### 2️⃣ Install dependencies

```
pip install opencv-python numpy
```

---

### 3️⃣ Download YOLO files

Download and place these files in the project folder:

* **yolov3.weights**
* **yolov3.cfg**
* **coco.names**

---

## ▶️ Usage

Run the following command in terminal:

```
python main.py
```

* Press **ESC** to exit the webcam window.

---

## 🧠 How It Works

1. YOLO model is loaded using OpenCV DNN module
2. Webcam frames are captured in real-time
3. Each frame is processed and converted into a blob
4. YOLO predicts objects with bounding boxes
5. Non-Max Suppression removes duplicate detections
6. Final results are displayed on screen

---

## 📸 Output

* Live video stream with:

  * Object labels
  * Confidence scores
  * Bounding boxes

---

## ⚠️ Requirements

* Python 3.x
* Webcam
* Minimum 4GB RAM (recommended)

---

## 🐞 Troubleshooting

### Camera not opening?

Try:

```
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

### Slow performance?

* Reduce input size (416 → 320)
* Close background apps

---

## 📈 Future Improvements

* Upgrade to YOLOv8 🚀
* Add GPU acceleration (CUDA)
* Save detected images/videos
* Add custom object training

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgment

* YOLO by Joseph Redmon
* OpenCV community

---

⭐ If you like this project, don't forget to **star the repository!**
