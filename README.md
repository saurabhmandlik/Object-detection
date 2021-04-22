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

And finally run your object detection script in cd /tensorflow/models/research/object_detection directory.


#### How to check when the training is finished or when do we stop to train the model?

As I have used SSD object detection model to train our model, because it allows the faster detection of object with good accuracy. 

While training the model, you can see that the loss is started about 15-20 and quickly dropped around 7-9.  Each step of training reports the loss. For SSD model, we have to train our model until loss is consistently below 2. For getting consistently loss 2 will take 21000 steps or about 4-5 hrs. 

You can see the progress of training model below.


![image](https://user-images.githubusercontent.com/67440191/115701485-205faf00-a368-11eb-8ba8-26c2c0063db6.png)





