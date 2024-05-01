import subprocess
import os
from utils.reverse_engineering_utils import disassemble_binary, analyze_executable
from utils.logging_utils import log_action, log_error
from external_tools.re_tools import Decompiler, InteractiveDebugger

class ReverseEngineering:
    def __init__(self, api_key):
        self.api_key = api_key
        self.decompiler = Decompiler()
        self.debugger = InteractiveDebugger()

    def analyze_binary(self, binary_path):
        try:
            log_action(f"Analyzing binary: {binary_path}")
            disassembly = disassemble_binary(binary_path)
            decompiled_code = self.decompiler.decompile(binary_path)
            return disassembly, decompiled_code
        except Exception as e:
            log_error(f"Error analyzing binary: {e}")
            return None, None

    def debug_executable(self, executable_path, breakpoints):
        try:
            log_action(f"Debugging executable: {executable_path}")
            self.debugger.load_executable(executable_path)
            for bp in breakpoints:
                self.debugger.set_breakpoint(bp)
            self.debugger.start_debugging()
            return self.debugger.get_debugging_info()
        except Exception as e:
            log_error(f"Error debugging executable: {e}")
            return None

    def extract_sensitive_info(self, binary_path):
        try:
            log_action(f"Extracting sensitive info from binary: {binary_path}")
            _, decompiled_code = self.analyze_binary(binary_path)
            sensitive_info = analyze_executable(decompiled_code)
            return sensitive_info
        except Exception as e:
            log_error(f"Error extracting sensitive info: {e}")
            return None

    def run_static_analysis(self, binary_path):
        try:
            log_action(f"Running static analysis on binary: {binary_path}")
            static_analysis_results = subprocess.run(["radare2", "-A", binary_path], capture_output=True, text=True)
            return static_analysis_results.stdout
        except Exception as e:
            log_error(f"Error running static analysis: {e}")
            return None

# Example usage
if __name__ == "__main__":
    api_key = os.getenv("REVERSE_ENGINEERING_API_KEY")
    re_tool = ReverseEngineering(api_key)
    binary_to_analyze = "/path/to/binary"
    disassembly, decompiled_code = re_tool.analyze_binary(binary_to_analyze)
    debugging_info = re_tool.debug_executable(binary_to_analyze, [0x00401000])
    sensitive_info = re_tool.extract_sensitive_info(binary_to_analyze)
    static_analysis_output = re_tool.run_static_analysis(binary_to_analyze)

    # Log results
    if disassembly and decompiled_code:
        log_action("Binary analysis completed successfully.")
    if debugging_info:
        log_action("Executable debugging completed successfully.")
    if sensitive_info:
        log_action("Sensitive information extraction completed successfully.")
    if static_analysis_output:
        log_action("Static analysis completed successfully.")