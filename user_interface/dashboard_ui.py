from tkinter import Tk, Frame, Button, Text, Scrollbar, Label, Entry, END
import threading
import queue
from config import api_key
from utils.logging_utils import log_action, log_error, log_info
from api_interaction import send_api_request, receive_api_response

class DashboardUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Red Team Operations Dashboard")
        self.queue = queue.Queue()
        self.create_widgets()
        self.start_polling()

    def create_widgets(self):
        self.main_frame = Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        self.api_key_label = Label(self.main_frame, text="API Key:")
        self.api_key_label.grid(row=0, column=0, sticky='w')

        self.api_key_entry = Entry(self.main_frame, width=50)
        self.api_key_entry.grid(row=0, column=1, sticky='w')
        self.api_key_entry.insert(0, api_key)

        self.update_api_key_button = Button(self.main_frame, text="Update API Key", command=self.update_api_key)
        self.update_api_key_button.grid(row=0, column=2, padx=5)

        self.log_area = Text(self.main_frame, height=20, width=80)
        self.log_scroll = Scrollbar(self.main_frame, command=self.log_area.yview)
        self.log_area.configure(yscrollcommand=self.log_scroll.set)
        self.log_area.grid(row=1, column=0, columnspan=3)
        self.log_scroll.grid(row=1, column=3, sticky='nsew')

        self.action_button = Button(self.main_frame, text="Execute Action", command=self.execute_action)
        self.action_button.grid(row=2, column=0, pady=5)

    def update_api_key(self):
        new_api_key = self.api_key_entry.get()
        if new_api_key:
            global api_key
            api_key = new_api_key
            log_info("API Key updated successfully.")
        else:
            log_error("API Key cannot be empty.")

    def execute_action(self):
        # Placeholder for action execution logic
        log_info("Executing action...")
        # This is where you would add the code to trigger the AI-driven operations
        # For example, sending a request to the AI API using the updated api_key
        # and processing the response to perform the necessary actions.
        # This could be implemented as a separate thread to keep the UI responsive.
        threading.Thread(target=self.perform_ai_action).start()

    def perform_ai_action(self):
        # Placeholder for AI action logic
        # This function would interact with the AI API and perform actions based on the response
        response = send_api_request(api_key, "action details")
        result = receive_api_response(response)
        self.queue.put(result)

    def start_polling(self):
        self.poll_queue()

    def poll_queue(self):
        while not self.queue.empty():
            message = self.queue.get()
            self.log_area.insert(END, f"{message}\n")
        self.master.after(100, self.poll_queue)

    def log_message(self, message):
        self.log_area.insert(END, f"{message}\n")
        log_action(message)

if __name__ == "__main__":
    root = Tk()
    app = DashboardUI(root)
    root.mainloop()