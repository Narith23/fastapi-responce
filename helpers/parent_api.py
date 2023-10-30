from typing import Union
from helpers.resp import success_resp, error_resp


def data_table(message: Union[str, None] = "OK", result: Union[any, None] = None):
    try:
        print(message)
    except:
        return error_resp()

    return success_resp(
        message=message,
        result=result
    )
