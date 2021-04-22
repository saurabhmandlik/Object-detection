#### To run the trained object detection script:

##### You must have the trainning model. Training model includes following files:
1. Saved_model
2. checkpoint
3. frozen_inference_graph
4. labelmap.pbtxt
5. model.ckpt.data-0000-of-0001
6. model.ckpt.index
7. model.ckpt.meta
8. pipeline.config

Save this folder in /object_detection directory of tensorflow except labelmap.pbtxt file. Copy this .pbtxt file and paste it in /object_detection/data folder.

And finally run the command of .py script in cd /tensorflow/models/research/object_detection directory.


#### How to check when the training is finished or when do we stop to train the model?

As I have used SSD neural network to train our model, because it allows the faster detection of object with good accuracy. 

SSD 
