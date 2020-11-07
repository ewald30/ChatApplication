import socket
import sys
from threading import Thread

#   Set the ip to whatever your ip is
IP = "127.0.0.1"
PORT = 6969
my_username = input("Username: ")

#   Create a TCP socket to communicate with the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Connect to the server through that socket
client_socket.connect((IP, PORT))

#   Send the username to the server tp authenticate
client_socket.send(my_username.encode())

def send_data(sock):
    """
    Thread function to send data to server and other clients
    :param sock: the socket that we use to communicate with the server
    :return: None
    """
    while True:
        data = sys.stdin.readline()
        sock.send(data.encode())

def receive_data(sock):
    """
    Thread function used to receive data from the server
    :param sock: the socket that we use to communicate with the server
    :return: None
    """
    while True:
        data = sock.recv(200)
        print(data.decode(), end="", flush=True)


#   Create two threads, one for sending data and one for receiving data
#   In this way neither the input nor the recv call is blocking
Thread(target=send_data, args=(client_socket,)).start()
Thread(target=receive_data, args=(client_socket, )).start()

