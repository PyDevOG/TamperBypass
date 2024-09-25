import subprocess
import os
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Error checking admin rights: {e}")
        return False


def run_system_command(command):
    try:
        print(f"Executing command: {command}")
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=True)
        print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\nReturn Code: {e.returncode}\nOutput: {e.stdout}\nError: {e.stderr}")
        return False


def enable_safe_mode():
    print("Enabling Safe Mode boot...")
    command = 'bcdedit /set {current} safeboot minimal'
    success = run_system_command(command)
    
    if success:
        print("Safe Mode enabled. Rebooting now...")

        run_system_command('shutdown /r /t 0')
    else:
        print("Failed to enable Safe Mode.")


def disable_defender_services():
    services = [
        "WinDefend", "Sense", "WdFilter", 
        "WdNisDrv", "WdNisSvc", "WdBoot"
    ]
    reg_path = "HKLM:\\SYSTEM\\CurrentControlSet\\Services"
    
   
    for service in services:
        command = f'Set-ItemProperty -Path "{reg_path}\\{service}" -Name Start -Value 4'
        run_system_command(f'powershell -Command "{command}"')
        
    print("Services disabled.")


def disable_defender_tasks():
    tasks = [
        "Windows Defender Cache Maintenance",
        "Windows Defender Cleanup",
        "Windows Defender Scheduled Scan",
        "Windows Defender Verification"
    ]
    
 
    for task in tasks:
        command = f'Get-ScheduledTask "{task}" | Disable-ScheduledTask'
        run_system_command(f'powershell -Command "{command}"')
    
    print("Scheduled tasks disabled.")


def disable_safe_mode():
    print("Disabling Safe Mode boot...")
    command = 'bcdedit /deletevalue {current} safeboot'
    success = run_system_command(command)
    
    if success:
        print("Safe Mode disabled. Rebooting to normal mode now...")
        # Reboot into normal mode
        run_system_command('shutdown /r /t 0')
    else:
        print("Failed to disable Safe Mode. Please manually check Safe Mode status.")


def is_safe_mode():
  
    try:
        result = subprocess.run(['bcdedit'], capture_output=True, text=True)
        return "safeboot" in result.stdout.lower()
    except Exception as e:
        print(f"Error checking Safe Mode status: {e}")
        return False


def ensure_safe_mode_disabled():
    print("Ensuring Safe Mode is disabled...")
    if is_safe_mode():
        print("Safe Mode is still enabled. Attempting to disable again...")
        disable_safe_mode()
    else:
        print("Safe Mode is already disabled.")


if __name__ == "__main__":
    if is_admin():
  
        if is_safe_mode():
            
            print("System is in Safe Mode.")
            disable_defender_services()
            disable_defender_tasks()
           
            disable_safe_mode()
        else:
      
            print("System is in Regular Mode. Switching to Safe Mode...")
            enable_safe_mode()
    else:
    
        print("Script is not running as Administrator. Elevating...")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"Failed to elevate script to administrator: {e}")
