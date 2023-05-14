from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def bot_info(request):
    info = BotInfo.objects.last()
    return Response(BotInfoSerializer(info).data)


@api_view(['GET'])
def listening(request):
    cat = Category.objects.all()
    item = cat.filter(typee=1).last()
    return Response(CategorySerializer(item).data)


@api_view(['GET'])
def reading(request):
    cat = Category.objects.all()
    item = cat.filter(typee=2).last()
    return Response(CategorySerializer(item).data)


@api_view(['GET'])
def speaking(request):
    cat = Category.objects.all()
    item = cat.filter(typee=3).last()
    return Response(CategorySerializer(item).data)


@api_view(['GET'])
def writing(request):
    cat = Category.objects.all()
    item = cat.filter(typee=4).last()
    return Response(CategorySerializer(item).data)


@api_view(['GET'])
def modules(request):
    module = Modules.objects.all().order_by('-id')[:4]
    return Response(ModuleSerializer(module, many=True).data)

