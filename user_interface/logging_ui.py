```python
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

class LoggingUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Activity Log")
        
        # Create the logging area
        self.log_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=100, height=30)
        self.log_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create the clear log button
        self.clear_button = tk.Button(master, text="Clear Log", command=self.clear_log)
        self.clear_button.pack(side=tk.BOTTOM, pady=5)
        
        # Initialize the log area
        self.log_info("Logging UI initialized.")

    def log_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[ACTION] {timestamp}: {action}\n"
        self.log_area.insert(tk.END, log_entry)
        self.log_area.see(tk.END)

    def log_error(self, error):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[ERROR] {timestamp}: {error}\n"
        self.log_area.insert(tk.END, log_entry)
        self.log_area.see(tk.END)

    def log_info(self, info):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[INFO] {timestamp}: {info}\n"
        self.log_area.insert(tk.END, log_entry)
        self.log_area.see(tk.END)

    def clear_log(self):
        self.log_area.delete(1.0, tk.END)
        self.log_info("Log cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    logging_ui = LoggingUI(root)
    root.mainloop()
```