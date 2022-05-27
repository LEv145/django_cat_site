from django.urls import path

from . import views


urlpatterns = [
    path("uploads", views.UploadList.as_view(), name="uploads"),
    path("upload/<int:pk>/", views.UploadDetail.as_view(), name="upload_detail"),
]
