from detectors import DetectorYolo8



ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg']
IMAGE_DIR = '/usr/src/input_images/'

detector = DetectorYolo8()

results = []
for filename in os.listdir(IMAGE_DIR):
    if filename.endswith(ALLOWED_IMAGE_EXTENSIONS):
        results.append(
            detector
                .predict(f'{IMAGE_DIR}{filename}')
                .boxes
        )

return results
