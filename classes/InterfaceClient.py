import curses
from os import system
#from classes.SocketClient import SocketClient

class InterfaceClient:
    
    def __init__(self, width = 80, height = 30) -> None:
        
        self.width = width
        self.height = height
        
        self.srdscr = curses.initscr()
        self.user_input = ""
        self.outputs = []
        
        self.output_border = curses.newwin(25, 80, 0, 0)
        self.output_field = curses.newwin(23, 78, 1, 1)
        self.input_border = curses.newwin(5, 80, 25, 0)
        self.input_field = curses.newwin(3, 78, 26, 1)
        
        self.output_border.box()
        self.input_border.box()
        
        self.input_border.addstr(0, 2, "Message")
        self.output_border.addstr(0, 2, "NetChat Client")
            
        
    def run(self) -> None:
        
        def run_loop(stdscr) -> None:
            self.output_border.refresh()
            self.input_border.refresh()
            
            while True:
                new_char = self.input_field.getch()
                
                if new_char == curses.KEY_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                    
                elif new_char == curses.KEY_ENTER or new_char in [10, 13]:
                    self.outputs.append(f"> {self.user_input}")
                    self.user_input = ""
                    
                elif new_char == 27:                                            # ESCAPE Key
                    break
                
                else:
                    if len(self.user_input) < 233:
                        self.user_input += chr(new_char)  
                        
                self.input_field.clear()
                self.output_field.clear()
                
                self.input_field.addstr(0, 0, self.user_input)
                self.output_field.addstr(0, 0, "\n".join(self.outputs))
                
                self.input_field.refresh()
                self.output_field.refresh()
            
                
        system(f"mode {self.width}, {self.height}")
        curses.wrapper(run_loop)
        
        
console = InterfaceClient()
console.run()