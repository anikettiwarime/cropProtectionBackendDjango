from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to='images/')
    is_intruder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
