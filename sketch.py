import cv2
import os
import numpy as np  # Import numpy

# Specify the image path (change this to your file path if necessary)
image_path = "after_edit.jpg"

# Check if the image exists at the specified path
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found.")
    exit()

# Load the image
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not loaded properly. Check the file path.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted = 255 - gray_image

# Apply a stronger Gaussian blur for smoother effects
blur = cv2.GaussianBlur(inverted, (35, 35), 0)

# Invert the blurred image
invertedblur = 255 - blur

# Create the pencil sketch
sketch = cv2.divide(gray_image, invertedblur, scale=250.0)

# Apply contrast and brightness adjustment (reduce contrast and brightness)
contrast = cv2.convertScaleAbs(sketch, alpha=1, beta=7)  # Lower contrast and brightness

# Optionally, sharpen the sketch to add more detail (use a kernel for sharpening)
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # Sharpening kernel
sharpened = cv2.filter2D(contrast, 0, sharpen_kernel)

# Save the enhanced sketch
cv2.imwrite("after_edit.jpg", sharpened)

# Show the enhanced sketch (in a window)
cv2.imshow("after_edit.jpg", sharpened)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close the window




