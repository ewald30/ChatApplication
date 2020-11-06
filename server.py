import socket
import select


def send_all(message_to_send, sender):
    """
    Sends a given message to all the clients except the sender
    :param message_to_send: gotten message from the sender
    :param sender: the client that sent the message
    :return: None
    """
    #print("Clients: ",clients)

    for client in clients:
        if client is not sender:
            client.send(message_to_send.encode())


def receive_message(client_socket):
    try:
        return client_socket.recv(100)
    except:
        return False


#   Select the ip and the port desired
ip = "0.0.0.0"
port = 6969

#   Create a tcp socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Overcome the address already in use error
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#   Bind to the socket
server_socket.bind((ip, port))

#   Listen for a new connection
server_socket.listen()

#   Create a list to keep track of sockets
sockets = [server_socket]
clients = {}

#   Call select system call in order to get a read set

while True:
    read_sockets, _, _ = select.select(sockets, [], [])

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            #   If the notified socket is the server => new connection
            #   Create a client socket
            client_socket, _ = server_socket.accept()

            #   Get the username from the client
            username = client_socket.recv(15)
            print("    "+str(username.decode())+" connected.")
            #   Send a welcome message
            welcome_message = "Hello " + username.decode() + ", welcome to the chat!"
            client_socket.send(welcome_message.encode())

            #   Add the client socket to the read list
            sockets.append(client_socket)

            #   Add a  record of the new client
            clients[client_socket] = username
        else:
            #   Recv is blocking!!!!!
            message = receive_message(notified_socket)
            if message is False:
                sockets.remove(notified_socket)
                del clients[notified_socket]
                continue

            #   Get the username of the user that sent the message
            user = clients[notified_socket]

            #   Create a format for the message to be sent to all the other clients
            broadcast_message = "    <" + user.decode() + ">  " + message.decode()
            print(broadcast_message)
            send_all(broadcast_message, notified_socket)
