from email import message
from django.http import JsonResponse
from .models import Messages
from .serializers import MessageSerializer

def messages_list(request):
    # geting all messages 
    messages = Messages.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse({"Messages": serializer.data}, safe=False)

