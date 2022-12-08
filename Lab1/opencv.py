import cv2 as cv
import time

video_path = '../Lab1/data/video.mp4'
img_size = (700, 400)
ksize = (3, 3) # размер примитива
cap = cv.VideoCapture(video_path)
is_dilated = 0 # переменная состояния, какое окно выводить

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print('Не удается получить кадр!')
        break

    # бинаризация
    img_gray = cv.cvtColor(cv.resize(img, img_size),cv.COLOR_BGR2GRAY)
    ret, img_bin = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

    key = cv.waitKey(20)
    # завершить работу программы по клавише q
    if key == ord('q'):
        break
    elif key == ord('d'):
        is_dilated = (is_dilated + 1) % 2

    if is_dilated:
        # дилатация
        for i in range(2):
            start = time.time()
            kernel = cv.getStructuringElement(cv.MORPH_RECT, ksize) # ядро
            img_dilation = cv.dilate(img_bin, kernel, img_bin)
            cv.imshow('frame', img_dilation)
            end = time.time()
            print(end-start)
     
    cv.imshow('frame', img_bin)
    
cap.release()
cv.destroyAllWindows()

