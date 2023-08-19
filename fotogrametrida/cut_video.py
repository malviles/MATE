import cv2
import datetime

def capture_frames(video_path):
    frame_count = 0
    capture = cv2.VideoCapture(video_path)
    frame_rate = capture.get(cv2.CAP_PROP_FPS)
    interval = int(frame_rate) * 2

    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            print("No ret")
            break

        if frame_count % interval == 0:
            now = datetime.datetime.now()
            formatted_date = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f'captura_{str(formatted_date)}.jpg'
            print('captura guardada: ', filename)
            cv2.imwrite(filename, frame)

        frame_count += 1

    capture.release()
    cv2.destroyAllWindows()

video_path = r"D:\manue\Documents\MATE\fotogrametrida\video\tree.mp4"
capture_frames(video_path)