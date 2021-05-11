from json import load, dump
from colorama import Fore, init
from colored import fg, attr
import curses

init(convert=True)

def get_settings():
    f = open("settings/settings.json", "r")
    settings = load(f)
    f.close()
    return settings


def edit_settings(key: str, value: str):
    settings = get_settings()
    settings[key] = value
    f = open("settings/settings.json", "w")
    dump(settings, f)
    f.close()
    
    
def red(text: str):                                                                 # func. that gen. a 'red' color
    colored_text = Fore.LIGHTRED_EX + str(text) + Fore.RESET
    return colored_text


def blue(text: str):                                                                # func. that gen. a 'blue' color
    colored_text = Fore.LIGHTBLUE_EX + str(text) + Fore.RESET
    return colored_text


def green(text: str):                                                               # func. that gen. a 'green' color
    colored_text = Fore.LIGHTGREEN_EX + str(text) + Fore.RESET
    return colored_text


def yellow(text: str):                                                              # func. that gen. a 'yellow' color
    colored_text = Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET
    return colored_text


def pink(text: str):                                                                # func. that gen. a 'pink' color
    colored_text = Fore.LIGHTMAGENTA_EX + str(text) + Fore.RESET
    return colored_text


def cyan(text: str):                                                                # func. that gen. a 'cyan' color
    colored_text = Fore.LIGHTCYAN_EX + str(text) + Fore.RESET
    return colored_text


# info = f"[{blue('i')}]"
# warn = f"[{yellow('!')}]"
# error = f"[{red('X')}]"

# info = f"[{fg(25)}i{attr(0)}]"
# warn = f"[{fg(226)}!{attr(0)}]"
# error = f"[{fg(1)}X{attr(0)}]"

    