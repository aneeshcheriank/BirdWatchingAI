import cv2

SIZE = (300, 300)


def open_image(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, SIZE)
    return image


def snip_objects(image, bboxs):
    if len(bboxs) == 0:
        return None

    objects = []
    for box in bboxs:
        x1, y1, x2, y2 = map(int, box)
        item = image[y1:y2, x1:x2]
        objects.append(item)

    return objects
