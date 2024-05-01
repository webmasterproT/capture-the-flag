# data/logs/__init__.py

from .log_schema import LogSchema

class LogManager:
    def __init__(self):
        self.logs = []

    def log_action(self, action, description, level='INFO'):
        log_entry = LogSchema(action=action, description=description, level=level)
        self.logs.append(log_entry)
        self.save_log(log_entry)

    def log_error(self, error, description):
        self.log_action(action='ERROR', description=description, level='ERROR')

    def log_info(self, info, description):
        self.log_action(action='INFO', description=description, level='INFO')

    def save_log(self, log_entry):
        # Implement the logic to save the log entry to a persistent storage
        # This could be a file, database, or any other form of storage
        pass

    def retrieve_logs(self):
        # Implement the logic to retrieve logs from the persistent storage
        return self.logs

# Initialize the LogManager instance for use across the application
log_manager = LogManager()