## Download Tensorflow Object Detection API from github

https://github.com/tensorflow/models

### Set up the new anoconda tensorflow environment

First you have to create a new tensorflow environment using following command:

C:\> conda create -n tensorflow pip python=3.7

then, activate the tensorflow environment by issuing:

C:\> activate tensorflow

Install tenorflow in this environment by issuing:

(tensorflow) C:\> pip install --ignore-installed --upgrade tensorflow

Note: You can also use tensorflow-gpu version then just use "tensorflow-gpu" instead of "tensorflow".

Install the all dependencies

(tensorflow) C:\> conda install -c anaconda protobuf
(tensorflow) C:\> pip install pillow
(tensorflow) C:\> pip install lxml
(tensorflow) C:\> pip install Cython
(tensorflow) C:\> pip install contextlib2
(tensorflow) C:\> pip install jupyter
(tensorflow) C:\> pip install matplotlib
(tensorflow) C:\> pip install pandas
(tensorflow) C:\> pip install opencv-python

### Configure PYTHONPATH environment variable

(tensorflow) C:\> set PYTHONPATH=C:\tensorflow\models;C:\tensorflow\models\research;C:\tensorflow\models\research\slim

(Give the command as per your given path for tensorflow\models). 

Note: Every time the "tensorflow" virtual environment is exited, the PYTHONPATH variable is reset and needs to be set up again. You can use "echo %PYTHONPATH% to see if it has been set or not.





