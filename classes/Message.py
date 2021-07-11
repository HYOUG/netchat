from classes.User import User

class Message:
    
    """Socket's message class"""
    
    def __init__(self, header:str = "MSG", author:str = None, timestamp:float = None,
                 content:str = "Hello, World!") -> None:
        
        """
        Parameters
        ----------
        header      (str)    def:None - message's header/prefix
        author      (User)   def:None - message's author
        timestamp   (float)  def:None - message's timestamp 
        content     (str)    def:None - message's content
        """
        
        # asserts
        assert isinstance(header, str) or header is None, f"Invalid header argument format : {type(header)}. Expected a str"
        assert isinstance(author, User) or header is None, f"Invalid author argument format : {type(author)}. Expected a User"
        assert isinstance(timestamp, float) or header is None, f"Invalid timestamp argument format : {type(timestamp)}. Expected a float"
        assert isinstance(content, str) or header is None, f"Invalid content argument format : {type(content)}. Expected a str"
        
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
        