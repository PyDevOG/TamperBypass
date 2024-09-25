## Project: Windows Safe Mode & Defender Automation Script ##
# Description
This Python script allows users to automate the process of enabling and disabling Windows Safe Mode, as well as managing Windows Defender services and scheduled tasks. It checks if the script is running with administrator privileges, switches between Safe Mode and Regular Mode, and optionally disables Windows Defender services and tasks while in Safe Mode.

This can be useful for system administrators or advanced users who need to manage Windows boot modes and Defender settings in a programmatic way.

# Features
Enable/Disable Safe Mode: Switch the system to Safe Mode or back to Regular Mode by manipulating the boot configuration.
Disable Windows Defender Services: Stop key Windows Defender services when Safe Mode is active.
Disable Windows Defender Scheduled Tasks: Disable scheduled tasks related to Windows Defender in Safe Mode.
Check Safe Mode Status: Detect if the system is currently in Safe Mode.
Admin Elevation Handling: Automatically elevates privileges if the script is not running as an Administrator.

# Prerequisites
Python 3.x: Ensure Python is installed.
Windows: This script is designed for Windows systems only.
Administrator Privileges: The script must be run with administrator privileges to make changes to system settings.


# Behavior:

If the system is in Regular Mode, it will:
Switch to Safe Mode.
Disable Windows Defender services and tasks.
Reboot the system into Safe Mode.
If the system is already in Safe Mode, it will:
Disable Windows Defender services and tasks.
Attempt to switch back to Regular Mode after rebooting.
