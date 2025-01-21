from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view([])
def index(request):
    if request.method == 'GET':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['POST', 'PUT'])
def pos(request):
    if request.method == 'POST':
        new_content = request.data.get('content', 'New Content Created')
        return Response({"message": "Content created", "new_content": new_content}, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        updated_content = request.data.get('content', 'Updated Content')
        return Response({"message": "Content updated", "updated_content": updated_content}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(request):
    if request.method == 'DELETE':
        return Response({"message": "Content deleted"}, status=status.HTTP_204_NO_CONTENT)