from rest_framework.serializers import ModelSerializer

from .models import Breed, Dog


class BreedSerializer(ModelSerializer):
    """Serializer class for Breed model using all is's fields,
    and id field read only.
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
    """Serializer class for Dog model using all is's fields,
    and id field read only.
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
