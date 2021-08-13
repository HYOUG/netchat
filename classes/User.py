from functions.utils import NoneType
from socket import socket

class User:
    """
    [summary]
    """
    
    def __init__(self, _socket:socket, address:tuple, uuid:int, username:str = None,
                 encoding:str = "utf-8", encoding_error:str = "replace") -> None:
        """
        Generate a NetChat user.

        Parameters
        ----------
        user_socket : socket
            [description]
        address : tuple
            [description]
        uuid : int
            [description]
        username : str, optional
            [description], by default None
        encoding : str, optional
            [description], by default "utf-8"
        encoding_error : str, optional
            [description], by default "replace"
        """
        
        # asserts
        assert isinstance(_socket, socket), f"Invalid '_socket' data type : {type(socket)}. Expected a socket."
        assert isinstance(address, tuple), f"Invalid 'address' data type : {type(address)}. Expected a tuple."
        assert isinstance(uuid, int), f"Invalid 'uuid' data type : {type(uuid)}. Expected an int."
        assert isinstance(username, (str, NoneType)), f"Invalid 'username' data type : {type(username)}. Expected a str or NoneType."
        assert isinstance(encoding, str), f"Invalid 'encoding' data type : {type(encoding)}. Expected a str."
        assert isinstance(encoding_error, str), f"Invalid 'encoding_errors' data type : {type(encoding_error)}. Expected a str."
        
        # attributes from arguments
        self.socket = _socket
        self.address = address
        self.host, self.port = address
        self.uuid = uuid
        self.username = username
        self.encoding = encoding
        self.encoding_errors = encoding_error
        
        
    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"<User: {self.uuid}>"
        
        
    def __str__(self) -> str:
        """String appearance of the User object"""
        return f"<User: {self.uuid}>"