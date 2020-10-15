from django.urls import path
from .views import (
    GaleryView,
    UploadImageCreateView,
    ManageListImageListView,
)


app_name = 'core'

urlpatterns = [
    path('', GaleryView.as_view(), name="galery"),
    path('upload/', UploadImageCreateView.as_view(), name="upload_image"),
    path('gerenciamento/', ManageListImageListView.as_view(), name="manage_list"),
]