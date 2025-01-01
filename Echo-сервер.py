import socket

def start_echo_server():
    # Створення сокету
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Прив'язка до порту
    server_socket.listen(5)  # Максимальна кількість клієнтів, які можуть підключитися одночасно

    print("Сервер запущений на порту 12345...")

    while True:
        # Очікуємо на підключення клієнта
        client_socket, client_address = server_socket.accept()
        print(f"Підключено до {client_address}")

        try:
            # Отримуємо дані від клієнта
            data = client_socket.recv(1024)
            if data:
                print(f"Отримано від клієнта: {data.decode()}")
                # Відправляємо назад отримані дані
                client_socket.sendall(data)
        except Exception as e:
            print(f"Помилка: {e}")
        finally:
            # Закриваємо з'єднання з клієнтом
            client_socket.close()

if __name__ == "__main__":
    start_echo_server()
