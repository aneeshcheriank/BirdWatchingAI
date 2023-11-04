import cv2


def convert_video_to_frames(video_file, out_folder, n_frames=20):
    cap = cv2.VideoCapture(video_file)
    i = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is False:
            break
        if (i % n_frames) == 0:
            cv2.imwrite(f'{out_folder}/frame{i}.jpg', frame)
        i += 1
    else:
        print('video is not captured')
    cap.release()
    cv2.destroyAllWindows()
