# ChatApplication
Simple chat application with No GUI (Yet) using python and socket programming

This method works only on LAN!



Server:

It creates a tcp socket for every client that connects to the server. 
The socket is then added to the readers list that select module uses to iterate through and decide what gets updated when. 
If the server socket is updated it means we have a new connection. 
If a client socket gets updated it means we have a new message and we should send it to all the other chat members. 
  
  
  
Client:

It creates a tcp socket to communicate with the server. 
It uses 2 threads in order to send data and receive data at the same time. 
This way, when we receive data the "recv()" call is not blocked by "stdin.readline()" call, so the chat history is updated no matter the circumstances. 
  
  
  
  
  
How to use:
Note: you have to have Python 3.7 or above installated

(Linux/MacOS)
Start the server by executing: python3 server.py
Start a client by executing: python3 client.py

(Windows)
Start the server by executing: py server.py
Start a client by executing: py client.py

Set the username of your choice then start chatting!
