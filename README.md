# ImageSegmentationAI
НЕОБХОДИМЫЕ БИБЛИОТЕКИ:
  1. Tensorflow
  2. pillow
  3. pixellib
  4. customtkinter

ОБЯЗАТЕЛЬНО СКАЧАТЬ ИЗ РЕПОЗИТОРИЯ:
  1. main.py
  2. AI.py

СКАЧАЙТЕ ФАЙЛ: "mask_rcnn_coco.h5" ПО ССЫЛКЕ:
  https://github.com/matterport/Mask_RCNN/releases/tag/v1.0


Перейдите в папку Pixellib -> semantic -> deeplab.py в вашем установленном местоположении Pixellib и замените строку. Замените "from tensorflow.python.keras.layers import BatchNormalization" на "from keras.layers.normalization.batch_normalization import BatchNormalization"
