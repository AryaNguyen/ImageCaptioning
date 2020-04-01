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
```
{"a": 1, "man": 2, "with": 3, "red": 4, "helmet": 5,...}
```
- **TRAIN_IMAGES_coco_5_cap_per_img_5_min_word_freq.hdf5**: 
- **caption_datasets/dataset_coco.json**
```json
{
  "images": 
    [
      {
      "filepath":  "val2014",
      "sentids": [770337, 771687, 772707, 776154, 781998],
      "filename": "COCO_val2014_000000391895.jpg",
      "imgrid": 0,
      "split": "test",
      "sentences": 
        [
          {"tokens": ["a", "man", "with", "a", "red", "helmet", "on", "a", "small", "moped", "on", "a", "dirt", "road"], "raw": "A man with a red helmet on a small moped on a dirt road. ", "imgid": 0, "sentid": 770337}, 
          {"tokens": ["man", "riding", "a", "motor", "bike", "on", "a", "dirt", "road", "on", "the", "countryside"], "raw": "Man riding a motor bike on a dirt road on the countryside.", "imgid": 0, "sentid": 771687}, 
          {"tokens": ["a", "man", "riding", "on", "the", "back", "of", "a", "motorcycle"], "raw": "A man riding on the back of a motorcycle.", "imgid": 0, "sentid": 772707}, 
          {"tokens": ["a", "dirt", "path", "with", "a", "young", "person", "on", "a", "motor", "bike", "rests", "to", "the", "foreground", "of", "a", "verdant", "area", "with", "a", "bridge", "and", "a", "background", "of", "cloud", "wreathed", "mountains"], "raw": "A dirt path with a young person on a motor bike rests to the foreground of a verdant area with a bridge and a background of cloud-wreathed mountains. ", "imgid": 0, "sentid": 776154}, 
          {"tokens": ["a", "man", "in", "a", "red", "shirt", "and", "a", "red", "hat", "is", "on", "a", "motorcycle", "on", "a", "hill", "side"], "raw": "A man in a red shirt and a red hat is on a motorcycle on a hill side.", "imgid": 0, "sentid": 781998}
        ],
      "cocoid": 391895
      }
    ],
  "data":  "coco"
}
```
- **annotations/caption_train2014.json**
```json
{
  "info": {},
  "images": [
    {
      "license": 5,
      "file_name": "COCO_train2014_000000057870.jpg",
      "coco_url": "http://images.cocodataset.org/train2014/COCO_train2014_000000057870.jpg",
      "height": 480,
      "weight": 640,
      "date_capture": "2013-11-14 16:28:13",
      "flickr_url": "http://farm4.staticflickr.com/3153/2970773875_164f0c0b83_z.jpg",
      "id": 57870
    }
  ],
  "licenses": [],
  "annotations": [
    {
      "image_id": 318556,
      "id": 48,
      "caption": "A very clean and well decorated empty bathroom"
    } 
  ]
}
```
