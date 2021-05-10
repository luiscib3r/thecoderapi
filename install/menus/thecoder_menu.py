from config import odoo

from core.odoorpc import OdooRPC

from core.models import Menu

from core.crud.menu import crud_create_menu, crud_search_menu, crud_delete_menu, crud_get_menu
from core.crud.action_window import crud_search_action_window

from core.utils import load_image


def install_thecoder_menu():
    x_telegram_user_action = crud_search_action_window(
        odoo, [["name", "=", "Telegram Users"]])[0]

    image = load_image("assets/logo_fastapi.png")

    thecoder_menu = Menu(
        name="TheCoder",
        web_icon_data=image,
        action=f"ir.actions.act_window,{x_telegram_user_action}"
    )

    crud_create_menu(odoo, thecoder_menu)


def uninstall_thecoder_menu():
    menu_id = crud_search_menu(
        odoo, [["name", "=", "TheCoder"]])[0]

    crud_delete_menu(odoo, menu_id)
