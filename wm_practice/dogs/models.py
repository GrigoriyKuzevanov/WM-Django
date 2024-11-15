from django.db import models


class Dog(models.Model):
    """
    Dog model representing class.
    """

    name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(
        "Breed", related_name="dogs", on_delete=models.CASCADE, blank=False
    )
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(255)
    favorite_toy = models.CharField(255)

    def __str__(self) -> str:
        """Get instance's string representation using name field.

        Returns:
            str: String representation.
        """

        return f"Dog: {self.name}"


class Breed(models.Model):
    """
    Breed model representing class.

    Attributes:
        SIZE_CHOICES (list[tuple[str, str]]): Choices for size field
        RATING_CHOICES (list[typle[int, str]]): Choices for fields using rating system
    """

    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=False)
    friendliness = models.PositiveIntegerField(choices=RATING_CHOICES, blank=False)
    trainability = models.PositiveIntegerField(choices=RATING_CHOICES, blank=False)
    shedding_amount = models.PositiveIntegerField(choices=RATING_CHOICES, blank=False)
    exercise_needs = models.PositiveIntegerField(choices=RATING_CHOICES, blank=False)

    def __str__(self) -> str:
        """Get instance's string representation using name field.

        Returns:
            str: String representation.
        """

        return f"Breed: {self.name}"
