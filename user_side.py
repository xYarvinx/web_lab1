import cv2
import mediapipe as mp
import socket

def send_signal():
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # IP-адрес и порт удаленного компьютера
    remote_ip = '192.168.0.4'  # Замените на IP-адрес вашего компьютера-получателя
    port = 1234  # Установите порт, который будете использовать

    try:
        client_socket.connect((remote_ip, port))
        client_socket.send(b'defeat')
        client_socket.close()

    except ConnectionRefusedError:
        print("Соединение не установлено!")


video_capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


while True:
    ret, frame = video_capture.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        results = hands.process(frame)

        num_hands = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                num_hands += 1

            if num_hands == 2:
                 send_signal()

        cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()

cv2.destroyAllWindows()







