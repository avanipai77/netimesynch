import socket
import time

HOST = "0.0.0.0"
PORT = 5005

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("Time server is running!")

while True:
    message, client_address = server_socket.recvfrom(1024)
    t2 = time.time()  # time server received the request
    t3 = time.time()  # time server is sending the reply

    reply = f"{t2},{t3}"
    server_socket.sendto(reply.encode(), client_address)
