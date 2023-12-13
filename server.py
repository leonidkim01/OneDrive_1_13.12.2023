import socket


def server(host: str, port: int) -> None:
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Привязываем сокет к IP-адресу и порту
        s.bind((host, port))
        # Слушаем входящие соединения
        s.listen()

        print('Сервер запущен и ожидает подключений...')

        # Принимаем входящее соединение
        client_socket, client_address = s.accept()
        with client_socket:
            print(f"Подключение установлено с {client_address}")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # Получаем данные от клиента
                print(f"Получены данные: \"{data.decode('utf-8')}\"")

                client_socket.sendall(f"Вы отправили: \"{data.decode('utf-8')}\"".encode())


if __name__ == '__main__':
    server('127.0.0.1', 65432)
