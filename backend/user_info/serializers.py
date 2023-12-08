# user_info/serializers.py

# Importing the User model from Django's built-in authentication system
from django.contrib.auth.models import User

# Serializers define how to convert complex data types, such as Django models, into native Python datatypes that can be rendered into JSON.
from rest_framework import serializers


# Defining a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Specifying the fields to be included in the serialized output
        fields = ('username', 'password')
