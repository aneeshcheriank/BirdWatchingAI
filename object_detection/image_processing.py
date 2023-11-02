import cv2

SIZE = (300, 300)


def open_image(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, SIZE)
    return image
