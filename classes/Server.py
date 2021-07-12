import socket
import curses
from threading import Thread
from os import system
from classes.Message import Message
from functions.utils import *


class Server:
    """
    NetChat Server.
    
    Basic Usage::
    >>> import netchat
    >>> s = Server()
    >>> s.show()
    >>> s.run()
    """
    
    def __init__(self, host:str = "127.0.0.1", port:int = 9999, max_users:int = 5, buff_size:int = 4096,
                 log:bool = True) -> None:
        """
        [summary]

        Parameters
        ----------
        host : str, optional
            [description], by default "127.0.0.1"
        port : int, optional
            [description], by default 9999
        max_users : int, optional
            [description], by default 5
        buff_size : int, optional
            [description], by default 4096
        log : bool, optional
            [description], by default True
        """
        
        # asserts
        assert isinstance(host, str), f"Invalid 'host' data type : {type(host)}. Expected a str."
        assert isinstance(port, int), f"Invalid 'port' data type : {type(port)}. Expected an int."
        assert isinstance(max_users, int), f"Invalid 'max_users' data type : {type(max_users)}. Expected an int."
        assert isinstance(buff_size, int), f"Invalid 'buff_size' data type : {type(buff_size)}. Expected an int."
        assert isinstance(log, bool), f"Invalid 'log' data type : {type(log)}. Expected a bool."
        
        # attributes from arguments
        self.host = host
        self.port = port
        self.max_users = max_users
        self.buff_size = buff_size
        self.log = log
        
        # attributes from initialization
        self.socket = None
        self.clients = []
        self.client_num = 0
        self.isopened = False
        self.outputs = []
        
        
    def display(self, txt:str) -> None:
        self.outputs.append(txt)
        self.output_field.clear()
        self.output_field.addstr("\n".join(self.outputs))
        self.output_field.refresh()
        
        
    def redirect(self, msg:Message) -> None:
        """Redirect the given message to the clients"""
        for client in self.clients:
            try:
                client["connection"].sendall(msg.encoded())
                self.display(f"[>] Message sent to {client['id']}")
            except ConnectionResetError:
                self.display("[X] Unreacheable target")
        
        
    def listen(self, client_num:int) -> None:
        """Listen thread that listen to the given client"""
        self.display(f"[i] The socket server is now listening to {client_num}")
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
            
            self.display(f"[i] The socket server is now running an opened")
            self.display(f"[i] Adress: {self.host}:{self.port}")
            
            while True:
                if self.isopened:
                    server.listen(self.max_users)
                    (clientsocket, address) = server.accept()
                    
                    self.display(f"[+] {address[0]}:{address[1]} joined the server")
                    client_obj = {"connection": clientsocket, "address": address, "id": self.client_num}
                    self.clients.append(client_obj)
                    listen_thread = Thread(target=self.listen, args=[self.client_num])
                    listen_thread.start()
                    self.client_num += 1
                else:
                    self.display("[i] The socket server is now closed")
                    break
                
                
    def show(self, width:int = 80, height:int = 30) -> None:
        """Show the NetChat console"""
        # asserts
        assert isinstance(width, int), f"Invalid 'width' data type : {type(width)}. Expected an int."
        assert isinstance(height, int), f"Invalid 'height' data type : {type(height)}. Expected an int."
        
        self.width = width
        self.height = height
        
        # curses settings
        self.stdscr = curses.initscr()
        self.output_border = curses.newwin(self.height, self.width, 0, 0)
        self.output_field = curses.newwin(self.height-2, self.width-2, 1, 1)
        self.output_border.box()
        self.output_border.addstr(0, 2, "NetChat Server")
        
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
        
    
    def __repr__(self) -> str:
        """Reprezentation of the NetChat Server object"""
        return f"<NetChat Server: {self.host}:{self.port}>"
    
    
    def __str__(self) -> str:
        """String appearance of the NetChat Server object"""
        return f"<NetChat Server: {self.host}:{self.port}>"