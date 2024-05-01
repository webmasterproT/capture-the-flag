import pefile
import capstone
from external_tools.re_tools import Decompiler

def disassemble_binary(binary_path):
    """
    Disassemble a binary executable file using Capstone disassembler.
    
    :param binary_path: Path to the binary file to be disassembled
    :return: Disassembled code as a string
    """
    disassembled_code = ""
    try:
        pe = pefile.PE(binary_path)
        entry_point = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        data = pe.get_memory_mapped_image()[entry_point:]
        cs = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
        for i in cs.disasm(data, 0x1000):
            disassembled_code += "0x{0:x}:\t{1}\t{2}\n".format(i.address, i.mnemonic, i.op_str)
    except Exception as e:
        log_error(f"Error disassembling binary: {e}")
    return disassembled_code

def analyze_executable(executable_path):
    """
    Analyze an executable to understand its behavior by decompiling it to C code.
    
    :param executable_path: Path to the executable file to be analyzed
    :return: Decompiled C code as a string
    """
    decompiled_code = ""
    try:
        decompiler = Decompiler(executable_path)
        decompiled_code = decompiler.decompile()
    except Exception as e:
        log_error(f"Error analyzing executable: {e}")
    return decompiled_code

def log_error(message):
    """
    Log an error message to the system log.
    
    :param message: Error message to log
    """
    # Assuming log_action is a function from utils/logging_utils.py that logs actions
    from utils.logging_utils import log_action
    log_action(message, level="ERROR")

# Additional reverse engineering utilities can be added here as needed.