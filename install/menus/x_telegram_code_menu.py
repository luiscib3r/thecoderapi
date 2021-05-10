from config import odoo

from core.odoorpc import OdooRPC

from core.models import Menu

from core.crud.menu import crud_create_menu, crud_search_menu, crud_delete_menu, crud_get_menu
from core.crud.action_window import crud_search_action_window

from core.utils import load_image


def install_x_telegram_code_menu():
    x_telegram_code_action = crud_search_action_window(
        odoo, [["name", "=", "Telegram Code"]])[0]

    x_thecoder_menu = crud_search_menu(odoo, [["name", "=", "TheCoder"]])[0]

    x_telegram_code_menu = Menu(
        name="Telegram Code",
        action=f"ir.actions.act_window,{x_telegram_code_action}",
        parent_id=x_thecoder_menu
    )

    crud_create_menu(odoo, x_telegram_code_menu)


def uninstall_x_telegram_code_menu():
    menu_id = crud_search_menu(
        odoo, [["name", "=", "Telegram Code"]])[0]

    crud_delete_menu(odoo, menu_id)
