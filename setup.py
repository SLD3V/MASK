"""
    * import os
    * import pip
    * importing module format from packages.visualizers
    * importing module importer from packages.file_handlers
    * importing module constants from src
"""
import os
import pip
from packages.file_handellers.importer import Importer as importer
from src.constants import Constants as const

"""
    * declaring class Installer
"""


class Installer:
    @staticmethod
    def installer():
        # initializing importer obj
        importer_obj = importer(
            const.STATIC_PATH + const.FILE_NAMES[0][0] + '.' + const.FILE_NAMES[0][1]
        )

        print("\nChecking Requirements...")
        print("\nInstalling requirements...\n")

        for requirements in importer_obj.read():
            pip.main(['install', requirements])

    @staticmethod
    def run_wizard():
        os.system('cls' if os.name == 'nt' else 'clear')
        # taking user_input to decide abt the execution
        ask_usr = input("Do you want to continue ? [Y/n] :: ").strip().upper()

        if ask_usr == "Y" or ask_usr == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            Installer.installer()

            # importing ascii banner from packages.visualizer.format as format
            from packages.visualizers.format import Format as format

            format.clear()
            format.return_ascii_banner()
            print("MASK has successfully installed.\n")
            print("Type 'bash mask.sh' to run the program.\n")
            format.line_break()

        elif ask_usr == "N":
            print("Requirements aren't satisfied...exiting.")

        else:
            print("Wrong Input...aborting.")
            return 0


Installer.run_wizard()
