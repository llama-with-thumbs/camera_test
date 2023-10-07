from PIL import Image

def save_image_with_pillow(input_path, output_path):
    try:
        # Open the captured image with Pillow
        image = Image.open(input_path)

        # Save the image (you can also perform further processing here)
        image.save(output_path)

        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the path of the captured image
    captured_image_path = "image.jpg"

    # Specify the path where you want to save the processed image
    processed_image_path = "processed_image.jpg"

    # Call the save_image_with_pillow function to open and save the image
    save_image_with_pillow(captured_image_path, processed_image_path)
