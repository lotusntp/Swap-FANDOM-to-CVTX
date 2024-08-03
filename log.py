from colorama import Fore
from colorama import init
import time
init()

COLOR = {
    'blue': Fore.BLUE,
    'default': Fore.WHITE,
    'grey': Fore.LIGHTBLACK_EX,
    'yellow': Fore.YELLOW,
    'black': Fore.BLACK,
    'cyan': Fore.CYAN,
    'green': Fore.GREEN,
    'magenta': Fore.MAGENTA,
    'white': Fore.WHITE,
    'red': Fore.RED
}


class Log:

    hwid = None

    def __init__(self) -> None:
        pass

    def importLibs(self):
        self.log = Log()
        self.date = self.dateFormatted()


    def dateFormatted(self, format = '%Y-%m-%d %H:%M:%S'):
        datetime = time.localtime()
        formatted = time.strftime(format, datetime)
        return formatted

    def console(self, message, emoji=False, color='default'):
        self.importLibs()
        color_formatted = COLOR.get(color.lower(), COLOR['default'])

        formatted_datetime = self.dateFormatted()
        wirte_message = "{} - {}".format(formatted_datetime, message)
        console_message_colorfull = color_formatted + message + Fore.RESET
        console_message = "{} - {}".format(formatted_datetime,console_message_colorfull)

        if emoji is not False:
            console_message = "{} - {} {}".format(
                formatted_datetime, emoji, message)
          
        print(console_message)

        file = open("./logs/logger.log", "a", encoding='utf-8')
        file.write(wirte_message + '\n')
        file.close()
            
        return True
