"""
    * import os
    * import sys
    * import pyfiglet
    * importing
    * import module variants from .

"""
import os
import sys
import pyfiglet
from colorama import Fore, Back, Style, init
from .variants import Variant as varients

"""
    * declaring class Format
    *
"""


class Format(varients):
    # initializing colorama.init to True
    init(autoreset=True)

    """
        * declaring class method clear
        * @param None
        * @return None
    """

    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    """
        * declaring class method sys_exit
        * @param None
        * @return None
    """
    @staticmethod
    def sys_exit():
        sys.exit(0)

    """
        * declaring class method return_ascii_banner
        * @param None
        * @return None
    """

    @classmethod
    def return_ascii_banner(cls):
        # calling a line break
        cls.line_break()
        print("\033[1m" + Fore.RED + Style.BRIGHT + pyfiglet.figlet_format(" MASK", font="slant") + "\033[1m")
        print("-----------------------------------\n")
        print("\033[1m" + (Fore.WHITE + Back.RED + "Developers : Saneth K. | Shehan W. ") + "\033[0m")
        print(Fore.YELLOW + "\nctrl + C to exit the program")
        # calling a line break
        cls.line_break()
