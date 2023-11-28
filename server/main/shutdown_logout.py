import os
import threading
import re

def shutdown():
    os.system("shutdown -s -t 0")


def logout():
    os.system(f"shutdown -l")


def shutdown_logout(function):
    result = None
    if "Shutdown" in function:
        timeLog = int(re.search(r"Shutdown\[(\d+)\]", function).group(1))
        result = f"Server will shutdown in {timeLog}s"
        threading.Timer(timeLog, shutdown).start()
    elif "Logout" in function:
        timeLog = int(re.search(r"Logout\[(\d+)\]", function).group(1))
        result = f"Server will logout in {timeLog}s"
        threading.Timer(timeLog, logout).start()
    return "<div class='mb-2'><b>Shutdown/Logout:</b> " + result + "</div>"
