import sys
import os

sys.path.append(os.getcwd())

from install.models.x_telegram_code import install_x_telegram_code
from install.actions.x_telegram_code_action import install_x_telegram_code_action
from install.menus.x_telegram_code_menu import install_x_telegram_code_menu
from install.views.x_telegram_code_view import install_x_telegram_code_view

install_x_telegram_code()
install_x_telegram_code_action()
install_x_telegram_code_menu()
install_x_telegram_code_view()