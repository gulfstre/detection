FROM ultralytics/ultralytics:8.1.8

ENTRYPOINT ["sh", "-c", "git clone https://github.com/gulfstre/detection.git ./detection_repo/; exec \"${@}\"", "--"]
