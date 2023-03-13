from rest_framework import status
from rest_framework.exceptions import APIException


class BaseCustomException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code


class UserBlockedException(BaseCustomException):

    def __init__(self, detail):
        detail = "User is blocked to borrow a book."
        super().__init__(detail, status.HTTP_403_FORBIDDEN)


class LoanBookAlreadyExistsException(BaseCustomException):

    def __init__(self):
        detail = "User already borrow a copy of this book but not returned yet."
        super().__init__(detail, status.HTTP_409_CONFLICT)


class BookCopyNotAvailableException(BaseCustomException):

    def __init__(self):
        detail = "There isn't copies available to loan."
        super().__init__(detail, status.HTTP_404_NOT_FOUND)
        