from functions.utils import NoneType
from classes.User import User

class Message:
    """
    [summary]
    """
    
    def __init__(self, header:str = None, author:User = None, timestamp:float = None,
                 content:str = None) -> None:
        """
        Generate a NetChat Message.

        Parameters
        ----------
        header : str, optional
            Message's header, by default None
        author : User, optional
            Message's author, by default None
        timestamp : float, optional
            Message's timestamp, by default None
        content : str, optional
            Message's content, by default None
        """
        
        # asserts
        assert isinstance(header, (str, NoneType)), f"Invalid 'header' data type : {type(header)}. Expected a str or NoneType."
        assert isinstance(author, (User, NoneType)), f"Invalid 'author' data type : {type(author)}. Expected a str or NoneType."
        assert isinstance(timestamp, (float, NoneType)), f"Invalid 'timestamp' data type : {type(timestamp)}. Expected a float or NoneType."
        assert isinstance(content, (str, NoneType)), f"Invalid 'content' data type : {type(content)}. Expected a str or NoneType."
        
        # attributes from arguments
        self.header = header
        self.author = author
        self.timestamp = timestamp
        self.content = content
        
        
    def  __repr__(self) -> str:
        """Reprezentation of the Message object"""
        return f"<Message: {self.header}|{self.author}|{self.timestamp}|{self.content}>".replace("None", "")
        
        
    def __str__(self) -> str:
        """String appearance of the Message object"""
        return f"<Message: {self.header}|{self.author}|{self.timestamp}|{self.content}>".replace("None", "")
    
    
    def encoded(self, encoding:str = "utf-8", encoding_errors:str = "replace") -> bytes:
        """
        Encoded version of the message.

        Parameters
        ----------
        encoding : str, optional
            [description], by default "utf-8"
        encoding_errors : str, optional
            [description], by default "replace"

        Returns
        -------
        bytes
            [description]

        Raises
        ------
        Exception
            [description]
        """
        
        try:
            short_repr = f"{self.header}|{self.author}|{self.timestamp}|{self.content}".replace("None", "")
            return short_repr.encode(encoding, encoding_errors)
        except UnicodeEncodeError:
            raise Exception("")                                  #TODO
        
        
    def parse(self, string:str) -> None:
        """
        [summary]

        Parameters
        ----------
        string : str
            [description]
            
            
        Raises
        ------
        Exception
            [description]
        """
        
        try:
            slots = string.split("|")       
            self.header = slots[0]
            self.author = slots[1]
            self.timestamp = slots[2]
            self.content = "".join(slots[3:])
        except ValueError:
            Exception("")
            
        