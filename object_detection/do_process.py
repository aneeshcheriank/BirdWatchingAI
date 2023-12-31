from object_detection import image_processing as ip
from object_detection import utils as u, model, video as v, image_processing as ip


def process_image(url):
    if u.url_check(url) is not None:
        image, image_actual = ip.open_image(url)
        tensor = u.transform_to_tensor(image)
        detection = model.detect_objects(tensor)

        return True, detection, image_actual
    return False, None, None


def detect_object_from_video(video_path, image_folder):
    u. create_folder(image_folder)
    v.convert_video_to_frames(video_path, image_folder)

    image_paths = u.list_images(image_folder, extension='jpg')

    objects_all_images = []
    for image_path in image_paths:
        is_detect, results_per_input, image = process_image(image_path)

        if is_detect:
            h, w, _ = image.shape
            box = u.process_bbox(results_per_input[0], (h, w))
            if box is not None:
                image_object = ip.snip_objects(image, box)
                objects_all_images.append(image_object)

    if len(objects_all_images) > 0:
        for objects_from_image in objects_all_images:
            if objects_from_image is None:
                continue

            for identified_object in objects_from_image:
                u.display_image(identified_object)
