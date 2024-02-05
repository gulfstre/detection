import os
from detectors import DetectorYolo8



ALLOWED_IMAGE_EXTENSIONS = ('.jpg', '.jpeg')
INPUT_DIR = '/usr/src/exchange/input/'
OUTPUT_DIR = '/usr/src/exchange/output/'
os.makedirs(OUTPUT_DIR, exist_ok=True)

detector = DetectorYolo8()

# Перебор всех файлов во входной директории
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(ALLOWED_IMAGE_EXTENSIONS):
        
        # Формирование путей к файлам
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '.txt')

        # Выполнение предсказания с помощью детектора
        predictions = detector.predict(f'{INPUT_DIR}{filename}')
        
        # Сохранение ограничивающих рамок в текстовый файл
        with open(output_path, 'w') as f:
            for prediction in predictions:
                for box in prediction.boxes:
                    f.write(f"{box}\n")
                
