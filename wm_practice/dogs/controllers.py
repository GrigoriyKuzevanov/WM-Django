from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class DogDetail(APIView):
    """Class for handling requests to get, update, delete dog data.

    - GET: Get dog data by given id
    - PUT: Update dog data by given id
    - DELETE: Delete dog data by given id
    """

    def get_object(self, pk: int) -> Dog:
        """Get dog model by given id from database or raise
        exception if it doens't exist.

        Args:
            pk (int): Dog's id

        Raises:
            Http404: If Dog with given id doesn't exist

        Returns:
            Dog: Django orm model for dog with given id
        """

        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404(f"Dog with id: {pk} is not found")

    def get(self, request: Request, pk: int) -> Response:
        """Get dog data using given identificator

        Args:
            request (Request): DRF Request object
            pk (int): Dog's id

        Returns:
            Response: DRF Response object with requested dog data
        """

        model = self.get_object(pk)
        serializer = DogSerializer(model)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """Update dog data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): Dog's id

        Returns:
            Response: DRF Response object with updated dog data
        """

        model = self.get_object(pk)
        serializer = DogSerializer(model, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """Delete dog data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): Dog's id

        Returns:
            Response: Blank DRF Response with 204 status
        """

        model = self.get_object(pk)
        model.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):
    """Class for handling requests to get list of all dogs from DB
    and to create a new dog in DB with given request data.

    - GET: Get list of all dogs
    - POST: Create a new dog in DB
    """

    def get(self, request: Request) -> Response:
        """Get list of all dogs in DB.

        Args:
            request (Request): DRF Request object

        Returns:
            Response: DRF Response object with data of all dogs
        """

        qs = Dog.objects.all().select_related("breed")

        serializer = DogSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """Create a new dog with given data.

        Args:
            request (Request): DRF Request object

        Returns:
            Response: DRF Response object with created dog data
        """

        serializer = DogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):
    """Class for handling requests to get, update, delete breed data.

    - GET: Get breed data by given id
    - PUT: Update breed data by given id
    - DELETE: Delete breed data by given id
    """

    def get_object(self, pk: int) -> Breed:
        """Get breed model by given id from database or raise
        exception if it doesn't exist.

        Args:
            pk (int): Breed's id

        Raises:
            Http404: If Breed with given id doesn't exist

        Returns:
            Breed: Django orm model for breed with given id
        """

        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404(f"Breed with id: {pk} is not found")

    def get(self, request: Request, pk: int) -> Response:
        """Get breed data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): Breed's id

        Returns:
            Response: DRF Response object with requested breed data
        """

        model = self.get_object(pk)
        serializer = BreedSerializer(model)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """Update breed data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): Breed's id

        Returns:
            Response: DRF Response object with updated breed data
        """

        model = self.get_object(pk)
        serializer = BreedSerializer(model, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """Delete breed data using given identificator.

        Args:
            request (Request): DRF Request object
            pk (int): Breed's id

        Returns:
            Response: Blank DRF Response with 204 status
        """

        model = self.get_object(pk)
        model.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(APIView):
    """Class for handling requests to get list of all breeds from DB
    and to create a new breed in DB with given request data.

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
