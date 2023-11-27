from PIL import ImageGrab
from PIL import Image
import os

def capture_screen(default_value=None):
    try:
        # Capture the screen
        img = ImageGrab.grab()
        
        # Create the directory if it doesn't exist
        directory = "server/main/image"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Save the image in the directory
        img.save(os.path.join(directory, "Screenshot.png"))
        return img
    except Exception as e:
        print("Error occurred:", e)
        return default_value
