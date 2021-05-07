# vehichle-number-plate-recognition
Recognition of the Liscence Plate of a four wheeler vehicle and then recognition of text written on the number plate using an OCR.

# About
- Uses YOLOv3(an object detection algorithm) implementation using keras & tensorflow and easyocr for OCR purpose.
- Dataset downloaded from https://www.kaggle.com/andrewmvd/car-plate-detection
- Dataset labelled with labelImg (https://github.com/tzutalin/labelImg)
- Model was trained by using transfer learning and it used pretrained darknet weights by freezing first 185 of 252 layers of the model.

# Dependencies
- Keras 2.1.5 (pip install keras==2.1.5)
- Tensorflow 1.x (pip install tensorflow)
- openCV (pip install cv2)
- easyocr (pip install easyocr && pip install imutils)

# How to run
- Make sure you have the dependencies installed 
- Go to kera-yolo3 directory (cd kera-yolo3)
- Download the Trained Model (Google Drive Link: https://drive.google.com/file/d/14iA1Z6JpV1WpA3UYdZSFnhVVFejBWOHL/view?usp=sharing) 
- Move the trained model to keras-yolo3/model_data
- Run python yolo_video.py --image (for recognition of number plate in an image)
- Enter path of the image to recognize
- Run predict.py
- The predicted image will be saved in prediction.jpg and the predicted number will be saved in num_plate.txt

# Input Image
![ss0](https://user-images.githubusercontent.com/43947335/117406764-1f637b80-af2b-11eb-8113-9a9f17234d7b.jpg)

# Trained model run on the input
![ss1](https://user-images.githubusercontent.com/43947335/117406839-44f08500-af2b-11eb-8dcd-5f4be20ee435.jpg)
![ss2](https://user-images.githubusercontent.com/43947335/117406853-4cb02980-af2b-11eb-9c1c-220029ec1548.jpg)

# Output
![ss3](https://user-images.githubusercontent.com/43947335/117406881-576abe80-af2b-11eb-816b-40913c8b71e5.jpg)
![ss4](https://user-images.githubusercontent.com/43947335/117406893-5d609f80-af2b-11eb-89de-c9ce15202079.jpg)

