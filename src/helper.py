"""
    * importing module format from packages.visualizers
    * importing module shortener from packages.shortener
"""
from packages.visualizers.format import Format as formatter
from packages.url_handellers.shortener import Shortener as shortener

"""
    * declaring class Helper
"""


class Helper:
    """
        * declaring static method helper
        * @param
    """
    @staticmethod
    def helper():
        # calling formatter.clear method
        formatter.clear()
        # calling formatter.ascii_banner method
        formatter.return_ascii_banner()

        # initializing shortener object
        shortener_obj = shortener(input("[*] Enter a long url (http/https) :: ").strip())

        # taking the output
        shortener_obj.shortener()
