from fastapi import APIRouter
from app.api.v1.endpoints.telegram_user import router as telegram_user_route
from app.api.v1.endpoints.telegram_message import router as telegram_message_route

router = APIRouter(prefix="/v1")

router.include_router(telegram_user_route)
router.include_router(telegram_message_route)
