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
    tensorflow) C:\> pip install lxml   
    (tensorflow) C:\> pip install Cython
    (tensorflow) C:\> pip install contextlib2
    (tensorflow) C:\> pip install jupyter
    (tensorflow) C:\> pip install matplotlib
    (tensorflow) C:\> pip install pandas
    (tensorflow) C:\> pip install opencv-python

Configure PYTHONPATH environment variable

    (tensorflow) C:\> set PYTHONPATH=C:\tensorflow\models;C:\tensorflow\models\research;C:\tensorflow\models\research\slim

(Give the command as per your given path for tensorflow\models). 

Note: Every time the "tensorflow" virtual environment is exited, the PYTHONPATH variable is reset and needs to be set up again. You can use "echo %PYTHONPATH% to see if it has been set or not.

## Compile Protobuf and setup.py

In the Anaconda Command Prompt, change directories to the \models\research directory:

    (tensorflow) C:\> cd C:\tensorflow\models\research

Paste the following command in this directory:

    protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto        .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto        .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto               .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

This will creates a name_pb2.py file from every name.proto file in the \object_detection\protos folder. You can check it if it's created or not.

Then, run the following command:

    (tensorflow) C:\tensorflow\models\research> python setup.py build
    (tensorflow) C:\tensorflow\models\research> python setup.py install


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
    
 
Download and install LabelImg, point it to your \images\train directory, and then draw a box around each object in each image. Repeat the process for all the images in the \images\test directory. This will take time as per your gathered images. 

LabelImg saves a .xml file containing the label data for each image. These .xml files will be used to generate TFRecords, which are one of the inputs to the TensorFlow trainer. Once you have labeled and saved each image, there will be one .xml file for each image in the \test and \train directories.

### Generate training data

It's time to generate tfrecords that serve as input data to the TensorFlow training model. For this, first you have to convert .xml to .csv all the data of train and test images. Then, download the xml_to_csv.py and generate_tfrecord.py from https://github.com/datitran/raccoon_dataset.

Now the xml data will used to create csv data using following command:

    (tensorflow) C:\tensorflow\models\research\object_detection> python xml_to_csv.py
    
This creates a train_labels.csv and test_labels.csv file in the \object_detection\images folder.

Now, the second part is to edit the generate_tfrecord.py file. Replace the label map starting with your own label map, where each object is assigned an ID number.

For example, say you are training a classifier to detect basketballs, shirts, and shoes. You will replace the following code in generate_tfrecord.py:

  #### TO-DO replace this with label map
  
    def class_text_to_int(row_label):
        if row_label == 'raspberry pi':
            return 1
        elif row_label == 'msp':
            return 2
        elif row_label == 'barcode':
            return 3
        elif row_label == 'mix':
            return 3
   
  #### with this
  
        def class_text_to_int(row_label):
            if row_label == 'basketball':
                return 1
            elif row_label == 'shirt':
                return 2
            elif row_label == 'shoe':
                return 3
            else:
                None      
     
 Just replace the row_label with your own label.
 
 Then, generate the TFRecord files by issuing these commands
 
    python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
    python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record
    
These generate a train.record and a test.record file in \object_detection. These will be used to train the new object detection classifier.

## Create label map and configuring training

The last thing to do before training is to create a label map and edit the training configuration file.

### Label map

The label map tells the trainer what each object is by defining a mapping of class names to class ID numbers. Use a text editor to create a new file and save it as labelmap.pbtxt in the C:\tensorflow1\models\research\object_detection\training folder.

The label map should be:

        item {
      id: 1
      name: 'raspberry pi'
    }

    item {
      id: 2
      name: 'msp'
    }

    item {
      id: 3
      name: 'barcode'
    }

    item {
      id: 4
      name: 'mix'

The label map ID numbers should be the same as what is defined in the generate_tfrecord.py file.

### Configure training

Finally, the object detection training pipeline must be configured. It defines which model and what parameters will be used for training. 

Here, I have used "ssd_mobilenet_v1_pets.config" file. You can find this file in C:\tensorflow\models\research\object_detection\samples\configs folder. Copy fro config folder and paste it into training directory. Then, open the file with a text editor. There are several changes to make to the .config file, mainly changing the number of classes and examples, and adding the file paths to the training data.

    -line 9, Change num_classes to the number of different objects you want the classifier to detect. For this e.g. the number would be 4.
    
    -line 156, Change fine_tune_checkpoint to:
    
    C:/tensorflow/models/research/object_detection/ssd_mobilenet_v1_coco_2018_01_28/model.ckpt"
    
    -line 176 and 178. In the train_input_reader section, change input_path and label_map_path to:
    
    input_path: "C:/tensorflow/models/research/object_detection/train.record
    
    label_map_path: "C:/tensorflow/models/research/object_detection/training/labelmap.pbtxt"
    
    -line 130. Change num_examples to the number of images you have in the \images\test directory.
    
    -line 188 and 190. In the test_input_reader section, change input_path and label_map_path to:
    
    input_path: "C:/tensorflow/models/research/object_detection/test.record
    
    label_map_path: "C:/tensorflow/models/research/object_detection/training/labelmap.pbtxt"
    
Save the file after the changes have been made. That’s it! The training job is all configured and ready to go!
    

## Run Training model

To train the model we will use the train.py file, which is located in the object_detection/legacy folder. We will copy it into the object_detection folder and from the \object_detection directory, issue the following command to begin training:

    python3 train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_pets.config
    
Training will start shortly. The initialization can take up to 30 seconds before the actual training begins.

Each step of training reports the loss. It will start high and get lower and lower as training progresses. For my training on the ssd-mobilenet-v1-coco, it started at about 20.0 and then slowly it dropped around 13-14. I trained the model until the loss consistently drop below 2. For this purpose, it will take about 20000 steps or about 7-8 hrs (depending on how powerful your CPU or GPU are). The losses will be different for different model. 

Parellely you can also see the progress of training model. Just open the new terminal of anaonda prompt and use this command in object_detection directory:

    (tensorflow) C:\tensorflow\models\research\object_detection>tensorboard --logdir=training
    
The training routine periodically saves checkpoints about every five minutes. You can terminate the training by pressing Ctrl+C while in the command prompt window.

## Export inference graph

I typically wait until just after a checkpoint has been saved to terminate the training. You can terminate training and start it later, and it will restart from the last saved checkpoint. The checkpoint at the highest number of steps will be used to generate the frozen inference graph.

You have to generate frozen inference graph file (.pb file) after completing the training. To run this, you just need to pass in your checkpoint and your pipeline config, then wherever you want the inference graph to be placed. From the \object_detection folder, issue the following command:

    python3 export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path training/ssd_mobilenet_v1_pets.config \
    --trained_checkpoint_prefix training/model.ckpt-XXXX \
    --output_directory inference_graph
 
  where “XXXX” in “model.ckpt-XXXX” should be replaced with the highest-numbered .ckpt file in the training folder.
    
  This creates a frozen_inference_graph.pb file in the \object_detection\inference_graph folder. The .pb file contains the object detection classifier.
  
  
  
## Test the trained model
  

  
  
  









    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



