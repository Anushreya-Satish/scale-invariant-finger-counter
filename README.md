# 🖐️ Real-Time Scale-Invariant Finger Counter

A robust, real-time computer vision application that detects hand landmarks and accurately counts extended fingers using MediaPipe and OpenCV. This project features a custom distance-scaling algorithm that makes thumb tracking invariant to hand distance, rotation, or camera mirroring.

## 🚀 Features
* **Distance-Invariant Tracking:** Uses Euclidean distance ratios between the thumb tip and pinky base to ensure accurate tracking regardless of proximity to the webcam.
* **Real-time Performance:** Low-latency hand landmark mapping powered by MediaPipe.
* **Clean Visual Overlay:** Displays a live skeletal mesh and a dynamic on-screen counter interface.

## 🛠️ Built With
* Python 3.12
* OpenCV (Computer Vision Library)
* MediaPipe (Google's Open-Source ML Framework)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anushreya-satish/scale-invariant-finger-counter.git
   cd scale-invariant-finger-counter

2. **Create and activate a virtual environment (Python 3.12 recommended):**
    ```bash
    py -3.12 -m venv env
    env\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

## 🎮 Usage

**Run the main script to launch the application:**
    ```bash
    python app.py
* Press the Spacebar while focusing on the camera window to safely exit the application.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE). Feel free to fork, modify, and use it for your own directory cleanup needs!

---

<p align="center">
  🚀 <b>Built by a junior polyglot</b><br>
  <sub>Learning & Embarking on new Endeavours</sub>
</p>
