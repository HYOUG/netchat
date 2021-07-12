from random import randint

class User:
    
    """NetChat's user class"""
    
    def __init__(self, host:str = "0.0.0.0", port:int = 9999, username:str = "John Doe",
                 uuid:str = str(randint(1000, 9999)), encoding:str = "utf-8",
                 encoding_error:str = "replace") -> None:
        """
        [summary]

        Parameters
        ----------
        host : str, optional
            [description], by default "0.0.0.0"
        port : int, optional
            [description], by default 9999
        username : str, optional
            [description], by default "John Doe"
        uuid : str, optional
            [description], by default str(randint(1000, 9999))
        encoding : str, optional
            [description], by default "utf-8"
        encoding_error : str, optional
            [description], by default "replace"
        """
        
        # asserts
        assert isinstance(host, str), f"Invalid username argument format : {type(host)}. Expected a str."
        assert isinstance(port, int), f"Invalid port argument format : {type(port)}. Expected an int."
        assert isinstance(username, str), f"Invalid username argument format : {type(username)}. Expected an str."
        assert isinstance(uuid, str), f"Invalid uuid argument format : {type(uuid)}. Expected a string."
        assert isinstance(encoding, str), f"Invalid encoding argument format : {type(encoding)}. Expected a string."
        assert isinstance(encoding_error, str), f"Invalid encoding_errors argument format : {type(encoding_error)}. Expected a string."
        
        # attributes from arguments
        self.host = host
        self.port = port
        self.username = username
        self.uuid = uuid
        self.encoding = encoding
        self.encoding_errors = encoding_error
        
        
    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"<User: {self.uuid}>"
        
        
    def __str__(self) -> str:
        """String appearance of the User object"""
        return f"<User: {self.uuid}>"