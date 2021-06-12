"""
    * declaring class File
    *
"""


class File:
    """
        * declaring class variables
    """
    _reader_obj = None
    _writer_obj = None

    """
        * declaring method for set reader_data
        * @param request
        * @return None
    """

    def _set_reader_obj(self, request) -> None:
        self._reader_obj = request
        return None

    """
        * declaring method for return reader_data
        * @param None
        * @return array response
    """

    def _return_reader_obj(self):
        return self._reader_obj

    """
        * declaring method for set reader_data
        * @param request
        * @return None
    """

    def _set_writer_obj(self, request) -> None:
        self._writer_obj = request
        return None

    """
        * declaring method for return writer_data
        * @param None
        * @return array response
    """

    def _return_writer_obj(self):
        return self._writer_obj

    """
        * declaring the file closer method
        *
    """

    @staticmethod
    def f_closer(f_object) -> None:
        f_object.close()
        return None
