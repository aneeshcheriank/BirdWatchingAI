import os
from torchvision.transforms import transforms
import cv2
import glob

EXTENSIONS = ('jpg', 'jpeg')


def check_image(path):
    """
    :param path: file path
    :return: Ture if the file is an image file
    """
    extension = path.split('.')[-1]
    if extension.lower() in EXTENSIONS:
        return True
    return False


def url_check(path):
    """
    :param path: image path
    :return: None if the path doesn't exist else the path
    """
    if os.path.exists(path):
        if check_image(path) is True:
            return path
        else:
            print('the file is not a jpeg or jpg file')
    print('{url} does not exist')
    return None


def transform_to_tensor(img):
    tensor = transforms.ToTensor()(img)
    return tensor.float().view(-1, 3, 300, 300)


def process_bbox(results_per_input, ix=0):
    boxes, classes, confidence = results_per_input[ix]
    box = [val*300 for val in boxes]
    return box


def display_images_with_box(image, bboxs):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    for box in bboxs:
        x1, y1, x2, y2 = map(int, box)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color=(255, 0, 0), thickness=2)

    cv2.imshow('image', image)
    cv2.waitKey()


def display_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('image', image)
    cv2.waitKey()


def list_videos(folder, extension='avi'):
    lst = glob.glob(f'{folder}/*.{extension}')
    return lst
