from fastapi import status
from helpers.pagination import paginate
from sqlmodel import Session
from .model import Tickets


class TicketService:
    @staticmethod
    def get_tickets(page_num: int, page_size: int, db: Session):
        query = db.query(Tickets).order_by(Tickets.ticketid.desc())
        data = paginate(query=query, page=page_num, page_size=page_size, db=db, model=Tickets, condition="swtickets")
        return data
