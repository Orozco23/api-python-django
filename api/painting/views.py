from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Painting
from .serializers import PaintingSerializer

# Get all the paintings (Read)
@api_view(['GET'])
def painting_list(request):
    paintings = Painting.objects.all()  # Get all the paintings from the database
    serializer = PaintingSerializer(paintings, many=True)
    return Response(serializer.data)

# Create a new painting (Create)
@api_view(['POST'])
def painting_create(request):
    if request.method == 'POST':
        serializer = PaintingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves the painting in the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Returns the newly created object
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Returns the errors if the data is not valid

# Updating an existing painting (Update)
@api_view(['PUT'])
def painting_update(request, id):
    painting = Painting.objects.get(id=id)
    if request.method == 'PUT':
        serializer = PaintingSerializer(painting, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves the changes in the painting
            return Response(serializer.data)  # Returns the updated object
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Returns the errors if the data is not valid

# Remove a painting (Delete)
@api_view(['DELETE'])
def painting_delete(request, id):
    painting = Painting.objects.get(id=id)
    if request.method == 'DELETE':
        painting.delete()  # Removes paint from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Returns status 204 (no content)

# Get details of a specific painting by id (Read)
@api_view(['GET'])
def painting_detail(request, id):
    painting = Painting.objects.get(id=id)  # Obtains the paint with the given id
    serializer = PaintingSerializer(painting)
    return Response(serializer.data) # Returns the painting details
