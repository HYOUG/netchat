#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

import socket
from datetime import datetime
from os import system
from select import select
from time import time
from class.Message import Message
from class.User import User


class SocketServer:
    
    """Socket Server class"""
    
    def __init__(self, host: str = "127.0.0.1", port: int = 9999, max_users: int = 5,
                 buff_size: int = 4096, encoding: str = "utf-8", encoding_errors: str = "replace",
                 socket_opt: list = None) -> None:
        
        """Socket server's builder"""
        
        # attributes from arguments
        self.host = host
        self.port = port
        self.max_users = max_users
        self.buff_size = buff_size
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.socket_opt = socket_opt
        
        # attributes from __init__
        self.socket = None
        self.clients = []
        self.client_num = 0
        self.isopened = False
        self.clients_chan = []
        self.inputs = []
        self.outputs = []
        self.exceptions = []
        self.notifications = {}
        self.color_code = {}
        
        
    def log(self, log_msg):
        if self.log:
            print(log_msg)       
        
        
    def redirect(self, msg: dict) -> None:
        """Redirect the given message to the clients"""
        msg_author_id = int(msg["author_id"])
        msg_author = self.clients[msg_author_id]["username"]
        msg_content = msg["content"].split(":")[1]
        msg = f"MSG:{msg_author}:{msg_author_id}:{msg_content}".encode()
        
        for client in self.clients:
            #if client["id"] != msg["author"]:
            try:
                client["connection"].sendall(msg)
                print(f"[i] Message sent to {client['id']}")
            except ConnectionResetError:
                print("Unreacheable target")
        
        
    def listen(self, client_num: int) -> None:
        """Listen thread that listen to the given client"""
        print(f"[i] The socket server is now listening to {':'.join(self.clients[client_num]['address'])}")  
        while True:
            #if self.clients[client_num]["listened"]:
            connection = self.clients[client_num]["connection"]
            data = connection.recv(self.buff_size)

            msg = {"content": data.decode(), "author_id": client_num, "timestamp": time()}
            
            if msg["content"].startswith("MSG"):
                self.redirect(msg)
            elif msg["content"].startswith("USERNAME"):
                self.clients[client_num]["username"] = msg["content"].split(":")[1]
            elif msg["content"].startswith("KILL"):
                self.kill()
            else:
                raise Exception("Unexpected header")
        
        
    def run(self) -> None:
        """Run the socket server"""
        with socket.socket() as server:
            server.bind((self.host, self.port))
            server.setblocking(0)
            server.listen(self.max_users)
            
            self.socket = server
            self.inputs.append(self.socket)
            self.isopened = True
            
            print(f"[i] The socket server is now running")
            print(f"[i] Settings : {self.host}:{self.port}")
            print(f"[i] The socket server is now open")
            
            readables, _, _ = select(self.inputs, self.outputs, self.inputs)
            
            for readable in readables:
                if readable is self.socket:
                    (clientsocket, address) = server.accept()
                    self.inputs(clientsocket)
                else:
                    data = readable.recv(self.buff_size)
                    if data:
                        msg = Message(string_msg=data.decode(encoding=self.encoding, errors=self.encoding_errors))
                        print(msg)
                    else:
                        self.inputs.remove(readable)
                        readable.close()
                    
            
            
            # while True:
            #     if self.isopened:
            #         server.listen(self.max_users)
            #         (clientsocket, address) = server.accept()
            #         print(f"[i] {address[0]}:{address[1]} joined the server")
            #         client_obj = {"connection": clientsocket, "address": address, "id": self.client_num}
            #         self.clients.append(client_obj)
            #         client_thread = Thread(target=self.listen, args=[self.client_num])
            #         client_thread.start()
            #         self.clients_chan.append(client_thread)
            #         self.client_num += 1
            #     else:
            #         print("[i] The socket server is now closed")
            #         break
            

    def kill(self) -> None:
        """Shutdown the socket server"""
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print("[i] The socket server have been shutdown")


    def close(self) -> None:
        """Stop the login loop thread"""
        self.isopened = False
        print("[i] Login : False")
        
        
    
if __name__ == "__main__":
    system("cls")
    host = input("Enter the socket server HOST : ")
    port = input("Enter the socket server PORT : ")  
    server = SocketServer(host=host, port=port)
    server.run()          
