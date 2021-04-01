from colorama import Fore, init                                                     # the 'chat effects' are from the colorama module

init(convert=True)                                                                  # set convert to True, avoiding characters display bugs

def red(text: str):                                                                 # func. that return a 'red' color text
    colored_text = Fore.LIGHTRED_EX + str(text) + Fore.RESET
    return colored_text


def blue(text: str):                                                                # func. that return a 'blue' color text
    colored_text = Fore.LIGHTBLUE_EX + str(text) + Fore.RESET
    return colored_text


def green(text: str):                                                               # func. that return a 'green' color text
    colored_text = Fore.LIGHTGREEN_EX + str(text) + Fore.RESET
    return colored_text


def yellow(text: str):                                                              # func. that return a 'yellow' color text
    colored_text = Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET
    return colored_text


def pink(text: str):                                                                # func. that return a 'pink' color text
    colored_text = Fore.LIGHTMAGENTA_EX + str(text) + Fore.RESET
    return colored_text


def cyan(text: str):                                                                # func. that return a 'cyan' color text
    colored_text = Fore.LIGHTCYAN_EX + str(text) + Fore.RESET
    return colored_text