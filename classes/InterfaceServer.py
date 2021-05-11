import curses
from os import system
from classes.SocketClient import SocketClient

class InterfaceServer:
    
    def __init__(self, width = 80, height = 30) -> None:
        
        self.height = height
        self.width = width
        
        self.srdscr = curses.initscr()
        self.outputs = []
        
        self.output_border = curses.newwin(self.height, self.width, 0, 0)
        self.output_field = curses.newwin(self.height - 1, self.width -1, 1, 1)
        
        self.output_border.box()
        self.output_border.addstr(0, 2, "NetChat Server")
        
    def run(self) -> None:
        
        def run_loop(stdscr) -> None:
            
            self.output_field.clear()
            self.output_field.refresh()
        
        system(f"mode {self.width}, {self.height}")
        curses.wrapper(run_loop)