# udp_server.py
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))  # listen on all IPs, port 12345

print("UDP Server is ready to receive files...")

while True:
    # Receive filename
    filename, addr = server_socket.recvfrom(1024)
    filename = filename.decode()
    print(f"Receiving file: {filename} from {addr}")

    # Open file to write received data
    with open("received_" + filename, "wb") as f:
        while True:
            data, _ = server_socket.recvfrom(1024)
            if data == b"END":  # when client sends END, stop
                break
            f.write(data)

    print(f"File '{filename}' received successfully!\n")
