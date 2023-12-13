import socket


def client(host: str, port: int) -> None:
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Подключаемся к серверу
        s.connect((host, port))
        message = input('Введите сообщение: ')
        # Отправляем данные серверу
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Получены данные: \"{data.decode('utf-8')}\"")


if __name__ == '__main__':
    client('127.0.0.1', 65432)