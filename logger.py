from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

COLORS = {
    "EVENT": Fore.CYAN,
    "DATA": Fore.YELLOW,
    "INTENT": Fore.MAGENTA,
    "RESPONSE": Fore.GREEN,
    "BOT": Fore.BLUE,
    "ERROR": Fore.RED
}

def log(tag, message):
    now = datetime.now().strftime("%H:%M:%S")
    color = COLORS.get(tag, Fore.WHITE)

    print(f"{Fore.WHITE}[{now}] {color}[{tag}] {Style.BRIGHT}{message}")
