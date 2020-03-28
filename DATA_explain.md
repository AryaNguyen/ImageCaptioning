# MS-COCO DATASET EXPLAIN
The MS-COCO dataset is used for image captioning task. Go to [here](http://cocodataset.org/#download) to download the dataset. You need to download 2014 dataset for image captioning task. 
- Training data: 2014 Train images [83K/13GB]
- Valuating data: 2014 Val images [41K/6GB]
- Testing data: 2014 Test images [41K/6GB]
- Annotation: 2014 Train/Val annotations [241MB] 
<br> (you can delete instances_train2014.json, instances_val2014.json, person_keypoints.json, and person_keypoints_val2014.json because these are for object and keypoint detection tasks)

This is my file structure:
```
ImageCaptioning_LSTM
│   README.md
|   DATA_explain.md
│   .gitignore    
│
└───data
│   │   TRAIN_IMAGES_coco_5_cap_per_img_5_min_word_freq.hdf5
│   │   WORDMAP_coco_5_cap_per_img_5_min_word_freq.json
│   │
│   └───annotations
│   |   │   captions_train2014.json
│   |   │   captions_val2014.json
│   |   
│   └───train2014 // trainning images folder
|   |   ...
|   |
|   └───val2014 // valuating images folder
|   |   ...
|   |
|   └───test2014 // testing images folder
|   |   ...
|   |
|   
└───src
    |   datasets.py
    |   eval.py
    |   models.py
    │   train.py
    │   utils.py
```

- **WORDMAP_coco_5_cap_per_img_5_min_word_freq.json**: Vocabulary dictionary where keys are numbers and values are unique words
```json
{"a": 1, "man": 2, "with": 3, "red": 4, "helmet": 5,...}
```
- **TRAIN_IMAGES_coco_5_cap_per_img_5_min_word_freq.hdf5**: 
