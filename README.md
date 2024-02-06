В данном репозитории реализованы обучение и предикт модели-детектора объектов на изображениях.

### Обучение.

Производилось на части датасета <a href="https://cocodataset.org/#explore" target="_blank">coco</a>. Этот датасет содержит несколько десятков классов, которые могут быть интересны в нашей задаче. С целью ускорения обучения, а также учитывая то, что нас как раз может интересовать детекция лишь ограниченного круга классов из этого датасета, были выбраны 3 класса (__44: spoon__, __65: remote__, __73: book__). Заметим, что объекты этих классов небольшие по габаритам и метрики их детекции ощутимо ниже метрик многих других классов. 

В качестве моделей использовались [yolov8](https://docs.ultralytics.com/ru/tasks/detect/#models) модификации "n" и "m". Модификация "n"обучалась в течение 150 эпох. Модификация "m" - 265 эпох. Логи обучения находятся в папке __runs__.

Валидационный сплит датасета __coco__ также отфильтрован по 3 выбранным классам и на нём результаты сравнивались со стандартными моделями __yolov8n__ и __yolov8m__. Сравнительная таблица метрик приведена ниже:

| Класс | Модель | mAP50 | mAP50-95 |
|:------------|:-----------:|:-----------:|------------:|
| spoon | "n" | 0.224 | 0.140 |
|  | "n" ours | 0.249 | 0.151 |
|  | "m" | 0.503 | 0.349 |
|  | "m" ours| 0.394 | 0.262 |
| remote | "n" | 0.322 | 0.189 |
|  | "n" ours | 0.438 | 0.256 |
|  | "m" | 0.629 | 0.421 |
|  | "m" ours| 0.578 | 0.371 |
| book | "n" | 0.223 | 0.111 |
|  | "n" ours | 0.221  | 0.106 |
|  | "m" | 0.333 | 0.191 |
|  | "m" ours| 0.274  | 0.151 |
| all | "n" | 0.256  | 0.147 |
|  | "n" ours | 0.303  | 0.171 |
|  | "m" | 0.488 | 0.32 |
|  | "m" ours| 0.415   | 0.261 |

Как видим, удалось достичь показателей близких к моделям от __yolo__. А по модификации "n" - даже лучше, на использованном валидационном датасете.

### Обучение детектора.

Можно осуществить в докер контейнере. Для этого запускаем контейнер из образа (~15 gb) на основе приложенного докерфайла в интерактивном режиме. По желанию вносим изменения в файлы /python/dataset_prepare_example.py и /python/train_example.py и запускаем их в контейнере последовательно (характерное время выполнения - порядок десятков минут на подготовку датасета и порядок часов на 100 эпох обучения на gpu, для работы с датасетом потребутся около 40-50 gb на диске), репозиторий клиноруется при создании контейнера в папку __/usr/src/detection_repo/__ . При запуске контейнера следует передать команду __bash__ .

В ходе тестирования было замечено, что __yolov8__ не работает на некотором железе, наиболее вероятно, на __cpu__ без поддержки __avx2__.

### Модели инференса.

В качестве модели можно использовать стандартные модели __yolov8__, а также передать пути к собственным моделям, переданным в контейнер.

### Запуск предикта.

Реализован в виде подачи примаунченной к __/usr/src/exchange/__ папки с подпапками __input__ и __output__. В папке __input__ следует разместить изображения __jpg/jpeg__, другие форматы можно разрешить в файле __/python/detect_example.py__ , который и необходимо запустить в контейнере (подробнее выше в трейне) для инференса. По каждому изображению из папки __input__ в папку __output__ будут выданы предикты в одноименные файлы __txt__.

В условиях работы робота, вероятно, изображения на вход будут приходить не в виде файлов, но для демонстрации удобнее использовать файлы.
