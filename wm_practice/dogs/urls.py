from django.urls import path
from .controllers import DogDetail, DogList


urlpatterns = [
    path("dogs/<int:pk>/", DogDetail.as_view(), name="dog-detail"),
    path("dogs/", DogList.as_view(), name="dog_list"),
]
