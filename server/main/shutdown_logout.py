import os
import threading


def shutdown():
    os.system("shutdown -s -t 0")


def logout():
    os.system(f"shutdown -l")


def shutdown_logout(function):
    result = None
    if "Shutdown" in function:
        result = "Server will shutdown in 30s"
        threading.Timer(30, shutdown).start()
    elif "Logout" in function:
        result = "Server will logout in 30s"
        threading.Timer(30, logout).start()
    return "<div class='mb-2'><b>Shutdown/Logout:</b> " + result + "</div>"
