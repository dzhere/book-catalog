from django.urls import path
from core.views import *

urlpatterns = [
    path('book/<int:id>/', book_view, name='book'),
    path('author/<int:id>/', author_view, name='author'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('genres/', GenresListView.as_view(), name='genres_list'),
    path('authors/', AuthorsListView.as_view(), name='authors_list'),
    path('add_book_to_list/<int:id>', add_book_to_list, name='add_book_to_list')
]
