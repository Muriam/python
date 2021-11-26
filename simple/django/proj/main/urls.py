from django.urls import path
from .views import *

urlpatterns = [
    path('', posts),                # список url-ов
    path('eng_1/', grammar),
    path('eng_2/', dictionary),
    path('library/', books),
    path('framework_1/', flask),
    path('framework_2/', django),
]