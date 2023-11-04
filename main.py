# This is a sample Python script.
# from object_detection import do_process as dp, utils as u, image_processing as ip
import os
from object_detection import video as v
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# image_path = '/home/aneesh/Pictures/camera/DSC_0010.JPG'
# image_path = '/home/aneesh/Downloads/bird images/image_1.jpeg'
# image_path = '/home/aneesh/Downloads/bird images/image_2.jpg'
working_folder = '/home/aneesh/Downloads/working folder'
input_folder = 'input'
output_folder = 'output'
file = 'test.mp4'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # out, image = dp.process_image(image_path)
    # box = u.process_bbox(out)
    # # u.display_images_with_box(image, box)
    # items = ip.snip_objects(image, box)
    # for img in items:
    #     u.display_image(img)
    file_path = os.path.join(working_folder, input_folder, file)
    output_path = os.path.join(working_folder, output_folder)

    v.convert_video_to_frames(file_path, output_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
