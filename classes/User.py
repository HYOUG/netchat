from random import randint

class User:
    
    """Socket user class"""
    
    def __init__(self, host:str = "0.0.0.0", port:int = 9999, username:str = "John Doe",
                 uuid:str = str(randint(1000, 9999)), encoding:str = "utf-8") -> None:
        """        
        Parameters
        ----------
        host     (str) def: None - user's host 
        port     (int) def: None - user's port
        username (str) def: None - user's username
        uuid     (int) def: None - user's unique universal ID
        encoding (str) def: None - users's encoding system
        """
        
        # asserts
        assert isinstance(host, str) or host is None, f"Invalid username argument format : {type(host)}. Expected a str"
        assert isinstance(port, int) or port is None, f"Invalid port argument format : {type(port)}. Expected an int"
        assert isinstance(username, str) or username is None, f"Invalid username argument format : {type(username)}. Expected an str"
        assert isinstance(username, str) or username is None, f"Invalid username argument format : {type(username)}. Expected an str"
        
        self.host = host
        self.port = port
        self.username = username
        self.uuid = uuid
        self.encoding = encoding
        
        
    def __str__(self) -> str:
        """String appearance of the User object"""
        return f"<User UUID: {self.uuid}>"
    
    
    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"<User UUID: {self.uuid}>"