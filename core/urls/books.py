from django.urls import path
from core.views import book_view, author_view

urlpatterns = [
    path('book/<int:id>/', book_view, name='book'),
    path('author/<int:id>/', author_view, name='author'),
]
