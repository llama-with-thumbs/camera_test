import cv2

def capture_image_and_save(output_path):
    try:
        # Initialize the camera (0 represents the default camera)
        cap = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            print("Error: Could not open the camera.")
            return

        # Capture a single frame (an image)
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error: Could not capture the frame.")
            return

        # Save the captured image
        cv2.imwrite(output_path, frame)

        # Release the camera
        cap.release()

        print(f"Image captured and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the path where you want to save the image
    image_output_path = "image.jpg"

    # Call the capture_image_and_save function to capture and save the image
    capture_image_and_save(image_output_path)
