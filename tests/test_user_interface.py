import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication
from user_interface.dashboard_ui import DashboardUI
from user_interface.settings_ui import SettingsUI
from user_interface.logging_ui import LoggingUI

app = QApplication([])

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.dashboard_ui = DashboardUI()
        self.settings_ui = SettingsUI()
        self.logging_ui = LoggingUI()

    def test_dashboard_ui_elements(self):
        self.assertIsNotNone(self.dashboard_ui.layout())
        self.assertIsNotNone(self.dashboard_ui.findChild(QPushButton, 'settings_button'))
        self.assertIsNotNone(self.dashboard_ui.findChild(QTextEdit, 'log_area'))

    def test_settings_ui_elements(self):
        self.assertIsNotNone(self.settings_ui.layout())
        self.assertIsNotNone(self.settings_ui.findChild(QLineEdit, 'api_key_input'))

    def test_logging_ui_elements(self):
        self.assertIsNotNone(self.logging_ui.layout())
        self.assertIsNotNone(self.logging_ui.findChild(QTextEdit, 'log_display_area'))

    @patch('user_interface.dashboard_ui.DashboardUI.update_ui')
    def test_dashboard_update_ui_called(self, mock_update_ui):
        self.dashboard_ui.update_ui()
        mock_update_ui.assert_called_once()

    @patch('user_interface.logging_ui.LoggingUI.log_action')
    def test_logging_ui_log_action_called(self, mock_log_action):
        test_message = "Test log action"
        self.logging_ui.log_action(test_message)
        mock_log_action.assert_called_with(test_message)

    @patch('user_interface.settings_ui.SettingsUI.save_settings')
    def test_settings_ui_save_settings_called(self, mock_save_settings):
        self.settings_ui.save_settings()
        mock_save_settings.assert_called_once()

if __name__ == '__main__':
    unittest.main()