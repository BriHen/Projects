# Pokemon Type Prediction
The goal of the project is to predict the type of a pokemon given an image of it.

## Learning Points

After completing this project, you should be able to understand the following.

### Data

* Cleaning and organizing data
* Reading in images
* Normalizing images
* One-hot vectors for labels
* Working with numpy arrays and Pytorch/Tensorflow tensors

### Machine Learning

* Support Vector Machines
* Fully connected neural network
* Convolutional Neural Network (CNN)
* Train/test/val
* Gradient descent
    * Learning rate
    * Batch size

### Instructions

#### Data

The data comes from [here](https://veekun.com/dex/downloads). You can download it using the script in the pokemon folder.
The labels can be downloaded [here](https://www.kaggle.com/abcsds/pokemon). Later, you'll have to associate the images with
their respective label, Type 1.

`./pokemon/download.sh`

This will download the data to the folder `pokemon/data/`. You'll need to
extract them using something like `tar -xvf generation-1.tar.gz`.

After they're all extracted, you'll have a folder
`pokemon/data/pokemon/main-sprites/` with all of the generations in there.  You
can move that out if you'd like, for example `mv
pokemon/data/pokemon/main-sprites/* pokemon/data/`.

From here you'll need to do a bit of data cleaning. Most of the pokemon are
named `<ID>.png`, where `ID` is their pokedex ID. However, you'll see that some
are named like `201-f.png`, since that image corresponds to the female version of
that Pokemon. You can either delete these images (`find pokemon/data/ -iname '*-*.png`),
or write your data reader to be able to use them. Just a tip, more data is better.


#### Algorithms

##### Support Vector Machine (SVM)

https://scikit-learn.org/stable/modules/svm.html


##### Fully Connected Neural Network



##### Convolutional Neural Network

#### Current Status
*Cleaning Sprite Names

#### Completed Tasks
*Downloaded All Sprites and Label Names
*Unzip Sprites
*Started Research on Data Cleaning
*Installed Ubunto on Desktop





