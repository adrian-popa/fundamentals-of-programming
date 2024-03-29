class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message=None):
        """
        Constructor for controller exception class
        message - A string representing the exception message
        """
        if message is None:
            message = "Game error!"
        self.__message = message

    @property
    def messages(self):
        return self.__message

    def __str__(self):
        result = "Game ERROR: " + self.__message
        return result
