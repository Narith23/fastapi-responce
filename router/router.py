from fastapi import APIRouter
from api.ticket.router import router as ticket_router
from api.swdepartments.router import router as sw_departments_router


router = APIRouter()


router.include_router(ticket_router)
router.include_router(sw_departments_router)
