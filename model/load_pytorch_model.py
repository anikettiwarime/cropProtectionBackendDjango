import torch
from torchvision import models, transforms
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
import os

# Load the saved model
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, 1000)  # Adjust to match the original model's output units
model.load_state_dict(torch.load('model1.pth'))
model.eval()

# Create a new model with the correct final layer
new_model = models.resnet18(pretrained=True)
new_model.fc = nn.Linear(new_model.fc.in_features, 2)  # Adjust to match the desired output units

# Copy the weights and biases from the loaded model to the new model
new_model.fc.weight.data = model.fc.weight.data[0:2]  # Copy only the first 2 output units
new_model.fc.bias.data = model.fc.bias.data[0:2]


# Prepare your new image for classification. You should use the same data transformations you used during training. Here's an example of how to prepare an image for inference:

from PIL import Image
import torch
import torchvision.transforms as transforms

# Perform inference using the model:

# Load and preprocess the unseen image
image_path = 'C:/Users/Admin/Documents/MLPROJECT/cell_images2/test/elefante/e833b80c2afc033ed1584d05fb1d4e9fe777ead218ac104497f5c978a4efbcb0_640.jpg'  # Replace with the path to your image
image = Image.open(image_path)
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
input_tensor = preprocess(image)

# Add a batch dimension to the input tensor
input_batch = input_tensor.unsqueeze(0)

# Perform inference
with torch.no_grad():
    output = model(input_batch)

# Get the predicted class
_, predicted_class = output.max(1)

# Map the predicted class to the class name
class_names = ['cane', 'cavallo', 'elefante', 'farfalla', 'gallina', 'gatto', 'mucca', 'pecora', 'ragno', 'scoiattolo']  # Make sure these class names match your training data
predicted_class_name = class_names[predicted_class.item()]

#*****************************************************
def find_class(predicted_class_name):
    
    if predicted_class_name=='cane':
        return "Dog"
    elif predicted_class_name=='cavallo':
        return "Horse"
    elif predicted_class_name=='elefante':
        return "Elephant"
    elif predicted_class_name=='farfalla':
        return "Butterfly"
    elif predicted_class_name=='gallina':
        return "Cock"
    elif predicted_class_name=='gatto':
        return "Cat"
    elif predicted_class_name=='mucca':
        return "cow"
    elif predicted_class_name=='pecora':
        return "Sheep"
    elif predicted_class_name=='ragno':
        return "Spider"
    else:
        return "scoiattolo"
        
output = find_class(predicted_class_name)

print(f'The predicted class is: {output}')


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Display the image with the predicted class name
image = np.array(image)
plt.imshow(image)
plt.axis('off')
plt.text(10, 10, f'Predicted: {output}', fontsize=12, color='white', backgroundcolor='red')
plt.show()