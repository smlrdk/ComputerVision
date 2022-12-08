import cv2 as cv
import time

video_path = '../Lab1/data/video.mp4'
img_size = (700, 400)
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
        start = time.time()
        img_dilation = img_bin.copy()
        for x in range(img_bin.shape[0]): # высота
            for y in range(img_bin.shape[1]): # ширина
                if img_bin[x][y] == 255: # белый
                    for j in range(y-1, y+1+1):
                        for i in range(x-1, x+1+1):
                            if i >= 0 and i < len(img_dilation) and j >= 0 and j < len(img_dilation[0]):
                                img_dilation[i][j] = 255
        cv.imshow('frame', img_dilation)
        end = time.time()
        print(end-start)

    cv.imshow('frame', img_bin)
    
cap.release()
cv.destroyAllWindows()