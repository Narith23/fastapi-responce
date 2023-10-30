from sqlmodel import SQLModel, Field


class Department(SQLModel, table=True):
    __tablename__ = 'swdepartments'

    departmentid: int = Field(default=None, primary_key=True)
    title: str
    departmenttype: str
    departmentapp: str
    isdefault: int
    displayorder: int
    parentdepartmentid: int
    uservisibilitycustom: int
