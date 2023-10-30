from fastapi import FastAPI

from config.config import APP_TITLE, APP_DESCRIPTION, APP_VERSION
from helpers.resp import success_resp, created_resp, updated_resp, deleted_resp
from router.router import router as base_route
app = FastAPI(
    title=f"{APP_TITLE}",
    description=f"{APP_DESCRIPTION}",
    version=f"{APP_VERSION}"
)
from fastapi_pagination import Page, add_pagination, paginate

add_pagination(app)

app.include_router(base_route)

data = [{
    "id": "1",
    "title": "Open",
    "displayorder": "1",
    "departmentid": "0",
    "displayicon": "{$themepath}icon_ticketstatusopen.png",
    "type": "public",
    "displayinmainlist": "0",
    "markasresolved": "0",
    "displaycount": "1",
    "statuscolor": "#4eafcb",
    "statusbgcolor": "#4eafcb",
    "resetduetime": "0",
    "triggersurvey": "0",
    "staffvisibilitycustom": "0"
},
    {
        "id": "3",
        "title": "Closed",
        "display-order": "3",
        "departmentid": "0",
        "displayicon": "{$themepath}icon_ticketstatusclosed.png",
        "type": "public",
        "displayinmainlist": "0",
        "markasresolved": "1",
        "displaycount": "0",
        "statuscolor": "#36a148",
        "statusbgcolor": "#36a148",
        "resetduetime": "0",
        "triggersurvey": "1",
        "staffvisibilitycustom": "0"
    },
    {
        "id": "5",
        "title": "Pending",
        "displayorder": "3",
        "departmentid": "0",
        "displayicon": "null",
        "type": "private",
        "displayinmainlist": "0",
        "markasresolved": "0",
        "displaycount": "1",
        "statuscolor": "#5757ff",
        "statusbgcolor": "#5757ff",
        "resetduetime": "0",
        "triggersurvey": "0",
        "staffvisibilitycustom": "0"
    }]


@app.get('/list')
async def list_items():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~", type(data))
    return success_resp(
        message="Successful",
        result=data
    )


@app.post('/create')
async def create_items():
    return created_resp(
        result=""
    )


@app.put('/update')
async def update_items():
    return updated_resp(
        result=""
    )


@app.delete('/delete')
async def delete_items():
    return deleted_resp(
        result=""
    )


@app.get('/')
def root():
    return {"status": "Running!"}
