# -*- coding: utf-8 -*-
"""LandT_Xception.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IMnIkzso03eehvJbsZszCoVnrRi8Auqc
"""

# from google.colab import drive
# drive.mount('/content/drive/')

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, BatchNormalization, Dropout, Activation, MaxPooling2D, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.losses import CategoricalCrossentropy
import PIL
from keras.callbacks import EarlyStopping
from keras import optimizers
import os
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications import ResNet50
from keras.applications.inception_v3 import InceptionV3
from keras.applications.xception import Xception
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.optimizers import SGD, Adam, RMSprop
import tensorflow as tf
from keras.models import Model

train_data_dir= '/Data/train/'
val_data_dir= '/Data/valid/'

batch_size=64

train_datagen = ImageDataGenerator(
rescale=1./255)


train_it = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(224,224),
    batch_size=batch_size,
    class_mode='binary',
    subset='training') # set as training data

val_it = train_datagen.flow_from_directory(
    val_data_dir, 
    target_size=(224,224),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation') # set as validation data

# Your model here ...
trained_model = InceptionV3(input_shape = [299, 299] + [3], weights='imagenet', include_top=False)
  
for layer in trained_model.layers[:229]:
  layer.trainable = False

for layer in trained_model.layers[229:]:
    layer.trainable = True
  
x = trained_model.output
x = GlobalAveragePooling2D()(x)

# let's add a fully-connected layer
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)

# this is the model we will train
model = Model(inputs = trained_model.input, outputs = predictions)
model.compile(optimizer=RMSprop(learning_rate =0.0005, decay = 1e-6), loss='binary_crossentropy', metrics=['acc',tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])
#model.compile(optimizer=Adam(learning_rate = 0.0005, decay = 1e-6), loss='binary_crossentropy', metrics=['acc',tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])

#model.compile(tf.optimizers.Adam(learning_rate=0.0001, decay=1e-6), loss=CategoricalCrossentropy(), metrics='acc')
model.fit(
train_it,
steps_per_epoch = train_it.samples //batch_size,
validation_data = val_it, 
validation_steps = val_it.samples // batch_size,
epochs = 20,
verbose=1,
callbacks=[EarlyStopping(patience=10,restore_best_weights=True)])

test_datagen = ImageDataGenerator(rescale=1./255.)
test_data_dir = '/Data/test/'

test_it = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(299,299),
    batch_size=1,
    class_mode='binary',
    shuffle=False
)

test_loss, test_accuracy,test_pre,test_recall  = model.evaluate(test_it)
print('test_loss = ', test_loss, ', test_accuracy = ',  test_accuracy , 'test_precision=', test_pre , 'test_recall=', test_recall , 'test_f1=', 2*test_pre*test_recall/(test_pre+test_recall))

import numpy as np
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow

p='/Data/predict/'
c=0
for i in os.listdir(p):
  image_path = p+i
  image = tf.keras.preprocessing.image.load_img(image_path,target_size=(299,299))
  input_arr = tf.keras.preprocessing.image.img_to_array(image)
  input_arr = input_arr*(1./255)
  input_arr = np.array([input_arr])  # Convert single image to a batch.
  prediction = model.predict(input_arr)
  img = cv2.imread(image_path)
  h,w,c = img.shape
  img = cv2.resize(img, (h//10, w//10))  
  cv2_imshow(img)
  if prediction>=0.5:
    print('\n Positive')
  else:
    print('\n Negative')

