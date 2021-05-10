import sys
import os

sys.path.append(os.getcwd())

from install.models.x_telegram_user import uninstall_x_telegram_user
from install.actions.x_telegram_user_action import uninstall_x_telegram_user_action
from install.menus.thecoder_menu import uninstall_thecoder_menu
from install.menus.x_telegram_user_menu import uninstall_x_telegram_user_menu
from install.views.x_telegram_user_view import uninstall_x_telegram_user_view

uninstall_x_telegram_user_view()
uninstall_x_telegram_user_menu()
uninstall_thecoder_menu()
uninstall_x_telegram_user_action()
uninstall_x_telegram_user()
