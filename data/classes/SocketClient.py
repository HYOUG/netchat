class SocketClient:
    
    """Socket Client class"""
    
    def __init__(self, username: str = "John Doe", log_enabled: bool = True, encoding: str = "utf-8",
                 encoding_errors: str = "replace", buff_size: int = 4096) -> None:
        """
        Socket client's builder
        
        Parameters
        ----------
        username        (str)    def: John Doe - username displayed in the chat feed
        log             (bool)   def: True     - enable/disbale the log system
        encoding        (str)    def: utf-8    - encoding codec
        encoding_errors (str)    def: replace  - encoding errors handler
        buff_size       (int)    def: 4096     - socket buff size
        """
        
        # Asserts checking the data format of the builder's arguments
        assert isinstance(username, str), f"Invalid username argument format : {type(username)}. Expected a str"
        assert isinstance(log_enabled, bool), f"Invalid log_enabled argument format : {type(log_enabled)}. Expected a bool"
        assert isinstance(encoding, str), f"Invalid encoding argument format : {type(encoding)}. Expected a str"
        assert isinstance(encoding_errors, str), f"Invalid encoding_errors argument format : {type(encoding_errors)}. Expected a str"
        assert isinstance(buff_size, int), f"Invalid buff_size argument format : {type(buff_size)}. Expected an int"
        
        # asserts checking the validity of the builder's arguments value
        assert 2 <= len(username) <= 20, f""
        assert "test".encode(encoding) == b"test", f""
        assert 1024 <= buff_size <= 2**20, f""

        
        # attributes from arguments
        self.username = username
        self.log_enabled = log_enabled
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.buff_size = buff_size
        
        # attributes from initialization
        self.host = None
        self.port = None
        self.socket = None
        self.notifications = {}
        self.color_code = {}
    
       
    def log(self, log_msg) -> None:
        if self.log_enabled:
            print(f"[red]{log_msg}[red]")
       
       
    def input(self) -> None:                                                                       # SocketClient's input thread
        while True:
            content = input("")
            if content != "":
                msg = Message("MSG", None, time(), content).encoded()
                self.socket.sendall(msg)
         
            
    def output(self) -> None:                                                                      # SocketClient's output thread
        while True:
            data = self.socket.recv(self.buff_size)
            msg = Message(string_msg=data.decode())
            if msg.header == "MSG": 
                print(msg.content)
            
       
    def connect(self, host: str = "127.0.0.1", port: int = 9999) -> None:
        """Connect the socket client to the given socket server"""
        
        assert isinstance(host, str), f"Invalid username argument format : {type(host)}. Expected a str"
        assert isinstance(port, int), f"Invalid log argument format : {type(port)}. Expected an int"
        
        assert len(host.split(".")) == 4, f""
        assert 1 <= port <= 65535, f""
        
        self.host = host
        self.port = port
        with socket.socket() as server:
            self.socket = server
            server.connect((host, port))
            username_msg = Message(header="USERNAME", content=self.username).encoded()
            server.sendall(username_msg)
            self.log(f"[i] connected to {host}:{port}")
            self.log(f"[i] Press Ctrl + C to exit the program")
            
            self.input_thread = Thread(target=self.input)
            self.output_thread = Thread(target=self.output)
            
            self.input_thread.start()
            self.output_thread.start()
    
    
    def disconnect(self):
        self.socket.close()
        self.log(f"[i] disconnected")