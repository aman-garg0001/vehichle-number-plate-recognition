import cv2
import easyocr

file = open('output.txt', 'r')
names = file.readlines()
file_name = names[0].split('\n')[0]
img = cv2.imread(file_name)
frame_thickness = 3
color = (255, 0, 0)
number_plate = []
for i in range(1, len(names)):
  lines = names[i]	
  line = lines.split(" ") 
  top_left = (int(line[0]), int(line[1])) 
  bottom_right = (int(line[2]), int(line[3]))
  number_plate.append(img[top_left[1]: bottom_right[1], top_left[0]: bottom_right[0]])
  cv2.rectangle(img,top_left,bottom_right, color, frame_thickness)
cv2.imwrite("prediction.jpg", img)

f2write = open("num_plate.txt", "w")
for numbers in number_plate:
  gray = cv2.cvtColor(numbers, cv2.COLOR_BGR2GRAY)
  reader = easyocr.Reader(['en'])
  result = reader.readtext(gray)
  text = 'The number plate read by the OCR is <' + result[0][-2] + '>\n'
  print(text)
  f2write.write(text)
f2write.close()
file.close()  