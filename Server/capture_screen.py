from PIL import ImageGrab
from PIL import Image
import os


def capture_screen(default_value=None):
    # capture the screen
    img = ImageGrab.grab()
    img.save("image/Screenshot.png")
    return img
