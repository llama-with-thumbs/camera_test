import picamera

def capture_image(output_path):
    try:
        with picamera.PiCamera() as camera:
            # Set the camera resolution (optional)
            camera.resolution = (1920, 1080)  # Set your desired resolution

            # Capture an image and save it to the specified path
            camera.capture(output_path)

            print(f"Image captured and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the path where you want to save the captured image
    image_output_path = "my_image.jpg"

    # Call the capture_image function to capture the image
    capture_image(image_output_path)
