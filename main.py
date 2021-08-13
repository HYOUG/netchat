#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

from classes.Client import Client
from classes.Server import Server
from functions.utils import *


HEADER = """
         __     _     ___ _           _   
      /\ \ \___| |_  / __\ |__   __ _| |_ 
     /  \/ / _ \ __|/ /  | '_ \ / _` | __|
    / /\  /  __/ |_/ /___| | | | (_| | |_ 
    \_\ \/ \___|\__\____/|_| |_|\__,_|\__|  by HYOUG                               
"""


def main():
    
    print(HEADER)
    
    while True:
        print("\nLaunch :")
        print("[1] Server")
        print("[2] Client")
        print("[3] Help")
        print("[4] Exit")
        
        user_input = input("\n> ")
        
        if user_input == "1":
            print("\nServer :")
            print("[1] Default settings")
            print("[2] Last used settings")
            print("[3] Custom settings")
            print("[4] Back")
            
            while True:
                user_input = input("\n> ")
                
                if user_input == "1":
                    server = Server()
                    server.show()
                    server.run()
                    break
                
                elif user_input == "2":
                    settings = get_settings("server")
                    host, port, max_users, buff_size, log_enabled, width, height = list(settings.values())
                    server = Server()
                    server.show()
                    server.run()
                    break
                
                elif user_input == "3":
                    host = input("[1/7] Host (def. = 127.0.0.1) : ")
                    port = input("[2/7] Port (def. = 9999) : ")
                    max_users = input("[3/7] Max. users (def. = 5) : ")
                    buff_size = input("[4/7] Buffer size (def. = 4096) : ")
                    log_enabled = input("[5/7] Enable log (y/n) (def. = True) :")
                    width = input("[6/7] width (def. = 80) : ")
                    height = input("[7/7] height (def. = 30) : ")
                    server = Server(host, port, max_users, buff_size, log_enabled)
                    server.show(width, height)
                    server.run()
                    break
                
                elif user_input == "4":
                    break
                
                else:
                    print("Invalid number, pleaser enter 1, 2 or 3.")
                    
            
        elif user_input == "2":
            print("\nClient :")
            print("[1] Default settings")
            print("[2] Last used settings")
            print("[3] Custom settings")
            print("[4] Back")
            
            while True:
                user_input = input("\n> ")
                
                if user_input == "1":
                    username = input("Username : ")
                    client = Client(username)
                    client.show()
                    client.connect()
                    break
                
                elif user_input == "2":
                    settings = get_settings("client")
                    username, log_enabled, encoding, encoding_errors, buff_size, width, height = list(settings.values())
                    client = Client()
                    client.show()
                    client.connect()
                    break
                
                elif user_input == "3":
                    username = input("[1/7] Username : ")
                    log_enabled = input("[2/7] Enable log (y/n) (def. = True) : ")
                    encoding = input("[3/7] Encoding (def. = utf-8) : ")
                    encoding_errors = input("[4/7] Encoding errors handling (def. = replace) : ")
                    buff_size =  input("[5/7] Buffer size (def. = 4096) : ")
                    width = input("[6/7] width (def. = 80) : ")
                    height = input("[7/7] height (def. = 30) : ")
                    client = Client(username, log_enabled, encoding, encoding_errors, buff_size)
                    client.show(width, height)
                    client.connect()
                    break
                
                elif user_input == "4":
                    break
                
                else:
                    print("Invalid number, pleaser enter 1, 2 or 3.")
            
        elif user_input == "3":
            print("\nHelp :")
            print("help")
            print("[PRESS ENTER TO RETURN TO THE MAIN MENU]")
            input()
        
        elif user_input == "4":
            exit()
        
        else:
            print("Invalid number, pleaser enter 1, 2 or 3.")



if __name__ == "__main__":
    main()