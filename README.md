# vehichle-number-plate-recognition
Recognition of the Liscence Plate of a four wheeler vehicle and then recognition of text written on the number plate using an OCR.

# About
- Uses YOLOv3(an object detection algorithm) implementation using keras & tensorflow and easyocr for OCR purpose.
- Dataset downloaded from https://www.kaggle.com/andrewmvd/car-plate-detection
- Dataset labelled with labelImg (https://github.com/tzutalin/labelImg)

# Dependencies
- Keras 2.1.5 (pip install keras==2.1.5)
- Tensorflow 1.x (pip install tensorflow)
- openCV (pip install cv2)
- easyocr (pip install easyocr && pip install imutils)

# How to run
- Make sure you have the dependencies installed 
- Clone github repository https://github.com/qqwweee/keras-yolo3 containing implementation of YOLOv3 using keras.
- Go to keras-yolo3 directory (cd keras-yolo3)
- Download the Trained Model (Google Drive Link: https://drive.google.com/file/d/14iA1Z6JpV1WpA3UYdZSFnhVVFejBWOHL/view?usp=sharing) 
- Run python yolo_video.py --image (for recognition of number plate in an image)
- Enter path of the image to recognize
- Run predict.py
- The predicted image will be saved in prediction.jpg and the predicted number will be saved in num_plate.txt
