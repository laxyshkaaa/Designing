import datetime


def create_error(message, error_code):
    return {
        "message" : message,
        "error_code" : error_code,
        "timestamp" : datetime.datetime.now().timestamp()
    }