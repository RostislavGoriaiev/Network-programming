import socket

def start_echo_client():
    # Створення сокету
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Підключення до сервера
        client_socket.connect(('localhost', 12345))

        # Відправка повідомлення на сервер
        message = input("Введіть повідомлення для сервера: ")
        client_socket.sendall(message.encode())

        # Отримуємо відповідь від сервера
        data = client_socket.recv(1024)
        print(f"Отримано від сервера: {data.decode()}")
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        # Закриваємо з'єднання
        client_socket.close()

if __name__ == "__main__":
    start_echo_client()
