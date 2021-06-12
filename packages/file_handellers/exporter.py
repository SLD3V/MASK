"""
    * importing module file from .
    *
"""
from .file import File as file

"""
    * declaring class exporter
    *
"""


class Exporter(file):
    """
        * declaring constructor method
        * @param request
        * @return None
    """

    def __init__(self, request) -> None:
        self._set_writer_obj(open(request, 'w', encoding='utf-8'))

    """
        * declaring method return_req_content
        * @var None
        * @return array reader_data
    """

    def return_writer_obj(self):
        self._return_writer_obj()

    """
        * declaring method exporter_mode
        * @param None
        * @return file writer object
    """

    def exporter_mode(self):
        return self._return_writer_obj()

    """
        * declaring method read_line
        * @param None
        * @return array read data
    """

    def write_line(self, args):
        self._return_writer_obj().write(args)

    """
        * declaring method read_line
        * @param None
        * @return string file name
    """

    def name(self):
        return self._writer_obj.name
