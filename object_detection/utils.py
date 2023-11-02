import os
from torchvision.transforms import transforms


def url_check(path):
    """
    :param path: image path
    :return: None if the path doesn't exist else the path
    """
    if os.path.exists(path):
        return path
    print('{url} does not exist')
    return None


def transform_to_tensor(img):
    tensor = transforms.ToTensor()(img)
    return tensor.float().view(-1, 3, 300, 300)
