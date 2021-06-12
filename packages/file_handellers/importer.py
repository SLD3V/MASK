"""
    * importing module file from .
    *
"""
from .file import File as file

"""
    * declaring class importer
    *
"""


class Importer(file):

    """
        * declaring constructor method
        * @param array request
        * @return None
    """

    def __init__(self, request) -> None:
        self._set_reader_obj(open(request, 'r', encoding='utf-8'))

    """
        * declaring method return response
        * @var None
        * @return array reader_data
    """

    def return_reader_obj(self):
        self._return_reader_obj()

    """
        * declaring method read_line
        * @param None
        * @return array read data
    """

    def read_line(self):
        return self._return_reader_obj().readline().split()

    """
        * declaring method read_line
        * @param None
        * @return array read data
    """

    def read(self):
        return self._return_reader_obj().read().splitlines()

    """
        * declaring method read_line
        * @param None
        * @return string file name
    """

    def name(self):
        return self._reader_obj.name
