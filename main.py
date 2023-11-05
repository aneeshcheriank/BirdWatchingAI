# This is a sample Python script.
import os

from object_detection import do_process as dp
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

working_folder = '/home/aneesh/Downloads/working folder'
input_folder = 'input'
output_folder = 'output'
file = 'test2.mp4'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file_path = os.path.join(working_folder, input_folder, file)
    output_path = os.path.join(working_folder, output_folder)

    dp.detect_object_from_video(file_path, output_path)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
