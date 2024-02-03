from app.utils.errors.GException import GException


class MaxTravellersReachedException(GException):
    message = "This travel can't contain more people"
    code = 400