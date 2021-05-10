import sys
import os

sys.path.append(os.getcwd())

from install.views.x_telegram_code_view import uninstall_x_telegram_code_view
from install.menus.x_telegram_code_menu import uninstall_x_telegram_code_menu
from install.actions.x_telegram_code_action import uninstall_x_telegram_code_action
from install.models.x_telegram_code import uninstall_x_telegram_code

uninstall_x_telegram_code_view()
uninstall_x_telegram_code_menu()
uninstall_x_telegram_code_action()
uninstall_x_telegram_code()
