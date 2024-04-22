from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the model
model = load_model('animal.h5')

# Function to find class name based on index
def find_class(f):
    class_mapping = {
        0: "Dog",
        1: "Horse",
        2: "Elephant",
        3: "Butterfly",
        4: "Cock",
        5: "Cat",
        6: "Cow",
        7: "Sheep",
        8: "Spider",
        9: "Squirrel"
    }
    return class_mapping.get(f, "Unknown")

# Load and preprocess the test image

# Path to the image file
image_path = 'OIP-zMaM2f6nWX-bwQNMd0HmxAHaE7.jpeg'

# test_image = image.load_img('C:/Users/Admin/Videos/finalYrProject/dataset/raw-img/gallina/5.jpeg', target_size=(64, 64))
test_image = image.load_img(image_path, target_size=(64, 64))

test_image = image.img_to_array(test_image)
test_image = test_image / 255.0  # Normalize pixel values
test_image = np.expand_dims(test_image, axis=0)  # Add batch dimension

# Make predictions using the model
result = model.predict(test_image)

# Get the class index with the highest probability
predicted_class_index = np.argmax(result)

# Find and print the class name corresponding to the predicted index
predicted_class_name = find_class(predicted_class_index)


# Load the image using matplotlib's imread function
image = mpimg.imread(image_path)

# Display the image
# plt.imshow(image)
# plt.axis('off')  # Hide axis
# plt.show()

print("Predicted class:", predicted_class_name)
plt.imshow(image)
plt.axis('off') 
plt.title(f'Predicted Class: {predicted_class_name}')
plt.show()