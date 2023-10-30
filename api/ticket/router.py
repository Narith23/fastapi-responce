from fastapi import APIRouter, Depends
from helpers.resp import success_resp
# from helpers.parent_api import data_table
from .service import TicketService
from sqlmodel import Session
from config.databases import get_session
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix='/api/ticket', tags=['Ticket'])


@router.get('/')
def indix(page_num: int = 1, page_size: int = 5, db: Session = Depends(get_session)):
    data= TicketService.get_tickets(page_num, page_size,db)
    return success_resp(
        result=jsonable_encoder(data)
    )
