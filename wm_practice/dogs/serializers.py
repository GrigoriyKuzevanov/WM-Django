from rest_framework.serializers import ModelSerializer

from .models import Breed, Dog


class BreedSerializer(ModelSerializer):
    """
    Сериалайзер для модели породы. Использует все поля модели,
    поле id доступно только для чтения.
    """

    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
        ]
        read_only_fields = ["id"]


class DogSerializer(ModelSerializer):
    """
    Сериалайзер для модели собаки. Использует все поля модели,
    поле id доступно только для чтения.
    """

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        ]
        read_only_fields = ["id"]
