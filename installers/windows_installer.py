import os
import subprocess
import sys
from zipfile import ZipFile

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        required_packages = [
            'requests', 'pycryptodome', 'scapy', 'beautifulsoup4', 'lxml',
            'python-nmap', 'paramiko', 'cryptography', 'stegano', 'ghidra',
            'capstone', 'pwntools', 'binwalk'
        ]
        for package in required_packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")
        sys.exit(1)

def create_directories():
    directories = [
        'user_interface', 'utils', 'external_tools', 'data/payloads',
        'data/logs', 'data/configurations', 'documentation', 'tests'
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("All necessary directories created.")

def extract_payloads():
    with ZipFile('data/payloads/payloads.zip', 'r') as zip_ref:
        zip_ref.extractall('data/payloads/')
    print("Payloads extracted.")

def create_configuration_file(api_key):
    with open('data/configurations/config.py', 'w') as config_file:
        config_file.write(f"api_key = '{api_key}'\n")
    print("Configuration file created.")

def main():
    print("Starting installation process for Windows...")
    api_key = input("Please enter your API key: ")
    install_dependencies()
    create_directories()
    extract_payloads()
    create_configuration_file(api_key)
    print("Installation completed successfully.")

if __name__ == "__main__":
    main()