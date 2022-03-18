# from dataclasses import fields
# import imp
# from pyexpat import model
# from pyexpat.errors import messages
from rest_framework import serializers
from .models import Messages

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'name', 'age', 'messages', 'created_at']



