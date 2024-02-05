from detector_dataset_helpers import DetectorDatasetHelper as helper



path = '.'

helper.create_folder(os.path.join(path, 'coco'))

helper.download_file_with_resume('http://images.cocodataset.org/zips/train2017.zip', path)
helper.unzip_file_nopaths(
    os.path.join(path, 'train2017.zip'), 
    os.path.join(path, 'coco', 'images', 'train2017')
)

helper.download_file_with_resume('http://images.cocodataset.org/zips/val2017.zip', path)
helper.unzip_file_nopaths(
    os.path.join(path, 'val2017.zip'), 
    os.path.join(path, 'coco', 'images', 'val2017')
)

helper.download_file_with_resume('https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip', path)
helper.unzip_file(
    os.path.join(path, 'coco2017labels.zip'), 
    os.path.join(path)
)

helper.filter_labels_and_images(os.path.join(path, 'coco'), ['44', '65', '73'])
