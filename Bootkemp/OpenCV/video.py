import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# face_cascade - переменная, CascadeClassifier - классификатор, у нас "лицо" (frontalface)

img = cv2.imread('test2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # конвертация в серые оттенки (черно-белая)

cv2.imshow('Result', img_gray)
cv2.waitKey(0)

faces = face_cascades.detectMultiScale(img_gray)
# находит координаты, в которых есть лица

for (x, y, w, h) in faces: # выбор лиц
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) # рисование прямоугольника

cv2.imshow('Result', img)
cv2.waitKey(0)

cap = cv2.VideoCapture(0)
# cap - переменная, содержащая видео (связь с веб-камерой, 0 - 1-я камера, 1 - 2-я и т.д.)
cap = cv2.VideoCapture('video.mp4')
# cap - переменная, содержащая видео (связь с видеофайлом)

# мы не знаем, сколько будет кадров, поэтому бесконечный цикл => 
while True:
    success, frame = cap.read() # считывание текущего кадра
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Result', frame) # вывод кадра

    if cv2.waitKey(1) & 0xff == ord('q'): # выход из цикла, когда мы нажмем q
        break