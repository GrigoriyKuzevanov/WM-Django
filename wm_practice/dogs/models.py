from django.db import models


class Dog(models.Model):
    """
    Класс для представления модели собаки в базе данных.
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
        """
        Возвращает строковое представление класса на основе поля name.
        """

        return f"Dog: {self.name}"


class Breed(models.Model):
    """
    Класс для представления породы собак в базе данных.
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

    def __str__(self):
        """
        Возвращает строковое представление класса на основе поля name.
        """

        return f"Breed: {self.name}"
