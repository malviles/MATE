import cv2
import time

video_path = 'ruta_del_video.mp4'
output_path = 'ruta_de_salida/'

cap = cv2.VideoCapture(video_path)
frame_rate = cap.get(cv2.CAP_PROP_FPS)
interval = int(frame_rate) * 2  # Capturar un fotograma cada 2 segundos

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count % interval == 0:
        timestamp = time.time()
        output_filename = f'{output_path}captura_{int(timestamp)}.jpg'
        cv2.imwrite(output_filename, frame)
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
