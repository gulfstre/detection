from ultralytics import YOLO



model = YOLO('yolov8n.yaml')

results = model.train(data='coco.yaml', epochs=500, imgsz=640, name='yolov8n_our')
