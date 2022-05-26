from django.urls import path

from . import views


urlpatterns = [
    path("uploads", views.uploads, name="uploads"),
    path("upload/<int:upload_id>/", views.upload_detail, name="upload_detail"),
]
