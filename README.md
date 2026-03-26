# Real-Time Face Detection System (OpenCV)

A simple and efficient real-time face detection system built using OpenCV in Python. This project captures video from your webcam, detects faces using Haar Cascade, and displays useful information like face count, FPS, and timestamp.

---

## Features

- Real-time webcam face detection  
- Multiple face detection support  
- Live face count display  
- Timestamp overlay  
- FPS (Frames Per Second) calculation  
- Exit using 'q' key  

---

## Project Structure

face-detection/
│── main.py  
│── haarcascade_frontalface_default.xml  
│── README.md  

---

## Requirements

Make sure you have Python installed (>=3.7 recommended)

Install dependencies:

pip install opencv-python

---

## Setup Instructions

1. Clone the repository:

git clone https://github.com/your-username/face-detection.git  
cd face-detection  

2. Download Haar Cascade file:  

haarcascade_frontalface_default.xml  

3. Place it in the project directory.

---

## How to Run

python main.py

---

## How It Works

1. The webcam is initialized using OpenCV.  
2. Each frame is converted to grayscale.  
3. Haar Cascade classifier detects faces.  
4. Bounding boxes are drawn around detected faces.  
5. Additional information displayed:
   - Face count  
   - Current timestamp  
   - FPS (performance metric)

---

## Output

- Blue rectangles → Detected faces  
- Green text → Face count  
- White text → Timestamp  
- Yellow text → FPS  

---

## Controls

| Key | Action |
|-----|--------|
| q   | Quit the application |

---

## Common Issues

### Camera not working
- Check if another app is using the webcam  
- Try changing camera index:

cv2.VideoCapture(1)

### Cascade file not loading
- Ensure file path is correct:

cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

---

## Future Improvements

- Face recognition (not just detection)  
- Mask detection  
- Emotion detection  
- Save detected faces  
- GUI dashboard  

---

## Contributing

Pull requests are welcome. Feel free to fork this repository and improve it.

---

## License

This project is open-source and available under the MIT License.

---

## Author

Mayank Mishra
