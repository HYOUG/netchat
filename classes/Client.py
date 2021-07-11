import socket
import curses
from threading import Thread
from classes.Message import Message
from functions.utils import *
from json import load, dump
from os import system


class Client:
    
    def __init__(self, username:str = "foo", log:bool = True, encoding:str = "utf-8",
                 encoding_errors:str = "replace", buff_size:int = 4096, width:int = 80, height:int = 30) -> None:
        """
        Generate a Client object

        Parameters
        ----------
        username : str, optional
            user's name used in the chat channel, by default "foo"
        log : bool, optional
            enable or disable the logs, by default True
        encoding : str, optional
            encoding type used in the data sent/received, by default "utf-8"
        encoding_errors : str, optional
            error handling method used in the data sent/received, by default "replace"
        buff_size : int, optional
            buffer size used when data is received, by default 4096
        width : int, optional
            width of the window, by default 80
        height : int, optional
            height of the window, by default 30
        """
        
        # attributes from arguments
        self.width = width
        self.height = height
        self.username = username
        self.log = log
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.buff_size = buff_size
        
        # attributes from initialization
        self.host = None
        self.port = None
        self.socket = None
        self.notifications = {}
        self.color_code = {}
        self.srdscr = curses.initscr()
        self.user_input = ""
        self.outputs = []
        self.settings = load(open("./settings/client.json", "r").read())
        
        self.output_border = curses.newwin(25, 80, 0, 0)
        self.output_field = curses.newwin(23, 78, 1, 1)
        self.input_border = curses.newwin(5, 80, 25, 0)
        self.input_field = curses.newwin(3, 78, 26, 1)
        self.output_border.box()
        self.input_border.box()
        self.input_border.addstr(0, 2, "Message")
        self.output_border.addstr(0, 2, "NetChat Client")
        
        
    def display(self, txt) -> None:
        self.outputs.append(txt)
        self.output_field.clear()
        self.output_field.addstr("\n".join(self.outputs))
        self.output_field.refresh()
        
        
    def output(self) -> None:
        while True:
            data = self.socket.recv(self.buff_size)
            print("reçu reçu")
            msg = Message()
            msg.parse(data.decode())
            if msg.header == "MSG": 
                self.outputs.append(msg.content)
                self.output_field.clear()
                self.output_field.addstr(0, 0, "\n".join(self.outputs))
                self.output_field.refresh()
    
    
    def input(self) -> None:
        while True:
            new_char = self.input_field.getch()
            
            if new_char == curses.KEY_BACKSPACE:
                self.user_input = self.user_input[:-1]
                
            elif new_char == curses.KEY_ENTER or new_char in [10, 13]:
                # parsing commands
                if self.user_input.startswith("/"):
                    pass
                
                else:
                    msg = Message(header="MSG", content=self.user_input)
                    self.socket.sendall(msg.encoded())
                    
                self.user_input = ""
                
            elif new_char == 27:                                            # ESCAPE Key
                break
            
            else:
                if len(self.user_input) < 233:
                    self.user_input += chr(new_char)  
                    
            self.input_field.clear()
            self.input_field.addstr(0, 0, self.user_input)
            self.input_field.refresh()
        
    
    def connect(self, host:str = "127.0.0.1", port:int = 9999) -> None:
        """
        Connect to a NetChat server

        Parameters
        ----------
        host : str, optional
            server-target's IP adress, by default "127.0.0.1"
        port : int, optional
            server-target's port, by default 9999
        """
        
        assert isinstance(host, str), f"Invalid username argument format : {type(host)}. Expected a str"
        assert isinstance(port, int), f"Invalid log argument format : {type(port)}. Expected an int"
        
        assert len(host.split(".")) == 4, f""
        assert 1 <= port <= 65535, f""
        
        self.host = host
        self.port = port
        
        with socket.socket() as server:
            self.socket = server
            self.socket.connect((host, port))
            username_msg = Message(header="USERNAME", content=self.username)
            server.sendall(username_msg.encoded())
            
            self.display(f"[i] connected to {host}:{port}")
            self.display(f"[i] Press ESC to exit the program")
            
            input_thread = Thread(target=self.input)
            output_thread = Thread(target=self.output)
            
            input_thread.start()
            output_thread.start()
            
            input_thread.join()
            output_thread.join()
            
        
    def show(self) -> None:
        
        def show_gui(stdscr) -> None:
            self.output_border.refresh()
            self.input_border.refresh()            
                
        system(f"mode {self.width}, {self.height}")
        curses.wrapper(show_gui)