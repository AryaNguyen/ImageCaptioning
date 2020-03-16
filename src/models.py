"""================================================

    * Author: Arya Nguyen
    * Description: Model

================================================"""
import torch
import torch.nn as nn
import torchvision


class Encoder(nn.Module):
    def __init__(self, encoded_image_size):
        super(Encoder, self).__init__()

        # pretrained resnet
        resnet = torchvision.models.resnet152(pretrained=True)

        # remove the last two layers of the resnet model
        modules = resnet.children()[:-2]
        self.resnet = nn.Sequential(modules)

        # Resize image to fixed size


        # fine tune

    def forward(self, images):
        pass


class Attention(nn.Module):
    def __init__(self):
        super(Attention, self).__init__()

    def forward(self, ):


class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()

