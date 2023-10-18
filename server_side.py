import socket
import cv2


def display_image():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    local_ip = '192.168.0.4'
    port = 1234

    try:

        server_socket.bind((local_ip, port))

        server_socket.listen(1)
        print("Ожидание подключения клиента...")
        client_socket, address = server_socket.accept()
        print("Подключен клиент", address)

        while TRUE:
            data = client_socket.recv(1024)
            if data == b'defeat':
                print("Сигнал получен!")
                image = cv2.imread('soyjack.jpeg')

                cv2.namedWindow('Изображение', cv2.WINDOW_FULLSCREEN)
                cv2.imshow('Изображение', image)
                cv2.waitKey(0)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        client_socket.close()
        server_socket.close()

    except OSError as e:
        print("Ошибка:", e)


display_image()
