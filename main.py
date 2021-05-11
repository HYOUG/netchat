#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

from classes.Client import Client
from classes.Server import Server


def main():
    
    header_logo = """
         __     _     ___ _           _   
      /\ \ \___| |_  / __\ |__   __ _| |_ 
     /  \/ / _ \ __|/ /  | '_ \ / _` | __|
    / /\  /  __/ |_/ /___| | | | (_| | |_ 
    \_\ \/ \___|\__\____/|_| |_|\__,_|\__|                                 
    """
    
    print(header_logo)
    
    
    #username = input("Enter you username : ")
    #host = input("Enter the socket server HOST : ")
    #port = int(input("Enter the socket server PORT : "))  
    #user = SocketClient(username=username)
    # user.connect(host=host, port=port)


if __name__ == "__main__":
    main()