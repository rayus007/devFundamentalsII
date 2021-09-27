from truck_delivery_rayus007.util.custom_exceptions import CustomException


def error_handler(message, status_code):
    # this should be done as we should many ifs
    if status_code == 200:
        return
    elif status_code == 404:
        if "not found" in message:
            return CustomException
    elif status_code == 500:
        return