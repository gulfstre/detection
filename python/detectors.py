from ultralytics import YOLO



class DetectorYolo8:

    def __init__(self, model_name='yolov8n.pt'):
        """Инициализируем модель YOLO

        Args:
            model_name (str): Имя предварительно обученной модели YOLO, путь к собственной модели или имя схемы
        """
        
        self.model = YOLO(model_name)


    def predict(self, img):
        """Инференс

        Args:
            img_path (str): Путь к изображению для предикта

        Returns:
            results: Результаты детекции
        """
        results = self.model(img)
        return results
