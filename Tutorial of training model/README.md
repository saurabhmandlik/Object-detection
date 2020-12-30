## Download Tensorflow Object Detection API from github

https://github.com/tensorflow/models

### Set up the new anoconda tensorflow environment

First you have to create a new tensorflow environment using following command:

##### C:\> conda create -n tensorflow pip python=3.7

then, activate the tensorflow environment by issuing:

##### C:\> activate tensorflow

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

### Compile Protobuf and setup.py

In the Anaconda Command Prompt, change directories to the \models\research directory:

(tensorflow) C:\> cd C:\tensorflow\models\research

Paste the following command in this directory:

protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

This will creates a name_pb2.py file from every name.proto file in the \object_detection\protos folder. You can check it if it's created or not.

Then, run the following command:

(tensorflow) C:\tensorflow\models\research> python setup.py build

(tensorflow) C:\tensorflow\models\research> python setup.py install


## Gather and label images


