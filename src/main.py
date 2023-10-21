import cv2
import numpy as np

# Load the images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Convert the images to grayscale
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate the average pixel values for each image
average_pixel_value_image1 = np.mean(gray_image1)
average_pixel_value_image2 = np.mean(gray_image2)

# Display the average pixel values
print('Average pixel value for image 1:', average_pixel_value_image1)
print('Average pixel value for image 2:', average_pixel_value_image2)

# Compare the average pixel values
if average_pixel_value_image1 > average_pixel_value_image2:
    print('Image 1 has a higher average pixel value.')
elif average_pixel_value_image1 < average_pixel_value_image2:
    print('Image 2 has a higher average pixel value.')
else:
    print('The average pixel values of both images are equal.')
