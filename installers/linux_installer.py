```python
#!/usr/bin/env python3
import os
import subprocess
import sys
from shutil import copyfile

def check_root():
    if os.geteuid() != 0:
        exit("You need to have root privileges to install this software. Please try running this script again with 'sudo'.")

def install_dependencies():
    print("Installing required system dependencies...")
    subprocess.check_call(['apt-get', 'update'])
    subprocess.check_call(['apt-get', 'install', '-y', 'python3', 'python3-pip'])

def copy_files():
    print("Copying files to the target directory...")
    target_dir = "/opt/red_team_toolkit"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    file_list = [
        "main.py",
        "config.py",
        "dashboard.py",
        "network_analysis.py",
        "forensics.py",
        "steganography.py",
        "reverse_engineering.py",
        "crypto.py",
        "osint.py",
        "exploit_development.py",
        "dynamic_code_exec.py",
        "polymorphic_code_gen.py",
        "incident_response.py",
        "threat_modeling.py",
        "risk_analysis.py",
        "ctf_simulation.py",
        "red_team_tools.py",
        "api_interaction.py",
        "user_interface/dashboard_ui.py",
        "user_interface/settings_ui.py",
        "user_interface/logging_ui.py",
        "utils/helpers.py",
        "utils/logging_utils.py",
        "utils/network_utils.py",
        "utils/forensic_utils.py",
        "utils/crypto_utils.py",
        "utils/osint_utils.py",
        "utils/reverse_engineering_utils.py",
        "utils/steganography_utils.py",
        "external_tools/debugging_tools.py",
        "external_tools/exploit_tools.py",
        "external_tools/forensic_tools.py",
        "external_tools/network_tools.py",
        "external_tools/re_tools.py",
        "external_tools/stego_tools.py",
        "data/payloads/__init__.py",
        "data/logs/__init__.py",
        "data/configurations/__init__.py",
    ]
    for file in file_list:
        copyfile(file, os.path.join(target_dir, file))
    print("Files copied successfully.")

def set_permissions():
    print("Setting file permissions...")
    target_dir = "/opt/red_team_toolkit"
    for root, dirs, files in os.walk(target_dir):
        for d in dirs:
            os.chmod(os.path.join(root, d), 0o755)
        for f in files:
            os.chmod(os.path.join(root, f), 0o644)
    print("Permissions set.")

def create_symlink():
    print("Creating symlink for easy execution...")
    os.symlink("/opt/red_team_toolkit/main.py", "/usr/local/bin/red_team_toolkit")
    print("Symlink created. You can run the program with 'red_team_toolkit' command.")

def main():
    check_root()
    install_dependencies()
    copy_files()
    set_permissions()
    create_symlink()
    print("Installation completed successfully.")

if __name__ == "__main__":
    main()
```