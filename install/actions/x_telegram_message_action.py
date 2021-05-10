from config import odoo

from core.odoorpc import OdooRPC

from core.models import ActionWindow

from core.crud.action_window import crud_create_action_window, crud_search_action_window, crud_delete_action_window


def install_x_telegram_message_action():
    x_telegram_message_action = ActionWindow(
        name="Telegram Messages",
        res_model="x_telegram_message"
    )

    crud_create_action_window(odoo, x_telegram_message_action)


def uninstall_x_telegram_message_action():
    action_id = crud_search_action_window(
        odoo, [["name", "=", "Telegram Messages"]])[0]

    crud_delete_action_window(odoo, action_id)
