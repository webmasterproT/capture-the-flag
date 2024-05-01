```python
import subprocess
import os
from utils.reverse_engineering_utils import disassemble_binary, analyze_executable
from utils.logging_utils import log_action, log_error

class ReverseEngineeringTool:
    def __init__(self, binary_path):
        self.binary_path = binary_path
        self.decompiler_path = '/path/to/decompiler'  # Path to the decompiler tool
        self.disassembler_path = '/path/to/disassembler'  # Path to the disassembler tool

    def decompile_binary(self):
        try:
            decompile_command = [self.decompiler_path, self.binary_path]
            decompile_result = subprocess.run(decompile_command, capture_output=True, text=True)
            if decompile_result.returncode != 0:
                log_error(f"Decompilation failed: {decompile_result.stderr}")
                return None
            log_action(f"Binary decompiled successfully: {self.binary_path}")
            return decompile_result.stdout
        except Exception as e:
            log_error(f"Error during decompilation: {str(e)}")
            return None

    def disassemble_binary(self):
        try:
            return disassemble_binary(self.binary_path)
        except Exception as e:
            log_error(f"Error during disassembly: {str(e)}")
            return None

    def analyze_binary(self):
        try:
            return analyze_executable(self.binary_path)
        except Exception as e:
            log_error(f"Error during binary analysis: {str(e)}")
            return None

    def run_debugger(self, commands):
        try:
            gdb_command = ['gdb', self.binary_path, '-ex', ' '.join(commands)]
            gdb_result = subprocess.run(gdb_command, capture_output=True, text=True)
            if gdb_result.returncode != 0:
                log_error(f"Debugging failed: {gdb_result.stderr}")
                return None
            log_action(f"Debugging completed successfully: {self.binary_path}")
            return gdb_result.stdout
        except Exception as e:
            log_error(f"Error during debugging: {str(e)}")
            return None

# Example usage:
# re_tool = ReverseEngineeringTool('/path/to/binary')
# decompiled_code = re_tool.decompile_binary()
# disassembled_code = re_tool.disassemble_binary()
# analysis_results = re_tool.analyze_binary()
# debugging_output = re_tool.run_debugger(['break main', 'run', 'info registers'])
```