from django.urls import path
from .views import *

urlpatterns = [
    path('', posts, name='home'),                # список url-ов
    path('eng_1/', grammar, name='grammar'),     # name - прописаны для отображения меню (base.html)
    path('eng_2/', dictionary, name='dictionary'),
    path('library/', books, name='books'),
    path('framework_1/', flask, name='flask'),
    path('framework_2/', django, name='django'),
]