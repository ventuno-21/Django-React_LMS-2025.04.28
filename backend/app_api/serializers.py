from rest_framework import serializers
from app_account.models import User, Profile


class UserSerializer(serializers.ModelSerilizer):

    class Meta:
        model = User
        fields = "__all__"


class Profileerializer(serializers.ModelSerilizer):

    class Meta:
        model = Profile
        fields = "__all__"
