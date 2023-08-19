import cv2
import time


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo capturar el fotograma.")
            break

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"captura_{timestamp}.png"
        cv2.imwrite(filename, frame)
        print(f"Captura guardada como {filename}")


        time.sleep(2)

except KeyboardInterrupt:
    print("Captura detenida por el usuario.")

cap.release()
