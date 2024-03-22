# Potato-Disease-Classification-with-CNN

#### Dataset credits: https://www.kaggle.com/arjuntejaswi/plant-village

### Introduction:

The project "Potato Disease Classification using CNN" focuses on developing a Convolutional Neural Network (CNN) model to accurately classify images `almost 100% accuracy` of potato plants into three categories: `healthy, early blight, and late blight potato`. Early and late blight are common fungal diseases that significantly impact potato yield and quality. By leveraging CNN technology, this project aims to automate disease detection, enabling early intervention and effective disease management strategies. The ultimate goal is to contribute to sustainable potato production by providing farmers with a reliable tool for timely diagnosis and treatment of blight infections.

### Workflows

#### Import data into tensorflow dataset object
I used image_dataset_from_directory api to load all images in tensorflow dataset: https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory

#### Visualize some of the images from our dataset
<img width="400" alt="image" src="https://github.com/engineersakibcse47/Potato-Disease-Classification-with-CNN/assets/108215990/aaa4de3c-a614-4990-96c1-5d17b0dc876e">

#### Function to Split Dataset

Dataset bifurcated into 3 subsets, namely:
- `Training`: Dataset to be used while training
- `Validation`: Dataset to be tested against while training
- `Test`: Dataset to be tested against after we trained a model

#### Set Cache, Shuffle, and Prefetch with Dataset

`train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)`
`val_ds = val_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)`
`test_ds = test_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)`

#### Building the Model

##### Creating a Layer for Resizing and Normalization

Before feed images to network, we should be resizing it to the desired size.
Moreover, to improve model performance, we should normalize the image pixel value (keeping them in range 0 and 1 by dividing by 256). This should happen while training as well as inference. Hence we can add that as a layer in our Sequential Model.
You might be thinking why do we need to resize (256,256) image to again (256,256). You are right we don't need to but this will be useful when we are done with the training and start using the model for predictions. At that time somone can supply an image that is not (256,256) and this layer will resize it.

#### Data Augmentation
Data Augmentation is needed when we have less data, this boosts the accuracy of our model by augmenting the data.

`data_augmentation = tf.keras.Sequential([`
  `layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),`
  `layers.experimental.preprocessing.RandomRotation(0.2),`
`])`

#### Model Architecture
I used CNN coupled with a Softmax activation in the output layer. Also add the initial layers for resizing, normalization and Data Augmentation.

#### Compiling the Model
I used `adam` Optimizer, `SparseCategoricalCrossentropy` for losses, accuracy as a metric.

#### Plotting the Accuracy and Loss Curves
<img width="400" alt="image" src="https://github.com/engineersakibcse47/Potato-Disease-Classification-with-CNN/assets/108215990/60f37408-a26a-40b5-af74-5194d2ffa062">

#### Write a function for inference to evaluate few sample images
<img width="400" alt="image" src="https://github.com/engineersakibcse47/Potato-Disease-Classification-with-CNN/assets/108215990/6c59dd4a-7742-4376-b7a3-1c51af1cc61e">

#### Saving the Model
I append the model to the list of models as a new version.
`import os`
`latest_version = max([int(i) for i in os.listdir("saved_models")] + [0]) + 1`
`model.save(f"saved_models/{latest_version}")`

#### Deployment Testing Using FastAPI
I tried with FstAPI and tested responses(predictions) through Postman(https://www.postman.com/downloads/). 



















