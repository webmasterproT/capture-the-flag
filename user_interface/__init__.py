# user_interface/__init__.py

from .dashboard_ui import DashboardUI
from .settings_ui import SettingsUI
from .logging_ui import LoggingUI

# Initialize the user interface components
def init_ui(api_key):
    dashboard = DashboardUI(api_key)
    settings = SettingsUI()
    logging = LoggingUI()

    return {
        'dashboard': dashboard,
        'settings': settings,
        'logging': logging
    }