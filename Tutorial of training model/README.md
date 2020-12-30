## Download Tensorflow Object Detection API from github

https://github.com/tensorflow/models

### Set up the new anoconda tensorflow environment

First you have to create a new tensorflow environment using following command:

##### C:\> conda create -n tensorflow pip python=3.7

then, activate the tensorflow environment by issuing:

##### C:\> activate tensorflow

Install tenorflow in this environment by issuing:

##### (tensorflow) C:\> pip install --ignore-installed --upgrade tensorflow

Note: You can also use tensorflow-gpu version then just use "tensorflow-gpu" instead of "tensorflow".

Install the all dependencies

##### (tensorflow) C:\> conda install -c anaconda protobuf

##### (tensorflow) C:\> pip install pillow

##### (tensorflow) C:\> pip install lxml

##### (tensorflow) C:\> pip install Cython

##### (tensorflow) C:\> pip install contextlib2

##### (tensorflow) C:\> pip install jupyter

##### (tensorflow) C:\> pip install matplotlib

##### (tensorflow) C:\> pip install pandas

##### (tensorflow) C:\> pip install opencv-python

### Configure PYTHONPATH environment variable

##### (tensorflow) C:\> set PYTHONPATH=C:\tensorflow\models;C:\tensorflow\models\research;C:\tensorflow\models\research\slim

(Give the command as per your given path for tensorflow\models). 

Note: Every time the "tensorflow" virtual environment is exited, the PYTHONPATH variable is reset and needs to be set up again. You can use "echo %PYTHONPATH% to see if it has been set or not.

### Compile Protobuf and setup.py

In the Anaconda Command Prompt, change directories to the \models\research directory:

##### (tensorflow) C:\> cd C:\tensorflow\models\research

Paste the following command in this directory:

##### protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

This will creates a name_pb2.py file from every name.proto file in the \object_detection\protos folder. You can check it if it's created or not.

Then, run the following command:

##### (tensorflow) C:\tensorflow\models\research> python setup.py build

##### (tensorflow) C:\tensorflow\models\research> python setup.py install


## Gather and label images

We need to provide the images it will use to train a new detection classifier.

### 1) Gather Images

Make sure the images aren’t too large. They should be less than 200KB each, and their resolution shouldn’t be more than 720x1280. The larger the images are, the longer it will take to train the classifier. 

You can use the following python script to reduce the size of the images.

from PIL import Image
import os
import argparse
    def rescale_images(directory, size):
        for img in os.listdir(directory):
            im = Image.open(directory+img)
            im_resized = im.resize(size, Image.ANTIALIAS)
            im_resized.save(directory+img)
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Rescale images")
        parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
        parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
        args = parser.parse_args()
        rescale_images(args.directory, args.size)
    
    
Create an folder with the name of images in the object detection directory of tensorflow/models. In that image folder, create another two folders as a test image and train image. Move 20% of the images into test directory and 80% of the images into train directory. Make sure there are a variety of pictures in both the \test and \train directories.

### 2)Label Images

Let's do some fun! Now you have to label all the images that you have in the image folder. For that, Labelimg is the best tool to fulfill our task. 
You can see the information about it and also download it through below links:

https://github.com/tzutalin/labelImg

https://www.dropbox.com/s/tq7zfrcwl44vxan/windows_v1.6.0.zip?dl=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



