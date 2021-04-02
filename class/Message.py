class Message:
    
    """Socket's message class"""
    
    def __init__(self, prefix: str = None, author_uuid: int = None, timestamp: float = None, 
                 content: str = None, string_msg: str = None) -> None:
        """Message object's builder"""
        
        if string_msg is not None:
            string_msg.split("|")
            self.prefix = string_msg[0]
            self.author_uuid = int(string_msg[1])
            self.timestamp = float(string_msg[2])
            self.content = "".join(string_msg[3:])
            
        else:
            self.prefix = prefix
            self.author_uuid = author_uuid
            self.timestamp = timestamp
            self.content = content
        
        
    def __str__(self) -> str:
        """String appearance of the Message object"""
        string = f"{self.prefix}|{self.author_id}|{self.timestamp}|{self.content}"
        return string
    
    
    def __repr__(self) -> str:
        """Representation of the Message object"""
        string = f"{self.prefix}|{self.author_id}|{self.timestamp}|{self.content}"
        return string
        