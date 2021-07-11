#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

from classes.Client import Client
from classes.Server import Server

header_logo = """
         __     _     ___ _           _   
      /\ \ \___| |_  / __\ |__   __ _| |_ 
     /  \/ / _ \ __|/ /  | '_ \ / _` | __|
    / /\  /  __/ |_/ /___| | | | (_| | |_ 
    \_\ \/ \___|\__\____/|_| |_|\__,_|\__|  by HYOUG                               
    """


def main():
    
    print(header_logo)
    
    print("[1] - Server")
    print("[2] - Client")
    print("[3] - Help")
    user_input = input("\n> ")
    
    while True:
        if user_input == "1":
            print("\nServer :")
            print("[1] - Default settings")
            print("[2] - Last used settings")
            print("[3] - Custom settings")
            user_input = input("\n> ")
            
            while True:
                if user_input == "1":
                    server = Server()
                    server.show()
                    server.run()
                    break
                
                elif user_input == "2":
                    server = Server()
                    server.show()
                    server.run()
                    break
                
                elif user_input == "3":
                    server = Server()
                    server.show()
                    server.run()
                    break
                
                else:
                    print("Invalid number, pleaser enter 1, 2 or 3.")
                    
            
        elif user_input == "2":
            print("\nClient :")
            print("[1] - Default settings")
            print("[2] - Last used settings")
            print("[3] - Custom settings")
            user_input = input("\n> ")
            
            while True:
                if user_input == "1":
                    client = Client(username=input("Username : "))
                    client.show()
                    client.connect()
                    break
                
                elif user_input == "2":
                    client = Client()
                    client.show()
                    client.connect()
                    break
                
                elif user_input == "3":
                    client = Client(username=input("Username : "))
                    client.show()
                    client.connect()
                    break
                
                else:
                    print("Invalid number, pleaser enter 1, 2 or 3.")
            
        elif user_input == "3":
            print("\nHelp :")
            print("help")
            break
        
        else:
            print("Invalid number, pleaser enter 1, 2 or 3.")
    
    #username = input("Enter you username : ")
    #host = input("Enter the socket server HOST : ")
    #port = int(input("Enter the socket server PORT : "))  
    #user = SocketClient(username=username)
    # user.connect(host=host, port=port)


if __name__ == "__main__":
    main()