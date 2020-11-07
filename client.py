import socket
import sys
import select

IP = "127.0.0.1"
PORT = 6969
my_username = input("Username: ")

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
client_socket.send(my_username.encode())


while True:
    #   Add stdin as a potential reader
    readers, _, _ = select.select([client_socket, sys.stdin], [], [])

    #   Check if something is ready to be read in either stdin or in the socket
    for reader in readers:
        if reader is client_socket:
            #   If socket is ready then we read the data from the socket and print the message
            message = client_socket.recv(100)
            print(message.decode(), end="", flush=True)
        else:
            #   If the user has written something then send the message
            message = sys.stdin.readline()
            client_socket.send(message.encode())