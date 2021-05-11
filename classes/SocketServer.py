import socket
import asyncio
from classes.Message import Message
from threading import Thread
# from rich import print


class SocketServer:
    
    """Socket Server class"""
    
    def __init__(self, host: str = "127.0.0.1", port: int = 9999, max_users: int = 5,
                 buff_size: int = 4096, log_enabled: bool = True, encoding: str = "utf-8",
                 encoding_errors: str = "replace", socket_opt: list = []) -> None:
        
        """
        Parameters
        ----------
        host            (str)  def: 127.0.0.1 - socket server host
        port            (int)  def: 9999      - socket server port
        max_users       (int)  def: 5         - maximum number of user
        buff_size       (int)  def: 4096      - socket server buff size
        log_enabled     (bool) def: True      - whether or not logs are enabled
        encoding        (str)  def: utf-8     - encoding codec
        encoding_errors (str)  def: replace   - encoding errors handler
        socket_opt      (list) def: None      - socket object options
        """
        
        # asserts checking the data format of the builder's arguments
        # assert isinstance(host, str), f"Invalid username argument format : {type(host)}. Expected a str"
        # assert isinstance(port, int), f"Invalid port argument format : {type(port)}. Expected an int"
        # assert isinstance(max_users, int), f"Invalid max_users argument format : {type(max_users)}. Expected an int"
        # assert isinstance(buff_size, int), f"Invalid buff_size argument format : {type(buff_size)}. Expected an int"
        # assert isinstance(log_enabled, bool), f"Invalid log_enabled argument format : {type(log_enabled)}. Expected a bool"
        # assert isinstance(encoding, str), f"Invalid encoding argument format : {type(encoding)}. Expected a str"
        # assert isinstance(encoding_errors, str), f"Invalid encoding_errors argument format : {type(encoding_errors)}. Expected a str"
        # assert isinstance(socket_opt, list), f"Invalid socket_opt argument format : {type(socket_opt)}. Expected a list"
        
        # asserts checking the validity of the builder's arguments value
        assert len(host.split(".")) == 4, f""
        assert 1 <= port <= 65535, f""
        assert 1 <= max_users <= 100, f""
        assert 1024 <= buff_size <= 2**20, f""
        assert "test".encode(encoding) == b"test", f""
        
        # attributes from arguments
        self.host = host
        self.port = port
        self.max_users = max_users
        self.buff_size = buff_size
        self.print_enabled = log_enabled
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.socket_opt = socket_opt
        
        # attributes from initialization
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
    
        
    def redirect(self, msg: Message) -> None:
        """Redirect the given message to the clients"""
        for client in self.clients:
            try:
                client["connection"].sendall(msg.encoded())
                print(f"[i] Message sent to {client['id']}")
            except ConnectionResetError:
                print("Unreacheable target")
        
        
    def listen(self, client_num: int) -> None:
        """Listen thread that listen to the given client"""
        print(f"[i] The socket server is now listening to {client_num}")
        connection = self.clients[client_num]["connection"]
        i = 0
        
        while True:
            
            print(i)
            
            data = connection.recv(self.buff_size)
            print("anchor Diamond")
            msg = Message()
            msg.parse(data.decode())
            
            if msg.header == "USERNAME":
                self.clients[client_num]["username"] = msg.content
            elif msg.header == "ENCODING":
                pass
            elif msg.header == "ENCODING_ERRORS":
                pass
            elif msg.header == "MSG":
                print("mars")
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
                raise Exception(f"Unexpected header : {msg.header}")
            
            i += 1
        
        
    def run(self) -> None:
        """Run the socket server"""
        with socket.socket() as server:
            server.bind((self.host, self.port))
            server.listen(self.max_users)
            
            self.socket = server
            self.isopened = True
            
            print(f"|i| The socket server is now running")
            print(f"|i| Settings : {self.host}:{self.port}")
            print(f"|i| The socket server is now open")
            
            while True:
                if self.isopened:
                    server.listen(self.max_users)
                    (clientsocket, address) = server.accept()
                    
                    print(f"[i] {address[0]}:{address[1]} joined the server")
                    client_obj = {"connection": clientsocket, "address": address, "id": self.client_num}
                    self.clients.append(client_obj)
                    listen_thread = Thread(target=self.listen, args=[self.client_num])
                    listen_thread.start()
                    self.client_num += 1
                else:
                    print("[i] The socket server is now closed")
                    break
            

    def kill(self) -> None:
        """Shutdown the socket server"""
        print("Ancho wow")
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print("[i] The socket server have been shutdown")


    def close(self) -> None:
        """Stop the login loop thread"""
        print("Anchor OK")
        self.isopened = False
        print("[i] Login : False")