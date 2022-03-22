# from email import message
from ast import If
from xmlrpc.client import ResponseError
from django.http import JsonResponse
from .models import Messages
from .serializers import MessageSerializer

# Api View Decorator
from rest_framework.decorators import api_view
# Importing Response and Status
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def messages_list(request):
    # geting all messages 
    if request.method == 'GET':
        messages = Messages.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse({"Messages": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request):
    if request.method == 'GET':
        pass
    elif:
        
