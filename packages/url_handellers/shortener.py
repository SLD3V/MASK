"""
    * importing urllib
    * importing module services from .
    * importing module format from packages.visualizers
    *
"""
import urllib
from .services import Services as services
from ..visualizers.format import Format as formater

"""
    * declaring class Shortener
"""


class Shortener(services):
    """
        * declaring constructor
        * @param
        * @return None
    """

    def __init__(self, url, fake_url='', keyword='') -> None:
        self.__url = url
        self.__fake_url = fake_url
        self.__keyword = keyword

    """
        * declaring method set_fake_url
        * @param fake_url
        * @return None
    """

    def set_fake_url(self, fake_url) -> None:
        self.__fake_url = fake_url

    """
        * declaring method set_keyword
        * @param keyword
        * @return None
    """

    def set_keyword(self, keyword) -> None:
        self.__keyword = keyword

    """
        * declaring instant method shortener
        * @param None
        * @return 
    """

    def shortener(self):
        formater.line_break()

        # setting self variable fake_url
        self.set_fake_url(str(input("[*] Enter a fake URL :: ")).strip())
        # setting self variable keyword
        self.set_keyword(str(input("[*] Enter a keyword :: ")).strip())

        formater.line_break()
        formater.line_break()
        print(
            formater.return_color('FG_GREEN') +
            "Short URL :: " + self.__fake_url + "-" + self.__keyword + "@" + str(
                services.url_service_manager(urllib.parse.quote(self.__url)))
        )
        formater.line_break()
