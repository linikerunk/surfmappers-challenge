from django.urls import path
from .views import GaleryView, UploadImageCreateView 


app_name = 'core'

urlpatterns = [
    path('', GaleryView.as_view(), name="galery"),
    path('upload/', UploadImageCreateView.as_view(), name="upload_image"),
]