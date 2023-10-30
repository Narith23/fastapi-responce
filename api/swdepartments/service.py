from fastapi import status
from sqlmodel import Session
from .model import Department
from typing import Any
from helpers.pagination import paginate


class DepartmentService:
    @staticmethod
    def get_department(page_num: int, page_size: int, db: Session):
        query = db.query(Department).order_by(Department.departmentid.desc())
        data = paginate(query=query, page=page_num, page_size=page_size, db=db, model=Department, condition="swdepartments")
        return data
