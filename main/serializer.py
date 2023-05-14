from rest_framework import serializers
from main.models import *


class BotInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotInfo
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
