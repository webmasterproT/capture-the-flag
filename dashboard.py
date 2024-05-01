```python
import tkinter as tk
from tkinter import messagebox
from config import api_key
from utils.logging_utils import log_action, log_error
from api_interaction import send_api_request, receive_api_response

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Government Security Operations Dashboard")
        self.create_widgets()

    def create_widgets(self):
        # Dashboard Frame
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack(pady=10)

        # API Key Entry
        self.api_key_label = tk.Label(self.dashboard_frame, text="API Key:")
        self.api_key_label.grid(row=0, column=0, sticky="e")
        self.api_key_entry = tk.Entry(self.dashboard_frame, width=50)
        self.api_key_entry.grid(row=0, column=1)
        self.api_key_entry.insert(0, api_key)

        # Action Log Area
        self.log_label = tk.Label(self.dashboard_frame, text="Action Log:")
        self.log_label.grid(row=1, column=0, sticky="nw")
        self.log_text = tk.Text(self.dashboard_frame, height=15, width=70)
        self.log_text.grid(row=1, column=1)

        # Buttons
        self.update_button = tk.Button(self.dashboard_frame, text="Update API Key", command=self.update_api_key)
        self.update_button.grid(row=2, column=1, sticky="ew")
        self.execute_button = tk.Button(self.dashboard_frame, text="Execute Command", command=self.execute_command)
        self.execute_button.grid(row=3, column=1, sticky="ew")

    def update_api_key(self):
        new_api_key = self.api_key_entry.get()
        if new_api_key:
            global api_key
            api_key = new_api_key
            log_action(f"API Key updated to: {api_key}")
            self.log_text.insert(tk.END, f"API Key updated successfully.\n")
        else:
            log_error("API Key update failed. Entry was empty.")
            messagebox.showerror("Error", "API Key cannot be empty.")

    def execute_command(self):
        command = self.command_entry.get()
        if command:
            response = send_api_request(api_key, command)
            result = receive_api_response(response)
            self.log_text.insert(tk.END, f"Executed command: {command}\nResult: {result}\n")
            log_action(f"Executed command: {command}")
        else:
            log_error("Command execution failed. Entry was empty.")
            messagebox.showerror("Error", "Command cannot be empty.")

    def log_action(self, message):
        self.log_text.insert(tk.END, f"{message}\n")

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()
```