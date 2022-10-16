class ServiceException(Exception):
    """
    Base except which all logo_service errors extend
    """
    pass


class LogoException(ServiceException):
    def __init__(self, message: str):
        self.message = message
