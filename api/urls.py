from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('predict/', ImageUploadView.as_view(), name='predict'),
]