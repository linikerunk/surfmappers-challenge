from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    GaleryView,
    UploadImageCreateView,
    ManageListImageListView,
    UpdateImageUpdateView,
)


app_name = 'core'

urlpatterns = [
    path('', GaleryView.as_view(), name="galery"),
    path('upload/', UploadImageCreateView.as_view(), name="upload_image"),
    path('gerenciamento/', ManageListImageListView.as_view(), name="manage_list"),
    path('aprovacao/<int:pk>/', UpdateImageUpdateView.as_view(),
    name="approval_image"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)