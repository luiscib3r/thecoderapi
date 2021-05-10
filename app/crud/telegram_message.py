from core.odoorpc import OdooRPC
from typing import List
from app.models import TelegramMessage

MODEL_NAME = "x_telegram_message"


def crud_get_telegram_message(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20, change_id=True) -> List[TelegramMessage]:
    telegram_message: List[TelegramMessage] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        if change_id:
            row["id"] = row["x_message_id"]

        telegram_message.append(TelegramMessage(**row))

    return telegram_message


def crud_search_telegram_message(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_telegram_message(odoo: OdooRPC, telegram_message: TelegramMessage) -> int:
    message = crud_get_telegram_message(
        odoo, [["x_message_id", "=", telegram_message.x_message_id]], change_id=False)

    if len(message) > 0:
        result = crud_update_telegram_message(
            odoo, message[0].x_message_id, telegram_message)
    else:
        result = odoo.create(MODEL_NAME, telegram_message.dict())

    return result


def crud_update_telegram_message(odoo: OdooRPC, message_id: int, telegram_message: TelegramMessage) -> bool:
    result = odoo.write(MODEL_NAME, message_id, telegram_message.dict())

    return result


def crud_delete_telegram_message(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
