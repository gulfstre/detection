import os
from detector_dataset_helpers import DetectorDatasetHelper as helper



PATH = '/usr/src/datasets/'

helper.create_folder(os.path.join(PATH, 'coco'))

helper.download_file_with_resume('http://images.cocodataset.org/zips/train2017.zip', PATH)
helper.unzip_file_nopaths(
    os.path.join(PATH, 'train2017.zip'), 
    os.path.join(PATH, 'coco', 'images', 'train2017')
)

helper.download_file_with_resume('http://images.cocodataset.org/zips/val2017.zip', PATH)
helper.unzip_file_nopaths(
    os.path.join(PATH, 'val2017.zip'), 
    os.path.join(PATH, 'coco', 'images', 'val2017')
)

helper.download_file_with_resume('https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip', PATH)
helper.unzip_file(
    os.path.join(PATH, 'coco2017labels.zip'), 
    os.path.join(PATH)
)

helper.download_file_with_resume('https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels-segments.zip', PATH)

helper.filter_labels_and_images(os.path.join(PATH, 'coco'), ['44', '65', '73'])
