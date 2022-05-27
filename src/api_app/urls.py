from django.urls import path

from . import views


urlpatterns = [
    path("uploads", views.uploads_view, name="uploads"),
    path("upload/<int:pk>/", views.upload_detail_view, name="upload_detail"),
]
