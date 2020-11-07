import socket
import sys
import select

IP = "127.0.0.1"
PORT = 6969
my_username = input("Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
client_socket.send(my_username.encode())


while True:
    readers, _, _ = select.select([client_socket, sys.stdin], [], [])
    for reader in readers:
        if reader is client_socket:
            message = client_socket.recv(100)
            print(message.decode(), end="", flush=True)
        else:
            message = sys.stdin.readline()
            client_socket.send(message.encode())