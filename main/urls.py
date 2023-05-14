from django import urls
from django.urls import path
from .views import *


urlpatterns = [
    path('bot-info/', bot_info),
    path('modules/', modules),
    path('listening/', listening),
    path('reading/', reading),
    path('speaking/', speaking),
    path('writing/', writing),

]