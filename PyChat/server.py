import socket
import sys
from multiprocessing import Process

def main():
    # receive packets from users
    data, (addr, port) = server.recvfrom(4096)
    print(f"[*] packet from {addr}:{port} :: {data.decode()}")

    if data.decode() == "<data_request>":
        server.sendto(send_log(), (addr, port))

    #checks if command is send from privilaged user, not good security...
    elif data.decode() == f"{server_admin}: ?shutdown" and addr == server_ip:
        server.sendto(b'[*] Closing server\n[*] Disconnecting...', (addr, port))
        server.close()
        sys.exit()

    elif data.decode() == f"{server_admin}: ?clear" and addr == server_ip:
        with open('chat_log.txt', 'w') as file:
            file.write("<===Chat===>\n")
            server.sendto(b'[*] Chat log cleared', (addr, port))
 
    else:
        # append log and send text back
        if data.decode() != "<data_request>":
            log_append(data.decode())

        server.sendto(send_log(), (addr, port))

def log_append(text):
    with open('chat_log.txt', 'a') as file:
        file.writelines(f"{text}\n")

def send_log():
    with open('chat_log.txt', 'r') as chat:
        return chat.read().encode()
        

if __name__ == '__main__':

    print("<==========CHAT APP SEVER==========>\n")

    server_ip = "0.0.0.0" # set server IP
    server_port = 9998
    server_admin = "admin" # username privilaged to close server (line 21)

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((server_ip, server_port))
    print(f"[*] server on {server_ip}:{server_port}")

    while 1:
        main()
