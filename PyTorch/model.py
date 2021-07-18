import torch.nn as nn
import torch

def weights_init_normal(m):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        torch.nn.init.normal_(m.weight.data, 0.0, 0.02)
        if hasattr(m, "bias") and m.bias is not None:
            torch.nn.init.constant_(m.bias.data, 0.0)
    elif classname.find("BatchNorm2d") != -1:
        torch.nn.init.normal_(m.weight.data, 1.0, 0.02)
        torch.nn.init.constant_(m.bias.data, 0.0)


class ResidualBlock(nn.Module):
    def __init__(self, in_features):
        super().__init__()
        # print(in_features)

        self.block = nn.Sequential(
            nn.ReflectionPad2d(1),
            nn.Conv2d(in_features, in_features, 3),
            nn.InstanceNorm2d(in_features),
            nn.LeakyReLU(inplace=True),
            nn.ReflectionPad2d(2),
            nn.Conv2d(in_features, in_features, 3),
            nn.InstanceNorm2d(in_features),
            nn.Conv2d(in_features, in_features, 3)
        )

    def forward(self, x):
        out = self.block(x)
        return x + out


class Generator_Resnet(nn.Module):
    def __init__(self, in_shape, n_res_blocks=5):
        super(Generator_Resnet, self).__init__()
        channels = in_shape[0]
        n_blocks = n_res_blocks

        out_features = 64

        model = [
            nn.ReflectionPad2d(channels),
            nn.Conv2d(channels, out_features, 7),
            nn.InstanceNorm2d(out_features),
            nn.LeakyReLU(inplace=True)
        ]
        in_features = out_features

        # Downscaling
        for _ in range(2):
            out_features *= 2
            model += [
                nn.Conv2d(in_features, out_features, 3, stride=2, padding=1),
                nn.InstanceNorm2d(out_features),
                nn.LeakyReLU(inplace=True)
            ]
            in_features = out_features

        model += [ResidualBlock(in_features) for _ in range(n_blocks)]

        for _ in range(2):
            out_features //= 2
            model += [
                nn.Upsample(scale_factor=2),
                nn.Conv2d(in_features, out_features, 3, stride=1, padding=1),
                nn.InstanceNorm2d(out_features),
                nn.ReLU(inplace=True),
            ]
            in_features = out_features

            # Output layer
        # print(out_features)
        model += [nn.ReflectionPad2d(channels), nn.Conv2d(out_features, channels, 7), nn.Tanh()]

        self.model = nn.Sequential(*model)

    def forward(self, x):
        return self.model(x)


# Discriminator
class Discriminator(nn.Module):
    def __init__(self, input_shape):
        super(Discriminator, self).__init__()
        channels, height, width = input_shape

        self.output_shape = (1, height // 2**5, width // 2**5)

        def discriminator_block(in_, out_, normalize=True):
            layers = [nn.Conv2d(in_, out_, 4, stride=2, padding=1)]
            if normalize:
                layers.append(nn.InstanceNorm2d(out_))
            layers.append(nn.LeakyReLU(0.2, inplace=True))
            return layers

        model = [
            *discriminator_block(channels, 64, normalize=False),
            *discriminator_block(64, 128),
            *discriminator_block(128, 256),
            *discriminator_block(256, 512),
            nn.ZeroPad2d((1, 0, 1, 0)),
            nn.Conv2d(512, 1, 4, padding=1)
        ]
        self.model = nn.Sequential(*model)

    def forward(self, img):
        return self.model(img)