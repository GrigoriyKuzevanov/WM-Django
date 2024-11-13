from django.urls import path
from .controllers import DogDetail


urlpatterns = [
    path("dogs/<int:pk>/", DogDetail.as_view(), name="dog-detail"),
]
