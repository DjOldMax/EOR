from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='Home'),
    path('book/<int:book_id>/', show_book, name='book'),
    path('media/', show_media, name='media')
]