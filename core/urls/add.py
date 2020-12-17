from django.urls import path
from core.views import AddAuthorView, AddGenreView, AddBookView

urlpatterns = [
    path('author/', AddAuthorView.as_view(), name='add_author'),
    path('genre/', AddGenreView.as_view(), name='add_genre'),
    path('book/', AddBookView.as_view(), name='add_book'),
]