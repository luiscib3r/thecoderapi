import sys
import os

sys.path.append(os.getcwd())

from install.views.x_telegram_message_view import uninstall_x_telegram_message_view
from install.menus.x_telegram_message_menu import uninstall_x_telegram_message_menu
from install.actions.x_telegram_message_action import uninstall_x_telegram_message_action
from install.models.x_telegram_message import uninstall_x_telegram_message

uninstall_x_telegram_message_view()
uninstall_x_telegram_message_menu()
uninstall_x_telegram_message_action()
uninstall_x_telegram_message()
