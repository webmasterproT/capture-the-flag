```python
import tkinter as tk
from tkinter import messagebox
from config import config_schema, api_key

class SettingsUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Settings")
        self.create_widgets()

    def create_widgets(self):
        # API Key Configuration
        self.api_key_label = tk.Label(self.master, text="API Key:")
        self.api_key_label.grid(row=0, column=0, sticky="w")

        self.api_key_entry = tk.Entry(self.master)
        self.api_key_entry.insert(0, api_key)
        self.api_key_entry.grid(row=0, column=1, sticky="ew")

        # Save Button
        self.save_button = tk.Button(self.master, text="Save", command=self.save_settings)
        self.save_button.grid(row=1, column=1, sticky="ew")

        # Cancel Button
        self.cancel_button = tk.Button(self.master, text="Cancel", command=self.master.destroy)
        self.cancel_button.grid(row=1, column=0, sticky="ew")

        # Adjust column weights so they expand properly
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def save_settings(self):
        # Validate and save the API key
        new_api_key = self.api_key_entry.get()
        if self.validate_api_key(new_api_key):
            config_schema['api_key'] = new_api_key
            self.update_api_key(new_api_key)
            messagebox.showinfo("Settings", "Settings have been saved successfully.")
            self.master.destroy()
        else:
            messagebox.showerror("Settings", "Invalid API key.")

    @staticmethod
    def validate_api_key(key):
        # Placeholder for actual API key validation logic
        return len(key) > 0

    @staticmethod
    def update_api_key(key):
        # Placeholder for the method to update the API key in the configuration
        with open('data/configurations/api_key.txt', 'w') as file:
            file.write(key)

def main():
    root = tk.Tk()
    app = SettingsUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```