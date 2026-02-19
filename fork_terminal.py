import os
import subprocess
import platform

def fork_terminal(command: str) -> str:
    system = platform.system()
    cwd = os.getcwd()
    
    try:
        if system == "Windows":
            full_command = f'cd /d "{cwd}" && {command}'
            subprocess.Popen(["cmd.exe", "/c", "start", "", "cmd.exe", "/k", full_command], shell=False)
        elif system == "Linux":
            # Example for Linux (requires a terminal like xterm or gnome-terminal)
            subprocess.Popen(["xterm", "-e", f"bash -c 'cd {cwd} && {command}; exec bash'"], shell=False)
        else:
            return f"Unsupported OS: {system}"
            
        return f"{system} terminal launched"
    except Exception as e:
        return f"Error launching terminal: {e}"
