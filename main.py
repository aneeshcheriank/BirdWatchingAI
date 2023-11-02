# This is a sample Python script.
from object_detection import do_process as dp
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

image_path = '/home/aneesh/Pictures/camera/DSC_0010.JPG'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    out = dp.process_image(image_path)
    print(out)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
