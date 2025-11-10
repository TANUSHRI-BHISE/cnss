import socket

# Server IP and port
host = '127.0.0.1'  # For testing on same PC, or server's LAN IP
port = 12345

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Server listening...")

# Wait for client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive Hello message
msg = conn.recv(1024).decode('ascii')
print("Client says:", msg)

# Send reply
conn.send("Hello from Server!".encode('ascii'))

# Receive filename
filename = conn.recv(1024).decode('ascii')

# Receive file data
with open("received_" + filename, "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print(f"File '{filename}' received successfully.")
conn.close()
