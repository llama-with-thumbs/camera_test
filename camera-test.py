from PIL import Image
import subprocess
import os

def capture_and_save_image(output_path):
    try:
        # Use the raspistill command to capture an image
        subprocess.run(["raspistill", "-o", output_path])

        # Open the captured image with Pillow
        image = Image.open(output_path)

        # Save the image (you can also perform further processing here)
        image.save(output_path)

        print(f"Image captured and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the path where you want to save the image
    image_output_path = "image.jpg"

    # Call the capture_and_save_image function to capture and save the image
    capture_and_save_image(image_output_path)
