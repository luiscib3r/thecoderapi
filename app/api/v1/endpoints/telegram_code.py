from fastapi import APIRouter, Query, Depends
from fastapi.security.api_key import APIKey
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from typing import List

from config import odoo
from core.errors import OdooException
from app.crud.telegram_code import crud_get_telegram_code, crud_create_telegram_code
from app.models import TelegramCode
from app.auth.api_key import get_api_key


router = APIRouter(prefix="/telegram_code", tags=["Telegram Code"])


@router.get("/", response_model=List[TelegramCode])
async def get_telegram_code(
    api_key: APIKey = Depends(get_api_key),
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_telegram_code(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/")
async def create_telegram_code(
    message: TelegramCode,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        return crud_create_telegram_code(odoo, message)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.get("/{id}", response_model=TelegramCode)
async def get_telegram_code_by_id(
    id: str,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        result = crud_get_telegram_code(odoo, [["x_message_id", "=", id]])

        if len(result) > 0:
            return result[0]
        else:
            raise HTTPException(
                status_code=404, detail=f"message by id {id}, not found")
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
