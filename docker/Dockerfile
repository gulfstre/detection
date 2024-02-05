FROM ultralytics/ultralytics:8.1.8

WORKDIR /usr/src/

ENTRYPOINT ["sh", "-c", "git clone https://github.com/gulfstre/detection.git ./detection_repo/; exec \"${@}\"", "--"]
