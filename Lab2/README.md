# Лабораторная работа № 2 по дисциплине "Компьютерное зрение". 
(Солодкая Мария, магистратура, 1 курс)

## Задание:
Необходимо реализовать два примитивных детектора объектов на изображении, работающих с помощью поиска эталона на входном изображении.
1. Прямой поиск одного изображения на другом (template matching)
2. Поиск ключевых точек эталона на входном изображении (например, с помощью SIFT, ORB..)

Программа должна принимать на вход два изображения, эталон и то, на котором будет производиться поиск. На выходе программа должна строить рамку в виде четырехугольника в области, где с наибольшей вероятностью находится искомый объект. Необходимо протестировать оба варианта программы на разных изображениях (например, сначала в качестве эталона использовать вырезанный фрагмент входного изображения, а затем изображение какого-либо предмета сцены, присутствующего на входном

## Теоретическая база
**Прямой поиск одного изображения на другом (template matching)** — это метод поиска и нахождения расположения шаблонного изображения на большом изображении. OpenCV поставляется с функцией cv.matchTemplate() для этой цели. Он просто наводит изображение шаблона на входное изображение (как в 2D-свертке) и сравнивает шаблон и фрагмент входного изображения с изображением шаблона. В OpenCV реализовано несколько методов сравнения. Он возвращает изображение в градациях серого, где каждый пиксель обозначает, насколько окрестности этого пикселя совпадают с шаблоном.

Если входное изображение имеет размер (ШхВ), а шаблонное изображение имеет размер (шхв), выходное изображение будет иметь размер (Ш-ш+1, В-ч+1). Получив результат, вы можете использовать функцию cv.minMaxLoc(), чтобы найти максимальное/минимальное значение. Возьмите его как верхний левый угол прямоугольника и примите (ш,в) как ширину и высоту прямоугольника. Этот прямоугольник является вашей областью шаблона.

**Поиск ключевых точек эталона на входном изображении (ORB)**
Детектирование с помощью ключевых точек использует алгоритм ORB. Этот алгоритм вычисляет массив ключевых точек, состоящий из их координат и дескрипторов. Такие массивы вычисляются для входного изображения и эталона. После чего вычисляется массив матчей, то есть совпадений точек. Из этого массива выбираются N пар ближайших точек, число N является параметром алгоритма. Далее для всех этих точек для входного изображения выбираются верхняя левая и нижняя правая. Они и являются координатами рамки.

## Описание разработанной системы

#### Этапы работы скриптов: 
1. Загрузка изображений в массив (одно эталонное изображение и 11 изображений с объектом).
2. Реализация поиска эталона на изображении.
3. Рисование рамки вокруг найденного объекта.
4. Вывод полученных результатов по каждому изображению с эталоном и изображению с найденным объектом в рамке.

## Результаты работы и тестирования системы
Вся работа представлена в файле solution.ipynb с наглядным представлением результатов работы.

## Выводы по работе
В ходе выполнения лабораторной работы были реализованы два алгоритма детектирования объектов на изображении:
* алгоритм прямого поиска;
* алгоритм поиска по ключевым точкам.
А также проведено тестирование алгоритмов на основе 10 изображений.

Алгоритм прямого поиска показывает наилучшие результаты, если эталонным изображением является фрагмент исходного. Зеркальное отображение исходного изображения, повороты мешают алгоритму находить объект на изображении.

Алгоритм с использованием поиска по ключевым точкам смог справиться с зеркальным отображением и поворотами. Однако в рамку попадают другие объекты, находящиеся на изображении. Что являтеся достаточно критичным явлением.

У каждого алгоритма есть как достоинства, так и недостатки. При выборе алгоритма для детектирования объектов на изображении рекомендуется руководствоваться не только рассмотренными выше алгоритмами.

## Использованные источники
1. https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
2. https://docs.opencv.org/3.4/d1/d89/tutorial_py_orb.html
3. https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html