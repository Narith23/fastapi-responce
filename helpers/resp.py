from typing import Union, Optional
from fastapi import status
from fastapi.responses import JSONResponse


def base_response(status_code: Union[int, None] = status.HTTP_200_OK, content: Union[any, None] = "OK"):
    return JSONResponse(
        status_code=status_code,
        content=content
    )


def success_resp(message: Union[str, None] = "OK", result: Optional[object | None] = None):
    return base_response(
        status_code=status.HTTP_200_OK,
        content={
            "status_code": status.HTTP_200_OK,
            "message": message,
            "result": result
        }
    )


def created_resp(message: Union[str, None] = "Created", result: Union[any, None] = None):
    return base_response(
        status_code=status.HTTP_201_CREATED,
        content={
            "status_code": status.HTTP_201_CREATED,
            "message": message,
            "result": result
        }
    )


def updated_resp(message: Union[str, None] = "Updated", result: Union[any, None] = None):
    return base_response(
        status_code=status.HTTP_202_ACCEPTED,
        content={
            "status_code": status.HTTP_202_ACCEPTED,
            "message": message,
            "result": result
        }
    )


def deleted_resp(message: Union[str, None] = "Deleted", result: Union[any, None] = None):
    return base_response(
        status_code=status.HTTP_204_NO_CONTENT,
        content={
            "status_code": status.HTTP_204_NO_CONTENT,
            "message": message,
            "result": result
        }
    )


def error_resp(message: Union[str, None] = "Something went wrong!"):
    return base_response(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": message,
            "result": None
        }
    )


def bad_resp(message: Union[str, None] = "Bad Request"):
    return base_response(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": message,
            "result": None
        }
    )


def unprocessable_resp(message: Union[str, None] = "Unprocessable", result: Union[any, None] = None):
    return base_response(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": message,
            "result": result
        }
    )


def not_found_resp(message: Union[str, None] = "not found", result: Union[any, None] = None):
    return base_response(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": message,
            "result": result
        }
    )
