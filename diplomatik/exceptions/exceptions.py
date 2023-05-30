from pydantic import BaseModel


class DiplomatikException(Exception):
    def __init__(self, message: str, details: str = None):
        Exception.__init__(self)
        self.message = message
        self.details = details


class DataEngineException(DiplomatikException):
    def __init__(self, message: str = None, details: str = None):
        super().__init__(message=message, details=details)


class DataModelException(DiplomatikException):
    def __init__(self, message: str = None, details: str = None):
        super().__init__(message=message, details=details)
