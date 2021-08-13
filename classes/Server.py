import curses
import socket
from datetime import datetime
from os import system
from threading import Thread
from functions.utils import *
from classes.Message import Message
from classes.User import User


class Server:
    """
    NetChat Server.
    
    Basic Usage::
    >>> import netchat
    >>> s = Server()
    >>> s.show()
    >>> s.run()
    """
    
    def __init__(self, host:str = "127.0.0.1", port:int = 9999, max_users:int = 5,
                 buff_size:int = 4096, logging:bool = False) -> None:
        """
        Generate a NetChat Server.

        Parameters
        ----------
        host : str, optional
            IP address used by the NetChat (socket) server, by default "127.0.0.1"
        port : int, optional
            Port used by the NetChat (socket) server, by default 9999
        max_users : int, optional
            Maximum amount of users connected to the server, by default 5
        buff_size : int, optional
            NetChat serer buffer size, by default 4096
        logging : bool, optional
            enable or disable the logging mode, displaying all the events and processes, by default False
        """
        
        # asserts
        assert isinstance(host, str), f"Invalid 'host' data type : {type(host)}. Expected a str."
        assert isinstance(port, int), f"Invalid 'port' data type : {type(port)}. Expected an int."
        assert isinstance(max_users, int), f"Invalid 'max_users' data type : {type(max_users)}. Expected an int."
        assert isinstance(buff_size, int), f"Invalid 'buff_size' data type : {type(buff_size)}. Expected an int."
        assert isinstance(logging, bool), f"Invalid 'logging' data type : {type(logging)}. Expected a bool."
        
        # attributes from arguments
        self.host = host
        self.port = port
        self.max_users = max_users
        self.buff_size = buff_size
        self.logging = logging
        
        # attributes from initialization
        self.users = []
        self.user_num = 0
        self.isopened = False
        self.outputs = []
        
        
    def log(self, category:str, event_text:str) -> None:
        """
        [summary]

        Parameters
        ----------
        category : str
            [description]
        event_text : str
            [description]
        """
        if self.logging:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("./debug/server.txt", "w+") as f:
                f.write(f"[{date}] ({category.upper()}) : {event_text}")
        
        
    def display(self, text:str) -> None:
        self.outputs.append(text)
        while sum([len(item) for item in self.outputs]) > ((self.height-2) * (self.width-2)):
            print(sum([len(item) for item in self.outputs]))
            print(((self.height-2) * (self.width-2)))
            self.outputs = self.outputs[1:]
            # self.log("info", f"outputs len : {sum([len(item) for item in self.outputs])}")
            # self.log("info", f"output field surface : {(self.height-2 * self.width-2)}")
            # exit()
        self.output_field.clear()
        self.output_field.addstr("\n".join(self.outputs))
        self.output_field.refresh()
        
        
    def redirect(self, msg:Message) -> None:
        """
        Redirect the given message to the clients.

        Parameters
        ----------
        msg : Message
            [description]
        """
        for user in self.users:
            try:
                self.display(f"[i] trying to redirect to #{user.uuid}")
                user.socket.sendall(msg.encoded())
                self.display(f"[>] Message sent to #{user.uuid}") #TODO
            except ConnectionResetError:
                self.display("[X] Unreacheable target")
        
        
    def listen(self, client_num:int) -> None:
        """
        Listen thread that listen to the given client.

        Parameters
        ----------
        client_num : int
            [description]

        Raises
        ------
        Exception
            Unexpected message header
        """
        
        self.display(f"[i] The socket server is now listening to #{client_num}.")    #TODO
        user_socket = self.users[client_num].socket
        
        while True:     
            self.display("'m in...")
            data = user_socket.recv(self.buff_size)
            self.display("data received")
            msg = Message()
            self.display("msg obj created")
            self.display(f"the data : {data.decode()}")
            msg.parse(data.decode())
            print(f"the message is : {msg}")
            
            if msg.header == "USERNAME":
                self.display("we got an username")
                self.users[client_num].username = msg.content
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
                self.display(f"[X] Unexpected header : {msg.header}.")
                #raise Exception(f"[X] Unexpected header : {msg.header}.")
        
        
    def run(self) -> None:
        """Run the socket server"""
        with socket.socket() as server:
            server.bind((self.host, self.port))
            server.listen(self.max_users)
            self.socket = server
            self.isopened = True
            self.display(f"[i] The socket server is now running an opened.")
            self.display(f"[i] Address: {self.host}:{self.port}.")
            while True:
                if self.isopened:
                    server.listen(self.max_users)
                    (clientsocket, address) = server.accept()     
                    self.display(f"[+] {address[0]}:{address[1]} joined the server.")
                    new_user = User(clientsocket, address, uuid=self.user_num)
                    self.users.append(new_user)
                    listen_thread = Thread(target=self.listen, args=[self.user_num])
                    listen_thread.start()
                    self.user_num += 1
                else:
                    self.display("[i] The socket server is now closed.")
                    break
                
                
    def resize(self, width:int = 80, height:int = 30) -> None:
        """
        Resize the NetChat console.

        Parameters
        ----------
        width : int, optional
            [description], by default 80
        height : int, optional
            [description], by default 30
        """
        
        # asserts
        assert isinstance(width, int), f"Invalid 'width' data type : {type(width)}. Expected an int."
        assert isinstance(height, int), f"Invalid 'height' data type : {type(height)}. Expected an int."
        
        system(f"mode {width}, {height}")
                
                
    def show(self, width:int = 80, height:int = 30) -> None:
        """
        Show the NetChat console.

        Parameters
        ----------
        width : int, optional
            [description], by default 80
        height : int, optional
            [description], by default 30
        """
        
        # asserts
        assert isinstance(width, int), f"Invalid 'width' data type : {type(width)}. Expected an int."
        assert isinstance(height, int), f"Invalid 'height' data type : {type(height)}. Expected an int."
        
        # attributes from arguments
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
                
        self.resize(width, height)
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
