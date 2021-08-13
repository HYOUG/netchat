import curses
import socket
from datetime import datetime
from os import system
from string import printable
from threading import Thread
from functions.utils import *
from classes.Message import Message


class Client:
    """
    NetChat Client.
    
    Basic Usage::
    >>> import netchat
    >>> c = netchat.Client()
    >>> c.show()
    >>> c.connect()
    """
    
    def __init__(self, username:str, encoding:str = "utf-8", encoding_errors:str = "replace",
                 buff_size:int = 4096, logging:bool = False) -> None:
        """
        Generate a Client object.

        Parameters
        ----------
        username : str
            user's name used in the chat channel
        encoding : str, optional
            encoding type used in the data sent/received, by default "utf-8"
        encoding_errors : str, optional
            error handling method used in the data sent/received, by default "replace"
        buff_size : int, optional
            buffer size used when data is received, by default 4096
        logging : bool, optional
            enable or disable the logging mode, displaying all the events and processes, by default False
        """
        
        # asserts
        assert isinstance(username, str), f"Invalid 'username' data type : {type(username)}. Expected a str."
        assert isinstance(encoding, str), f"Invalid 'encoding' data type : {type(encoding)}. Expected a str."
        assert isinstance(encoding_errors, str), f"Invalid 'enconding_errors' data type : {type(encoding_errors)}. Expected a str."
        assert isinstance(buff_size, int), f"Invalid 'buff_size' data type : {type(buff_size)}. Expected an int."
        assert isinstance(logging, bool), f"Invalid 'logging' data type : {type(logging)}. Expected a bool."
        
        # attributes from arguments
        self.username = username
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.buff_size = buff_size
        self.logging = logging
        
        # attributes from initialization
        self.user_input = ""
        self.outputs = []
        self.KEYS_ENTER = [curses.KEY_ENTER, 10, 13]
        self.KEYS_BACKSPACE = [curses.KEY_BACKSPACE, 8, 127]
        self.KEY_ESCAPE = 27
        self.KEYS_UTILITY = self.KEYS_ENTER + self.KEYS_BACKSPACE + [self.KEY_ESCAPE]
        self.KEYS_PRINTABLE = [ord(item) for item in printable if item not in self.KEYS_UTILITY]
        
    
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
            with open("./debug/client.txt", "w+") as f:
                f.write(f"[{date}] ({category}) : {event_text}")
        
        
    def display(self, text:str) -> None:
        """
        [summary]

        Parameters
        ----------
        text : str
            [description]
        """
        
        self.outputs.append(text)
        self.output_field.clear()
        self.output_field.addstr("\n".join(self.outputs))
        self.output_field.refresh()
        
        
    def run(self) -> None:
        """
        [summary]
        """
        
        pass
        
        
    def output_method(self) -> None:
        """
        [summary]
        """
        
        while True:
            data = self.socket.recv(self.buff_size)
            msg = Message()
            msg.parse(data.decode())
            if msg.header == "MSG": 
                self.outputs.append(msg.content)
                self.output_field.clear()
                self.output_field.addstr(0, 0, "\n".join(self.outputs))
                self.output_field.refresh()
    
    
    def input_method(self) -> None:
        """
        [summary]
        """
        
        while True:
            new_char = self.input_field.getch()
            
            if new_char in self.KEYS_PRINTABLE:
                if len(self.user_input) < 233:             #TODO: accoding to the field size
                    try:
                        new_input = chr(new_char)
                        self.user_input += new_input
                    except ValueError:
                        raise Exception(f"Invalid new input : {new_char}")
                
            elif new_char in self.KEYS_ENTER:
                # parsing commands
                if self.user_input.startswith("/"):
                    if self.user_input[1:] in ["leave", "exit"]:
                        pass
                # sending message
                else:
                    self.display("msg sent")
                    msg = Message(header="MSG", content=self.user_input)
                    self.socket.sendall(msg.encoded(self.encoding, self.encoding_errors))
                    
                self.user_input = ""

            elif new_char in self.KEYS_BACKSPACE:
                self.user_input = self.user_input[:-1]
                
            elif new_char == self.KEY_ESCAPE:
                exit()
            
            else:
                self.log("ERROR", "unknwown imput")
                    
            self.input_field.clear()
            self.input_field.addstr(0, 0, self.user_input)
            self.input_field.refresh()
            
            
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
        Show the NetChat Client console.

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
        self.srdscr = curses.initscr()
        self.output_border = curses.newwin(height-5, width, 0, 0)
        self.output_field = curses.newwin(height-7, width-2, 1, 1)
        self.input_border = curses.newwin(5, width, height-5, 0)                 #TODO: make the 'input' zone proportianlly big to the width and height given
        self.input_field = curses.newwin(3, width-2, height-5+1, 1)              #TODO: make the 'input' zone proportianlly big to the width and height given
        self.output_border.box()
        self.input_border.box()
        self.input_border.addstr(0, 2, "Message")
        self.output_border.addstr(0, 2, "NetChat Client")
        
        def show_gui(stdscr) -> None:
            self.output_border.refresh()
            self.input_border.refresh()            
                
        self.resize(width, height)
        self.display(f"[i] NetChat started, press ESC to exit the program")
        curses.wrapper(show_gui)
        
    
    def connect(self, host:str = "127.0.0.1", port:int = 9999) -> None:
        """
        Connect to a NetChat server.

        Parameters
        ----------
        host : str, optional
            server-target's IP address, by default "127.0.0.1"
        port : int, optional
            server-target's port, by default 9999
        """
        
        # asserts
        assert isinstance(host, str), f"Invalid 'host' data type : {type(host)}. Expected a str."
        assert isinstance(port, int), f"Invalid 'port' data type : {type(port)}. Expected an int."
        
        # attributes from arguments
        self.host = host
        self.port = port
        
        with socket.socket() as server:
            self.socket = server
            self.socket.connect((host, port))
            username_msg = Message(header="USERNAME", content=self.username)
            server.sendall(username_msg.encoded())
            
            self.display(f"[i] connected to {host}:{port}")
            
            input_thread = Thread(target=self.input_method)
            output_thread = Thread(target=self.output_method) 
            input_thread.start()
            output_thread.start()
            input_thread.join()
            output_thread.join()
        
        
    def __repr__(self) -> str:
        """Reprezentation of the NetChat Client object"""
        return f"<NetChat Client: {self.username}>"
    
    
    def __str__(self) -> str:
        """String appearance of the NetChat Client object"""
        return f"<NetChat Client: {self.username}>"
