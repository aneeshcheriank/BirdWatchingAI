from object_detection import image_processing as ip
from object_detection import utils as u, model


def process_image(url):
    if u.url_check(url) is not None:
        image = ip.open_image(url)
        tensor = u.transform_to_tensor(image)
        detection = model.detect_objects(tensor)

        return detection, image
    return None
