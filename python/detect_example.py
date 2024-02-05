import os
from detectors import DetectorYolo8



ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg']
INPUT_DIR = '/usr/src/exchange/input_images/'
OUTPUT_DIR = '/usr/src/exchange/output_images/'

detector = DetectorYolo8()

# Перебор всех файлов во входной директории
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(ALLOWED_IMAGE_EXTENSIONS):
        
        # Формирование путей к файлам
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '.txt')

        # Выполнение предсказания с помощью детектора
        prediction = detector.predict(f'{INPUT_DIR}{filename}')
        # Получение ограничивающих рамок
        boxes = prediction.boxes

        # Сохранение ограничивающих рамок в текстовый файл
        with open(output_path, 'w') as f:
            for box in boxes:
                f.write(f"{box}\n")
                
