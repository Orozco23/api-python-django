from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Card
from .serializers import CardSerializer

# Get all the Cards (Read)
@api_view(['GET'])
def card_list(request):
    cards = Card.objects.all()  # Get all the Cards from the database
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

# Create a new Card (Create)
@api_view(['POST'])
def card_create(request):
    if request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves the card in the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Returns the newly created object
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Returns the errors if the data is not valid

# Updating an existing card (Update)
@api_view(['PUT'])
def card_update(request, id):
    card = Card.objects.get(id=id)
    if request.method == 'PUT':
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves the changes in the card
            return Response(serializer.data)  # Returns the updated object
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Returns the errors if the data is not valid

# Remove a card (Delete)
@api_view(['DELETE'])
def card_delete(request, id):
    card = Card.objects.get(id=id)
    if request.method == 'DELETE':
        card.delete()  # Removes card from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Returns status 204 (no content)

# Get details of a specific card by id (Read)
@api_view(['GET'])
def card_detail(request, id):
    card = Card.objects.get(id=id)  # Obtains the card with the given id
    serializer = CardSerializer(card)
    return Response(serializer.data) # Returns the card details
