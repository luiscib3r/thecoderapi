from fastapi import APIRouter, Query, Depends
from fastapi.security.api_key import APIKey
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from typing import List

from config import odoo
from core.errors import OdooException
from app.crud.telegram_message import crud_get_telegram_message, crud_create_telegram_message
from app.models import TelegramMessage
from app.auth.api_key import get_api_key


router = APIRouter(prefix="/telegram_message", tags=["Telegram messages"])


@router.get("/", response_model=List[TelegramMessage])
async def get_telegram_message(
    api_key: APIKey = Depends(get_api_key),
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_telegram_message(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/")
async def create_telegram_message(
    message: TelegramMessage,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        return crud_create_telegram_message(odoo, message)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )

@router.get("/{id}", response_model=TelegramMessage)
async def get_telegram_message_by_id(
    id: str,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        result = crud_get_telegram_message(odoo, [["x_message_id", "=", id]])

        if len(result) > 0:
            return result[0]
        else:
            raise HTTPException(status_code=404, detail=f"message by id {id}, not found")
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
