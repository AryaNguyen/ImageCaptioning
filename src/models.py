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
        self.adaptive_pool = nn.AdaptiveAvgPool2d((encoded_image_size, encoded_image_size))

        # fine tune
        self.fine_tune()

    def forward(self, images):
        out = self.resnet(images)
        out = self.adaptive_pool(out)
        out = out.permute((0, 2, 3, 1))
        return out

    def fine_tune(self, fine_tune=True):
        for p in self.resnet.parameters():
            p.required_grad = False

        for c in list(self.resnet.children()[5:]):
            for p in c.parameters():
                p.required_grad = fine_tune


class Attention(nn.Module):
    def __init__(self):
        super(Attention, self).__init__()

    def forward(self, ):


class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()

