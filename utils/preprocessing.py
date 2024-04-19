from PIL import Image
import os

def resize_images(folder_path):
    # Get the list of files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file in the folder
    for file_name in file_list:
        # Check if the file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            # Open the image file
            image_path = os.path.join(folder_path, file_name)
            image = Image.open(image_path)

            # Resize the image to 255x255 pixels
            resized_image = image.resize((128, 128))

            # Save the resized image
            resized_image.save(image_path)

            # Close the image file
            image.close()

# Call the function with the folder path
folder_path = "/home/snow/NEU/StableDiffusion-PyTorch/data/images/train/2"
resize_images(folder_path)