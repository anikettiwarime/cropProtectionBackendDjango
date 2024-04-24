from django.urls import path
from .views import ImageUploadView, HomeApiView

urlpatterns = [
    path('predict/', ImageUploadView.as_view(), name='predict'),
    path('', HomeApiView.as_view(), name='home'),
]