from core.odoorpc import OdooRPC
from typing import List
from app.models import TelegramCode

MODEL_NAME = "x_telegram_code"


def crud_get_telegram_code(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20, change_id=True) -> List[TelegramCode]:
    telegram_code: List[TelegramCode] = []

    result = odoo.search_read(MODEL_NAME, domain, [], offset, limit)

    for row in result:
        if change_id:
            row["id"] = row["x_message_id"]

        telegram_code.append(TelegramCode(**row))

    return telegram_code


def crud_search_telegram_code(odoo: OdooRPC, domain: List = [], offset: int = 0, limit: int = 20) -> List[int]:
    result = odoo.search(MODEL_NAME, domain, offset, limit)

    return result


def crud_create_telegram_code(odoo: OdooRPC, telegram_code: TelegramCode) -> int:
    message = crud_get_telegram_code(
        odoo, [["x_message_id", "=", telegram_code.x_message_id]], change_id=False)

    if len(message) > 0:
        result = crud_update_telegram_code(
            odoo, message[0].x_message_id, telegram_code)
    else:
        result = odoo.create(MODEL_NAME, telegram_code.dict())

    return result


def crud_update_telegram_code(odoo: OdooRPC, message_id: int, telegram_code: TelegramCode) -> bool:
    result = odoo.write(MODEL_NAME, message_id, telegram_code.dict())

    return result


def crud_delete_telegram_code(odoo: OdooRPC, id: int) -> bool:
    result = odoo.unlink(MODEL_NAME, id)

    return result
