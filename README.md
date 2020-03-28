# Image Captioning (CNN, LSTM) - Pytorch
This project implements [Show, Attend, and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/abs/1502.03044) paper using PyTorch (1.4.0) Python API. 
<br><br>
The model is tranined on MS-COCO dataset. The instruction on how to download and preprocess the data can be found [here](https://github.com/AryaNguyen/ImageCaptioning/blob/master/DATA_explain.md).
<br><br>
I'm a beginner in AI/ML. I want to explore the application of Computer Vision and Deep Learning, and I found Image Captioning is an interesting topic to start with. I haven't take any classes in AI, ML, or computer vision; therefore, I'll explain a lot of things that you might know for the purpose of learning.

## Encoder
```
import torch
import torchvision
import torch.nn as nn
```

```
class Encoder(nn.Module):
    def __init__(self, encoded_image_size=14):
        super(Encoder, self).__init__()
        
        # pretrained resnet-18 without the last 2 layers
        resnet = torchvision.models.resnet18(pretrained=True)
        layers = list(resnet.children())[:-2]
        self.resnet = nn.Sequential(*layers)

        # add layer to resize images to <encoded_image_size>
        self.adaptive_pool = nn.AdaptiveAvg2dPool((encoded_image_size, encoded_image_size))
        
        self.fine_tune()

    def forward(self, images)
        out = self.resnet(images)
        out = self.adaptive_pool(images)
        out = out.permute(0, 2, 3, 1)

    self.fine_tune(self, fine_tune=True):
        for p in self.resnet.paramteters:
            p.required_grad = False
        
        for c in list(self.resnet.childdren())[5:]:
            for p in c.parameters():
                p.required_grad = fine_tune

```

I'm using ResNet-18 model from [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385). By setting parameter ```pretrained=True```, it return a pretrained model that is previously trained on ImageNet dataset. 

```
>>> resnet
ResNet(
    (conv1): Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
    (bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (relu): ReLU(inplace=True)
    (maxpool): MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, ceil_mode=False)
    (layer1): Sequential(
        ...
    )
    (layer2): Sequential(
        ...
    )
    (layer3): Sequential(
        ...
    )
    (layer4): Sequential(
        ...
    )
    (avgpool): AdaptiveAvgPool2d(output_size=(1, 1))
    (fc): Linear(in_features=512, out_features=1000, bias=True)
)

```

The pretrained model consists of 18 layers in which the last 2 are 2D adaptive average pool layer with 1 x 1 output size and fully connected layer with 512 input features and 1000 output features. These layers are for classifying tasks, and we don't need them for this project.
<br><br>
By default, all of the parameters in the pretrained model's children have ```.required_grad = True``` that enables tracking the history and forming the backward graph. However, we don't want to compute gradient over model child 1 to 4 so we set  ```.required_grad = False```. This will reduce memory consumptions for computation and the training phase becomes much faster. 
<br><br>



## Attention

## Decoder

## References
- Deep Residual Learning for Image Recognition
- Show, Tell, Attend: Neural Image Caption Image with Visual Attention 
