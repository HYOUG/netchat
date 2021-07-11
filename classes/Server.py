import socket
import curses
from threading import Thread
from classes.Message import Message
from classes.User import User
from functions.utils import *
from json import load, dump
from os import system


class Server:
    
    def __init__(self, host:str = "127.0.0.1", port:int = 9999, max_users:int = 5, buff_size:int = 4096,
                 log_enabled:bool = True, encoding:str = "utf-8", encoding_errors:str = "replace",
                 socket_opt:list = [], width:int = 80, height:int = 30) -> None:
        
        # attributes from arguments
        self.host = host
        self.port = port
        self.max_users = max_users
        self.buff_size = buff_size
        self.log_enabled = log_enabled
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.socket_opt = socket_opt
        self.width = width
        self.height = height
        
        # attributes from initialization
        self.socket = None
        self.clients = []
        self.client_num = 0
        self.isopened = False
        self.clients_chan = []
        self.inputs = []
        self.outputs = []
        self.settings = load(open("./settings/server.json", "r").read())
        self.exceptions = []
        self.notifications = {}
        self.color_code = {}
        
        self.stdscr = curses.initscr()
        curses.start_color()
        self.output_border = curses.newwin(self.height, self.width, 0, 0)
        self.output_field = curses.newwin(self.height - 2, self.width - 2, 1, 1)
        self.output_border.box()
        self.output_border.addstr(0, 2, "NetChat Server")
        
        
    def log(self, txt:str) -> None:
        self.outputs.append(txt)
        self.output_field.clear()
        self.output_field.addstr("\n".join(self.outputs))
        self.output_field.refresh()
        
        
    def redirect(self, msg:Message) -> None:
        """Redirect the given message to the clients"""
        for client in self.clients:
            try:
                client["connection"].sendall(msg.encoded())
                self.log(f"[>] Message sent to {client['id']}")
            except ConnectionResetError:
                self.log("[X] Unreacheable target")
        
        
    def listen(self, client_num:int) -> None:
        """Listen thread that listen to the given client"""
        self.log(f"[i] The socket server is now listening to {client_num}")
        connection = self.clients[client_num]["connection"]
        
        while True:
            
            data = connection.recv(self.buff_size)
            msg = Message()
            msg.parse(data.decode())
            
            if msg.header == "USERNAME":
                self.clients[client_num]["username"] = msg.content
            elif msg.header == "ENCODING":
                pass
            elif msg.header == "ENCODING_ERRORS":
                pass
            elif msg.header == "MSG":
                self.redirect(msg)
            elif msg.header == "DM":
                pass
            elif msg.header == "USERS":
                pass
            elif msg.header == "DUMP":
                pass
            elif msg.header == "KICK":
                pass
            elif msg.header == "BAN":
                pass
            elif msg.header == "QUIT":
                pass
            elif msg.header == "KILL":
                self.kill()
            else:
                raise Exception(f"[X] Unexpected header : {msg.header}")
        
        
    def run(self) -> None:
        """Run the socket server"""
        with socket.socket() as server:
            server.bind((self.host, self.port))
            server.listen(self.max_users)
            
            self.socket = server
            self.isopened = True
            
            self.log(f"[i] The socket server is now running an opened")
            self.log(f"[i] Adress : {self.host}:{self.port}")
            
            while True:
                if self.isopened:
                    server.listen(self.max_users)
                    (clientsocket, address) = server.accept()
                    
                    self.log(f"[+] {address[0]}:{address[1]} joined the server")
                    client_obj = {"connection": clientsocket, "address": address, "id": self.client_num}
                    self.clients.append(client_obj)
                    listen_thread = Thread(target=self.listen, args=[self.client_num])
                    listen_thread.start()
                    self.client_num += 1
                else:
                    self.log("[i] The socket server is now closed")
                    break
                
                
    def show(self) -> None:
        """Show the NetChat console"""
        def show_gui(stdscr) -> None:
            self.output_border.refresh()
            pass         
                
        system(f"mode {self.width}, {self.height}")
        curses.wrapper(show_gui)
            

    def kill(self) -> None:
        """Shutdown the socket server"""
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


    def close(self) -> None:
        """Stop the login loop thread"""
        self.isopened = False