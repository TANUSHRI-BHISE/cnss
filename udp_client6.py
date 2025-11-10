# udp_client.py
import socket
import time

server_ip = '127.0.0.1'  # Change to server IP if on another PC
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send one file at a time
def send_file(filename):
    print(f"Sending file: {filename}")
    client_socket.sendto(filename.encode(), (server_ip, server_port))
    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            client_socket.sendto(data, (server_ip, server_port))
            data = f.read(1024)
            time.sleep(0.001)  # small delay to avoid flooding
    client_socket.sendto(b"END", (server_ip, server_port))
    print(f"File '{filename}' sent successfully!\n")

# Example files to send
files = ["sample.txt", "music.mp3", "video.mp4", "script.py"]

for file in files:
    send_file(file)

client_socket.close()
