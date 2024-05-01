```python
import sys
import threading
from dashboard import Dashboard
from config import load_configuration, save_configuration
from api_interaction import APIInteraction
from dynamic_code_exec import execute_dynamic_code
from polymorphic_code_gen import generate_polymorphic_code
from utils.helpers import log_action
from utils.network_utils import monitor_network
from utils.forensic_utils import perform_forensics
from utils.crypto_utils import solve_cipher
from utils.osint_utils import gather_intelligence
from utils.reverse_engineering_utils import analyze_executable
from utils.steganography_utils import hide_message, reveal_message

class RedTeamAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.dashboard = Dashboard()
        self.api_interaction = APIInteraction(api_key)
        self.config = load_configuration()
        self.running = True

    def start(self):
        threading.Thread(target=self.dashboard.run).start()
        log_action("RedTeamAI started.")
        self.perform_tasks()

    def perform_tasks(self):
        while self.running:
            task = self.dashboard.get_next_task()
            if task:
                self.handle_task(task)

    def handle_task(self, task):
        try:
            if task['type'] == 'dynamic_code_execution':
                code = generate_polymorphic_code(task['code'])
                execute_dynamic_code(code)
            elif task['type'] == 'network_monitoring':
                monitor_network()
            elif task['type'] == 'forensics':
                perform_forensics(task['target'])
            elif task['type'] == 'cryptography':
                solve_cipher(task['cipher'])
            elif task['type'] == 'osint':
                gather_intelligence(task['target'])
            elif task['type'] == 'reverse_engineering':
                analyze_executable(task['binary'])
            elif task['type'] == 'steganography':
                if task['action'] == 'hide':
                    hide_message(task['message'], task['carrier'])
                elif task['action'] == 'reveal':
                    reveal_message(task['carrier'])
            log_action(f"Task {task['type']} completed.")
        except Exception as e:
            log_action(f"Error handling task {task['type']}: {str(e)}")

    def stop(self):
        self.running = False
        save_configuration(self.config)
        log_action("RedTeamAI stopped.")
        sys.exit(0)

if __name__ == "__main__":
    api_key = input("Enter your API key: ")
    red_team_ai = RedTeamAI(api_key)
    try:
        red_team_ai.start()
    except KeyboardInterrupt:
        red_team_ai.stop()
```