from PIL import ImageGrab
import os


def capture_screen(default_value=None):
    # capture the screen
    return ImageGrab.grab()
