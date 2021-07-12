from functions.utils import NoneType
from classes.User import User

class Message:
    
    """NetChat's message class"""
    
    def __init__(self, header:str = "MSG", author:User = None, timestamp:float = None,
                 content:str = None) -> None:
        """
        [summary]

        Parameters
        ----------
        header : str, optional
            [description], by default "MSG"
        author : User, optional
            [description], by default None
        timestamp : float, optional
            [description], by default None
        content : str, optional
            [description], by default None
        """
        
        # asserts
        assert isinstance(header, str), f"Invalid 'header' data type : {type(header)}. Expected a str."
        assert isinstance(author, (User, NoneType)), f"Invalid 'author' data type : {type(author)}. Expected a str or NoneType."
        assert isinstance(timestamp, (float, NoneType)), f"Invalid 'timestamp' data type : {type(timestamp)}. Expected a float or NoneType."
        assert isinstance(content, (str, NoneType)), f"Invalid 'content' data type : {type(content)}. Expected a str or NoneType."
        
        # attributes from arguments
        self.header = header
        self.author = author
        self.timestamp = timestamp
        self.content = content
                    
            
    def parse(self, string:str) -> None:
        slots = string.split("|")       
        self.header = slots[0]
        self.author = slots[1]
        self.timestamp = slots[2]
        self.content = "".join(slots[3:])
        
        
    def  __repr__(self) -> str:
        """Reprezentation of the Message object"""
        return f"<Message: {self.header}|{self.author}|{self.timestamp}|{self.content}>".replace("None", "")
        
        
    def __str__(self) -> str:
        """String appearance of the Message object"""
        return f"<Message: {self.header}|{self.author}|{self.timestamp}|{self.content}>".replace("None", "")
    
    
    def encoded(self, encoding:str = "utf-8", encoding_errors:str = "replace") -> bytes:
        """Encoded version of the message"""
        return str(self).encode(encoding, encoding_errors)
        