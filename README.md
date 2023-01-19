# LandT-Edutech-Hackathon

This repository contains the code for the classification models used and it also provides the judging metrics (precision, recall and f1 score for all the models)

Evaluation metrics on test data and Predictions by different models. These can be verified by looking at the output of the corressponding ipynb files.



**Xception**

| Metric | Value |
| --- | --- |
| Precision | 1 |
|Recall | 1 |
|F1     |  1 |


|Image|Prediction|
| --- | --- |
|IMG_1129| Positive|
|IMG_1130| Positive|
|IMG_1131| Positive|
|IMG_1132| Positive|
|IMG_1133| Positive|
|IMG_1134| Positive|

**InceptionV3**


| Metric | Value |
| --- | --- |
| Precision | 0.99 |
|Recall | 1 |
|F1     |  0.995 |

|Image|Prediction|
| --- | --- |
|IMG_1129| Positive|
|IMG_1130| Negative|
|IMG_1131| Negative|
|IMG_1132| Positive|
|IMG_1133| Positive|
|IMG_1134| Positive|


**InceptionResnetV2**


| Metric | Value |
| --- | --- |
| Precision | 0.99 |
|Recall | 1 |
|F1     |  0.995 |

|Image|Prediction|
| --- | --- |
|IMG_1129| Negative|
|IMG_1130| Negative|
|IMG_1131| Negative|
|IMG_1132| Positive|
|IMG_1133| Positive|
|IMG_1134| Negative|


**Vgg16**


| Metric | Value |
| --- | --- |
| Precision | 1|
|Recall | 1 |
|F1     |  1 |

|Image|Prediction|
| --- | --- |
|IMG_1129| Negative|
|IMG_1130| Negative|
|IMG_1131| Negative|
|IMG_1132| Negative|
|IMG_1133| Negative|
|IMG_1134| Negative|





**Conclusions**

1. The 6 images used for prediction are quite different compared to the images in train, test and valid datasets.
2. The images in the test,train and valid datasets,the crack and background are clearly differentiable. (background surface color and crack color are clearly seperable). This is not the case with the images used for prediction(crack and background are barely separable).
3. Xception has performed quite well on the test data and it had also correctly predicted (with probability of nearly 1) the classes of all the images in the predict folder.
4. A more powerful and generalized model can be obtained by taking the majority voting of different pretrained models for the final prediction.