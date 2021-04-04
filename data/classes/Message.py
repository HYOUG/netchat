from classes.User import User

class Message:
    
    """Socket's message class"""
    
    def __init__(self, header: str = None, author: User = None, timestamp: float = None, 
                 content: str = None) -> None:
        """
        Message object's builder
        
        Parameters
        ----------
        header      (header) def:None - message's header/prefix
        author_uuid (int)    def:None - message's author's unique universal ID
        timestamp   (float)  def:None - message's timestamp 
        content     (str)    def:None - message's content
        """
        
        # attributes from arguments
        self.header = header
        self.author = author
        self.timestamp = timestamp
        self.content = content
        
        # attributes from initialization
        self.author_uuid = self.author.uuid
                    
            
    def setfromstring(self, string) -> None:
        string.split("|")
        self.header = string[0]
        self.author_uuid = int(string[1])
        self.timestamp = float(string[2])
        self.content = "".join(string[3:])
            
        
    def __str__(self) -> str:
        """String appearance of the Message object"""
        string = f"{self.header}|{self.author_uuid}|{self.timestamp}|{self.content}".replace("None", "")
        return string
    
    
    def __repr__(self) -> str:
        """Representation of the Message object"""
        string = f"{self.header}|{self.author_uuid}|{self.timestamp}|{self.content}".replace("None", "")
        return string
    
    
    def encoded(self, encoding: str = "utf-8", encoding_errors: str = "replace") -> bytes:
        """Encoded version of the message"""
        return str(self).encode(encoding, encoding_errors)
        