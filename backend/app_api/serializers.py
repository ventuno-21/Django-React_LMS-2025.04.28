from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app_account.models import User, Profile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # These information will be added in PAYLOAd of access/refresh Token
        token["full_name"] = user.full_name
        token["email"] = user.email
        token["username"] = user.username
        try:
            token["teacher_id"] = user.teacher.id
        except:
            token["teacher_id"] = 0

        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class Profileerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
