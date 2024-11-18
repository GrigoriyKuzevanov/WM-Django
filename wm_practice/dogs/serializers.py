from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

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

    breed_id = PrimaryKeyRelatedField(
        queryset=Breed.objects.all(), source="breed", write_only=True
    )
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "breed_id",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        ]
        read_only_fields = ["id", "breed"]
