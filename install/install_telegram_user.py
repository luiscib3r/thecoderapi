import sys
import os

sys.path.append(os.getcwd())

from install.models.x_telegram_user import install_x_telegram_user
from install.actions.x_telegram_user_action import install_x_telegram_user_action
from install.menus.thecoder_menu import install_thecoder_menu
from install.menus.x_telegram_user_menu import install_x_telegram_user_menu
from install.views.x_telegram_user_view import install_x_telegram_user_view

install_x_telegram_user()
install_x_telegram_user_action()
install_thecoder_menu()
install_x_telegram_user_menu()
install_x_telegram_user_view()