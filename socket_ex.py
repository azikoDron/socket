import socket
#   from bs4 import BeautifulSoup
import soup as sup
#   import lxml

content = 'hello'

def run():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = adress family default IPV4\\ AF_INET6 = IPV6
    server_socket.bind(('localhost', 5002))
    server_socket.listen()

    while True:
        soup = sup.BeautifulSoup(content, 'lxml')

        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)
        client_socket.sendall(soup.encode())
        client_socket.close()


if __name__ == '__main__':
    run()
