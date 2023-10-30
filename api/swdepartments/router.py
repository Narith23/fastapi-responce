from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from helpers.resp import success_resp, error_resp, bad_resp, base_response
from .service import DepartmentService
from config.databases import get_session
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/sw/departments", tags=["SW Departments"])


@router.get('/')
def indix(page_num: int = 1, page_size: int = 5, db: Session = Depends(get_session)):
    data= DepartmentService.get_department(page_num, page_size, db)
    return success_resp(
        result=jsonable_encoder(data)
    )
