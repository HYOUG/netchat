#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

import socket
from time import time
from datetime import datetime
from os import system
from select import select
from sys import stdin
from rich import print
from class.Message import Message
from class.User import User


class SocketClient:
    
    """Socket Client class"""
    
    def __init__(self, username: str = "John Doe", log: bool = True, encoding: str = "utf-8",
                 encoding_errors: str = "replace", buff_size: int = 4096) -> None:
        
       """Socket client's builder"""
        
       # attributes from arguments
       self.username = username
       self.log = log
       self.encoding = encoding
       self.encoding_errors = encoding_errors
       self.buff_size = buff_size
       
       # attributes from __init__
       self.host = None
       self.port = None
       self.socket = None
       self.notifications = {}
       self.color_code = {}
       self.inputs = []
       self.outputs = []
       
       
    def log(self, log_msg) -> None:
        if self.log:
            print(log_msg)
       
       
    def input(self) -> None:                                                                       # SocketClient's input thread
        while True:
            msg = input("")
            if msg != "":
                self.socket.sendall(f"MSG:{msg}".encode())
         
            
    def output(self) -> None:                                                                      # SocketClient's output thread
        while True:
            data = self.socket.recv(self.buff_size)
            msg = Message(string_msg=data.decode())
            if msg.prefix == "MSG": 
                print(msg)
            
       
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
            
            
    def run(self):
        readable, _, _ = select()
    
    def disconnect(self):
        pass
            
            
            
            
if __name__ == "__main__":
    system("cls")
    username = input("Enter you username : ")
    host = input("Enter the socket server HOST : ")
    port = input("Enter the socket server PORT : ")  
    user = SocketClient(username=username)
    user.connect(host=host, port=port)
    