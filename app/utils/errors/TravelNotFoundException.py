from app.utils.errors.GException import GException


class TravelNotFoundException(GException):
    message = "This travel doesn't exist"
    code = 404