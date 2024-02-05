FROM ultralytics/ultralytics:8.1.8

ENTRYPOINT ["sh", "-c", "git clone https://github.com/gulfstre/detection.git /usr/src/detection_repo/; exec \"${@}\"", "--"]
