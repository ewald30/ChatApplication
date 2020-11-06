import socket
import select

IP = "192.168.100.5"
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

    # Wait for user to input a message
    message = input(f'    {my_username} > ')

    # If message is not empty - send it
    if message:
        message = message + "\n"
        client_socket.send(message.encode())

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:
            message = client_socket.recv(100)

            # Print message
            print(message.decode(),"\n")

    except IOError as e:
        # We just did not receive anything
        continue

