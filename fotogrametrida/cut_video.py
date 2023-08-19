import cv2
import datetime

video_path = r"D:\manue\Documents\MATE\fotogrametrida\video\tree.mp4"

capture = cv2.VideoCapture(video_path)
frame_rate = capture.get(cv2.CAP_PROP_FPS)
interval = int(frame_rate) * 2  # Capturar un fotograma cada 2 segundos

frame_count = 0

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("No ret")
        break
    
    if frame_count % interval == 0:
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d_%H-%M-%S")
        print(formatted_date)
        filename = f'captura_{str(formatted_date)}.jpg'
        print('captura guardada')
        cv2.imwrite(filename, frame)

    frame_count += 1

capture.release()
cv2.destroyAllWindows()
