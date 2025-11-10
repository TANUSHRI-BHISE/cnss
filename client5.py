import socket

# Server IP and port
host = '127.0.0.1'  # Server IP
port = 12345

# Create socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Send Hello message
client_socket.send("Hello from Client!".encode('ascii'))

# Receive server reply
response = client_socket.recv(1024).decode('ascii')
print("Server says:", response)

# Send file
filename = "sample.txt"
client_socket.send(filename.encode('ascii'))  # send filename first

with open(filename, "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

client_socket.close()
print(f"File '{filename}' sent successfully.")
