from django.db.models.query import QuerySet
from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class DogDetail(APIView):
    """
    Класс для обработки запросов на получение, обновление и удаление
    данных о конкретной собаке.

    - GET: Получить данные о собаке по id
    - PUT: Обновить данные о собаке по id
    - DELETE: Удалить данные собаки по id
    """

    def get_object(self, pk: int) -> Dog:
        """
        Получить объект собаки по переданному идентификатору.
        Возвращает Http 404 error, если данных собаки с переданным id
        не существует.

        Args:
            pk (int): Идентификатор собаки
        """

        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404(f"Dog with id: {pk} is not found")

    def get(self, request, pk: int, format=None) -> Response:
        """
        Получить данные о собаке по переданному идентификатору.

        Args:
            pk (int): идентификатор собаки
        """

        dog_model = self.get_object(pk)
        dog_serializer = DogSerializer(dog_model)

        return Response(dog_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int) -> Response:
        """
        Изменить данные о собаке по переданному идентификатору.

        Args:
            pk (int): идентификатор собаки
        """

        dog_model = self.get_object(pk)
        dog_serializer = DogSerializer(dog_model, data=request.data)

        if dog_serializer.is_valid():
            dog_serializer.save()
            return Response(dog_serializer.data, status=status.HTTP_200_OK)

        return Response(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        """
        Удалить данные о собаке по переданному идентификатору.

        Args:
            pk (int): идентификатор собаки
        """

        dog_model = self.get_object(pk)
        dog_model.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):
    """
    Класс для обработки запросов на получение списка собак
    и добавления данных новой собаки.

    - GET: Получить список данных о всех собаках
    - POST: Добавить данные о новой собаке
    """

    @staticmethod
    def get_queryset() -> QuerySet[Dog]:
        """
        Получить список всех записей собак из БД.
        """

        return Dog.objects.all()

    def get(self, request) -> Response:
        """
        Получить список всех собак из БД.
        """

        dog_models = self.get_queryset()
        serializer = DogSerializer(dog_models, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        """
        Добавить данные о новой собаке с переданными параметрами.
        """

        dog_serializer = DogSerializer(data=request.data)

        if dog_serializer.is_valid():
            dog_serializer.save()
            return Response(dog_serializer.data, status=status.HTTP_201_CREATED)

        return Response(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):
    """Class for handling requests to get, update, delete breed's data.

    - GET: Get breed's data by given id
    - PUT: Update breed's data by given id
    - DELETE: Delete breed's data by given id
    """

    def get_object(self, pk: int) -> Breed:
        """Get breed model by given id from database or raise
        exception if it doesn't exist.

        Args:
            pk (int): Breed's id

        Raises:
            Http404: If Breed by given id doesn't exist

        Returns:
            Breed: Django orm model for breed by given id
        """

        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404(f"Breed with id: {pk} is not found")

    def get(self, request: Request, pk: int) -> Response:
        """Get breed data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): breed's id

        Returns:
            Response: DRF Response object with requested breed's data
        """

        model = self.get_object(pk)
        serializer = BreedSerializer(model)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """Update breed's data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): breed's id

        Returns:
            Response: DRF Response object with updated breed's data
        """

        model = self.get_object(pk)
        serializer = BreedSerializer(model, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """Delete breed's data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): breed's id

        Returns:
            Response: blank DRF Response with 204 status
        """

        model = self.get_object(pk)
        model.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(APIView):
    """Class for handling requests to get list of all breeds from DB
    and to create a new breed in DB with given in request data.

    - GET: Get list of all breeds
    - POST: Create a new breed in DB
    """

    def get(self, request: Request) -> Response:
        """Get list of all breeds in DB.

        Args:
            request (Request): DRF Request object

        Returns:
            Response: DRF Response object with data of all breeds
        """

        qs = Breed.objects.all()
        serializer = BreedSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """Create a new breed with given data.

        Args:
            request (Request): DRF Request object

        Returns:
            Response: DRF Response object with created breed data
        """

        serializer = BreedSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
