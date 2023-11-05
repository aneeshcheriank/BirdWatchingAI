import os
from torchvision.transforms import transforms
import cv2
import glob

EXTENSIONS = ('jpg', 'jpeg')
SELECTED_CLS = 15
BOX_COLOR = (255, 0, 0)
BOX_THICKNESS = 2
CHANNEL = 3
HEIGHT = 300
WIDTH = 300


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
    return tensor.float().view(-1, CHANNEL, HEIGHT, WIDTH)


def process_bbox(results_per_object, image_shape):
    box, item, confidence = results_per_object
    h, w = image_shape
    box = filter_class(box, item, SELECTED_CLS)

    if (box is None) | (len(box) == 0):
        return None

    box = box * [w, h, w, h]
    return box


def display_images_with_box(image, bboxs):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    for box in bboxs:
        x1, y1, x2, y2 = map(int, box)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color=BOX_COLOR, thickness=BOX_THICKNESS)

    cv2.imshow('image', image)
    cv2.waitKey()


def display_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('image', image)
    cv2.waitKey()


def list_images(folder, extension='jpg'):
    lst = glob.glob(f'{folder}/*.{extension}')
    return lst


def clear_folder(folder):
    files = glob.glob(f'{folder}/*.*')
    for file in files:
        os.remove(file)


def create_folder(folder):
    if os.path.exists(folder):
        clear_folder(folder)
        return None
    os.makedirs(folder, exist_ok=True)


def filter_class(box_array, cls_array, selected_cls=SELECTED_CLS):
    return box_array[cls_array == selected_cls]
