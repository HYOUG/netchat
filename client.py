#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

import socket
from threading import Thread
from datetime import datetime
from os import system


class SocketClient:
    
    def __init__(self, username: str = "John Doe", buff_size: int = 4096) -> None:                 # SocketClient's builder
       self.username = username
       self.buff_size = buff_size
       self.host = None
       self.port = None
       self.socket = None
       
       
    def input(self) -> None:                                                                       # SocketClient's input thread
        while True:
            msg = input("")
            if msg != "":
                self.socket.sendall(f"MSG:{msg}".encode())
         
            
    def output(self) -> None:                                                                      # SocketClient's output thread
        while True:
            data = self.socket.recv(self.buff_size)
            data = data.decode()
            data = data.split(":")
            
            msg_type = data[0]
            if msg_type == "MSG":
                msg_author = data[1]
                msg_author_id = data[2]
                msg_content = "".join(data[3:])
                print(f"{msg_author} | [#{msg_author_id}] : {msg_content}")
            
       
    def connect(self, host: str = "127.0.0.1", port: int = 9999, encoding: str = "utf-8",
                encoding_errors: str = "replace") -> None:
        """Connect the socket client to the given socket server"""
        self.host = host
        self.port = port
        with socket.socket() as server:
            self.socket = server
            server.connect((host, port))
            server.send(f"USERNAME:{self.username}".encode())
            print(f"[i] connected to {host}:{port}")
            print("[i] Press Ctrl + C to exit the program")
            
            input_loop = Thread(target=self.input)
            output_loop = Thread(target=self.output)
            
            input_loop.start()
            output_loop.start()
            
            while True:
                pass
            
            
if __name__ == "__main__":
    username = input("Enter you username : ")
    host = input("Enter the socket server HOST : ")
    port = input("Enter the socket server PORT : ")  
    user = SocketClient(username=username)
    user.connect(host=host, port=port)
    