import cv2
import os

# Define relative path to the image using specified logo path
image_path = os.path.join("..", "Images", "logo.png")

# Load the image using OpenCV
img = cv2.imread(image_path)

# Check if image loaded successfully
if img is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Display the image in a window
    cv2.imshow("Loaded Image", img)
    print("Image loaded successfully. Press any key to close the window.")
    
    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
