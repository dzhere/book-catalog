from django.views.generic import CreateView
from core.models import *

class AddAuthorView(CreateView):
    model = Author
    fields = ('first_name', 'last_name', 'birtday_date', 'country')
    template_name = 'books/add.html'

class AddGenreView(CreateView):
    model = Genre
    fields = ('name',)
    template_name = 'books/add.html'

class AddBookView(CreateView):
    model = Book
    fields = ('authors', 'title')
    template_name = 'books/add.html'