import cv2

# picture = cv2.imread(r"C:\filiki\code 2\firsr_67\images\people.png")

# img = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

# model = cv2.CascadeClassifier(r"C:\filiki\code 2\firsr_67\neiros.xml")

# result = model.detectMultiScale(picture, scaleFactor = 2, minNeighbors = 3)

# for (x, y, w, h) in result:
#     cv2.rectangle(picture, (x, y), (x+w, h+y), (255, 0, 0), 4)

# cv2.imshow("picture", picture)
# cv2.waitKey(0)



picture = cv2.VideoCapture(0)
model = cv2.CascadeClassifier(r"C:\filiki\code 2\firsr_67\neiros.xml")
picture.set(cv2.CAP_PROP_FPS, 24)

while True:
    stat, img = picture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = model.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, h+y), (0, 0, 255), 4)

    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
        break

