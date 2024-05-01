```python
import gdb
from utils.logging_utils import log_action, log_error

class DebuggingTool:
    def __init__(self):
        self.gdb_interface = gdb.GdbInterface()

    def attach_to_process(self, pid):
        try:
            self.gdb_interface.attach(pid)
            log_action(f"Attached to process with PID: {pid}")
        except gdb.GdbError as e:
            log_error(f"Error attaching to process {pid}: {e}")

    def set_breakpoint(self, location):
        try:
            self.gdb_interface.breakpoint(location)
            log_action(f"Breakpoint set at: {location}")
        except gdb.GdbError as e:
            log_error(f"Error setting breakpoint at {location}: {e}")

    def run(self):
        try:
            self.gdb_interface.run()
            log_action("Debugger started")
        except gdb.GdbError as e:
            log_error(f"Error starting debugger: {e}")

    def continue_execution(self):
        try:
            self.gdb_interface.continue_execution()
            log_action("Continued execution")
        except gdb.GdbError as e:
            log_error("Error continuing execution: {e}")

    def step_instruction(self):
        try:
            self.gdb_interface.step_instruction()
            log_action("Stepped one instruction")
        except gdb.GdbError as e:
            log_error("Error stepping instruction: {e}")

    def get_register_value(self, register):
        try:
            value = self.gdb_interface.get_register(register)
            log_action(f"Value of register {register}: {value}")
            return value
        except gdb.GdbError as e:
            log_error(f"Error getting value of register {register}: {e}")
            return None

    def read_memory(self, address, length):
        try:
            memory_contents = self.gdb_interface.read_memory(address, length)
            log_action(f"Memory contents at {address}: {memory_contents}")
            return memory_contents
        except gdb.GdbError as e:
            log_error(f"Error reading memory at {address}: {e}")
            return None

    def write_memory(self, address, data):
        try:
            self.gdb_interface.write_memory(address, data)
            log_action(f"Memory at {address} modified")
        except gdb.GdbError as e:
            log_error(f"Error writing to memory at {address}: {e}")

    def detach(self):
        try:
            self.gdb_interface.detach()
            log_action("Detached from process")
        except gdb.GdbError as e:
            log_error("Error detaching from process: {e}")

# Example usage:
# debugger = DebuggingTool()
# debugger.attach_to_process(1234)
# debugger.set_breakpoint("0x400123")
# debugger.run()
# register_value = debugger.get_register_value("eax")
# memory_contents = debugger.read_memory("0x601048", 4)
# debugger.write_memory("0x601048", b"\x90\x90\x90\x90")
# debugger.detach()
```

Please note that this code assumes the existence of a `gdb.GdbInterface` class which is a wrapper around the actual GDB Python API. The `utils.logging_utils` module is expected to contain the logging functions used in this script. The example usage at the bottom is commented out and should be used as a guide on how to use the `DebuggingTool` class.