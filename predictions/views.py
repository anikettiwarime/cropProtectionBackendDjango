from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import tempfile

from .models import Prediction
from .serializers import PredictionSerializer, ImageUploadSerializer
from .utils import find_class

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            image_file = serializer.validated_data['image']

            # Save the uploaded image to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                temp_file.write(image_file.read())
                temp_file_path = temp_file.name

            try:
                # Load the model
                model = load_model('model/animal.h5')

                # Load and preprocess the test image
                test_image = image.load_img(temp_file_path, target_size=(64, 64))
                test_image = image.img_to_array(test_image)
                test_image = test_image / 255.0
                test_image = np.expand_dims(test_image, axis=0)

                # Make predictions using the model
                result = model.predict(test_image)

                # Get the class index with the highest probability
                predicted_class_index = np.argmax(result)

                # Find and print the class name corresponding to the predicted index
                predicted_class_name = find_class(predicted_class_index)
                category = "Unknown"
                is_intruder = False

                # Classify into animals, birds, or insects
                if predicted_class_index in [1, 2, 3, 4, 5, 6, 7, 9]:  # Animal classes
                    category = "Animal"
                    is_intruder = True
                elif predicted_class_index in [8, 0]:  # Insect class
                    category = "Insect"

                # Create a Prediction instance
                if is_intruder:
                    prediction = Prediction.objects.create(
                        image=image_file,
                        is_intruder=is_intruder
                    )

                return Response(
                    {
                        'class': predicted_class_name,
                        'category': category,
                        'is_intruder': is_intruder,
                    },
                    status=status.HTTP_200_OK
                )
            finally:
                # Remove the temporary file
                os.unlink(temp_file_path)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictionDetailView(APIView):
    def get(self, request):
        prediction = Prediction.objects.all()
        serializer = PredictionSerializer(prediction, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HomeApiView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Image Classification API!'}, status=status.HTTP_200_OK)
