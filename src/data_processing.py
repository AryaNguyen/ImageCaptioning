"""================================================

    * Author: Arya Nguyen
    * Description: Model

================================================"""
import json
from tqdm import tqdm

from utils import *


def load_json(file, split, save_path):
    with open(file, "r") as j:
        data = json.load(j)

    images = data["images"]  # list of dict
    annotations = data["annotations"]  # list of dict

    captions = {"images": []}

    # Search captions for image
    for image in tqdm(images):
        image_caption = {
            "filename": image["file_name"],
            "id": image["id"],
            "split": split,
            "captions_id": [],
            "captions": []
        }

        for annotation in annotations:
            # case: matched image_id
            if annotation["image_id"] == image["id"]:
                image_caption["captions_id"].append(annotation["id"])
                caption = {
                    "tokens": tokenize(annotation["caption"]),
                    "raw": annotation["caption"].lower(),
                    "id": annotation["id"]
                }
                image_caption["captions"].append(caption)
        captions["images"].append(image_caption)

    with open(save_path, "w") as s:
        json.dump(captions, s)


if __name__ == "__main__":
    json_file = r"C:\Users\quynh\Desktop\GitHub\ImageCaptioning_LSTM\data\annotations\captions_train2014.json"
    save_path = r"C:\Users\quynh\Desktop\GitHub\ImageCaptioning\data\coco_captions_train2014.json"
    load_json(json_file, "train", save_path)


