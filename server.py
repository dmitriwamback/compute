import socket
import threading

servsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsocket.bind(('192.168.0.17', 8080))
servsocket.listen(5)


def multithread_client(client):
    while True:
        print('hi')
        buf = client.recv(1024)
        if len(buf) > 0:
            print(buf)


while True:

    print('waiting for connections...')

    connection, address = servsocket.accept()

    t = threading.Thread(target=multithread_client, args=(connection,))
    t.start()