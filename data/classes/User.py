class User:
    
    """Socket user class"""
    
    def __init__(self, host: str = None, port: int = None, username: str = None,
                 uuid: int = None) -> None:
        """
        User object's builder
        
        Parameters
        ----------
        host     (str) def: None - user's host 
        port     (int) def: None - user's port
        username (str) def: None - user's username
        uuid     (int) def: None - user's unique universal ID
        """
        
        self.host = host
        self.port = port
        self.username = username
        self.uuid = uuid
        
        
    def __str__(self) -> str:
        """String appearance of the User object"""
        return self.uuid
    
    
    def __repr__(self) -> str:
        """Representation of the User object"""
        return self.uuid