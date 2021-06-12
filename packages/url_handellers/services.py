"""
    * declaring class Services
    * importing module format from ..visualizers
"""
import requests
from ..visualizers.format import Format as formatter


class Services:
    """
        * declaring method get_url_services

    """

    @classmethod
    def __get_url_services(cls):
        """
            * initializing class variable private dict url_services
            * @param None
            * @return dict url_services
        """
        return {
            '01': "is.gd", '02': "da.gd",
            '03': "clck.ru", '04': "qps.ru", '05': "ulvis.net",
        }

    """
        * declaring class method private get_url_callers
        * @param None
        * @return dict url_callers
    """

    @classmethod
    def __get_url_callers(cls, arg):
        return {
            '01': cls._service_isgd(arg), '02': cls._service_dagd(arg),
            '03': cls._service_clckru(arg), '04': cls._service_qpsru(arg),
            '04': cls._service_ulvis()
        }

    """
        * declaring method service_isgd
        * @param str arg
        * @return str request.response()
    """

    @classmethod
    def __service_isgd(cls, arg):
        return str(requests.get("https://is.gd/create.php?format=simple&url=" + arg).text)[8:].strip()

    """
        * declaring method service_dagd
        * @param str arg
        * @return str request.response()
    """

    @classmethod
    def __service_dagd(cls, arg):
        return str(requests.get("https://da.gd/?url=" + arg).text)[8:].strip()

    """
        * declaring method service_clckru
        * @param str arg
        * @return str request.response()
    """

    @classmethod
    def __service_clckru(cls, arg):
        return str(requests.get("https://clck.ru/--?url=" + arg).text)[8:].strip()

    """
        * declaring method service_qpsru
        * @param str arg
        * @return str request.response()
    """

    @classmethod
    def __service_qpsru(cls, arg):
        return str(requests.get("https://qps.ru/api?url=" + arg).text)[8:].strip()

    """
        * declaring method service_ulvis
        * @param str arg
        * @return str request.response()
    """

    @classmethod
    def __service_ulvis(cls, arg):
        return str(requests.get("https://ulvis.net/api.php?url=" + arg).text)[8:].strip()

    """
        * declaring class method 
        * @param
        * @return str
    """

    @classmethod
    def url_service_manager(cls, arg):
        print("--- PLEASE SELECT A SERVICE ---\n")
        for itr, mdl in enumerate(cls.__get_url_services()):
            print("===>> [{mdl_code}] {service_name} ".format(mdl_code=mdl, service_name=cls.__get_url_services()[mdl]))

        short_service = input("\n[*] Enter the number :: ").strip()

        if (short_service == "1") or (short_service == "01"):
            return cls.__service_isgd(arg)
        elif (short_service == "2") or (short_service == "02"):
            return cls.__service_dagd(arg)
        elif (short_service == "3") or (short_service == "03"):
            return cls.__service_clckru(arg)
        elif (short_service == "4") or (short_service == "04"):
            return cls.__service_qpsru()
        elif (short_service == "5") or (short_service == "04"):
            return cls.__service_ulvis(arg)
        else:
            formatter.line_break()
            print("Wrong input...exiting.")
            formatter.line_break()
            formatter.sys_exit()
