# Split_Long_Screenshort
This code can be used to split the long screenshort in short pictures.
# Step-by-Step explanation how this code works 
# 1. Importing the Library:
  Import the 'Image' module from the Python Imaging Library (PIL).
# 2. Defining the Function:
  Define a function 'split_long_screenshot' that takes three parameters: 'input_image_path', 'output_folder' and 'num_splits'.
# 3. Opening the Image: 
  Open the "input.image" using the Image.open method from PIL.
# 4. Getting Image Dimensions: 
  Get the width and height of the image using the 'size' attribute.
# 5. Calculating Split Height: 
  Calculate the height of each smaller image by dividing the total height by the number of splits.
# 6. Iterating to Save Smaller Images: 
  I.Loop through the range of 'num_splits'.<br>
  II. For each iteration, calculate the 'top' and 'bottom' coordinates for cropping.<br>
  III. Crop the image region using the 'crop' method, specifying the coordinates '(left, top, right, bottom)'.<br>
  IV. Generate the output path for the cropped image and save it using the 'save' method.<br>
# 7. Main Block: 
  I. Define the main block to ensure the code runs only if the script is executed directly.<br>
  II. Set the paths for input_image_path and output_folder, and specify the number of splits.<br>
  III. Call the split_long_screenshot function with the provided parameters.<br>
