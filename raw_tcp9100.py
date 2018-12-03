#!/usr/bin/env python3

import socket
import threading
import sys
from datetime import datetime

class ServerThread(threading.Thread):
    def __init__(self, ip, port, open_socket, file_handle):
        self.ip = ip
        self.port = port
        self.socket = open_socket
        self.file_handle = file_handle
        print(f"[+] Initializing thread for {ip}:{port}")
        threading.Thread.__init__(self)
    
    def run(self):
        print(f"[+] Running thread for {self.ip}:{self.port}")

        # Block for 10 seconds before giving up
        self.socket.settimeout(10)
        
        try:
            data = self.socket.recv(4096)
            file_handle.write(data)

            while len(data) != 0:    
                data = self.socket.recv(4096)
                file_handle.write(data)
            
            print(f"[ ] No more data from {self.ip}:{self.port}")
        except socket.timeout:
            # Timeout on the data read
            print(f"[-] Timeout on connection from {self.ip}:{self.port}")
        
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        self.file_handle.close()

host = "0.0.0.0"
port = 9100

server_threads = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

while True:
    try:
        open_socket, (ip, port) = s.accept()
        time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{time_stamp}_{ip}_{port}.raw"
        file_handle = open(file_name, 'wb')
        print("[+] Writing to file " + file_name)
        server_thread = ServerThread(ip, port, open_socket, file_handle)
        server_thread.start()
        server_threads.append(server_thread)
    except KeyboardInterrupt:
        print("\n[*] Keyboard interrupt exiting ...")
        break

nr_of_threads_joined = 0

for st in server_threads:
    try:
        st.join(5)
        nr_of_threads_joined += 1
    except Exception as e:
        print(e)
        print("[-] Exception stopping server thread ")

print(f"Nr of threads joined: {nr_of_threads_joined}")
print(f"Nr of threads started: {len(server_threads)}")




    