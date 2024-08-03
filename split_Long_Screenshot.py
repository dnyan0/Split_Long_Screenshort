# Note: Check the address of the Input and Output folders in the code.
from PIL import Image
# PIL stands for Python Imaging Library
def split_long_screenshot(input_image_path, output_folder, num_splits):
    # Open the image
    image = Image.open("Input image address")

    # Getting Image Dimensions
    width, height = image.size

    # Calculate the height of each small picture
    split_height = height // num_splits

    # Iterate and save each small picture
    for i in range(num_splits):
        # Calculate the region to crop
        top = i * split_height
        bottom = (i + 1) * split_height

        # Crop the region
        region = image.crop((0, top, width, bottom))

        # Save the cropped region
        output_path = f"{"output image address"}/split_{i + 1}.png"
        region.save(output_path)

if __name__ == "__main__":
    # Replace 'input_image_path' with the path to your long screenshot
    input_image_path = "path/to/long_screenshot.png"

    # Replace 'output_folder' with the folder where you want to save the small pictures
    output_folder = "path/to/output_folder"

    # Replace 'num_splits' with the desired number of small pictures
    num_splits = 5

    split_long_screenshot(input_image_path, output_folder, num_splits)
