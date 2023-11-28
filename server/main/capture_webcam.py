import cv2
from PIL import Image
import os


def capture_webcam_image(default_value=None):
    # initialize the camera
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # check if camera is opened successfully
    if not camera.isOpened():
        return "Unable to open camera"
    else:
        # capture a frame from the camera
        bool, image = camera.read()

        if bool:
            # convert color space from BGR to RGB
            rgb_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


            # pil_image.save("image/Webcam_image.png")
        
            try:
                # create a PIL Image from the numpy array
                pil_image = Image.fromarray(rgb_frame)
                
                # Create the directory if it doesn't exist
                directory = "static/server/images"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                
                # Save the image in the directory
                pil_image.save(os.path.join(directory, "Webcam_image.png"))
                return pil_image
            except Exception as e:
                print("Error occurred:", e)
                return default_value


            return pil_image
        else:
            return "Unable to capture"
