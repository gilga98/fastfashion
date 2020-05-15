from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .utils import predict
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","username"]

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_ClassField
        fields = "__all__"

class CupboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        validated_data["user"] = user_serializer.save()
        instance = super().create(validated_data)
        return instance

    class Meta:
        model = Cupboard
        fields ="__all__"


class DressSerializer(serializers.ModelSerializer):
    cupboard = CupboardSerializer(required=True)
    prediction = ClassSerializer(required=False,read_only=True)
    def create(self, validated_data):
        cupboard_data = validated_data.pop("cupboard")
        cupboard_serializer = CupboardSerializer(data=cupboard_data)
        cupboard_serializer.is_valid(raise_exception=True)
        validated_data["cupboard"] = cupboard_serializer.save()
        instance = super().create(validated_data)
        # add logic to predict dress type here
        result_dict = predict(instance.image)
        print(result_dict)
        instance.prediction = result_dict["prediction"]
        return instance

    class Meta:
        model = Dress
        fields = "__all__"