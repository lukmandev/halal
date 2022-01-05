from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'avatar',
            'phone',
            'gender',
            'creation_date',
            'update_date',
            'favorite_companies'
        )