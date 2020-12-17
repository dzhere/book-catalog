from django.views.generic import CreateView
from django.shortcuts import redirect
from core.models import *

class AddAuthorView(CreateView):
    model = Author
    fields = ('__all__')
    template_name = 'books/add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save() 
        return redirect("/")

class AddGenreView(CreateView):
    model = Genre
    fields = ('__all__')
    template_name = 'books/add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save() 
        return redirect("/")

class AddBookView(CreateView):
    model = Book
    fields = ('__all__')
    template_name = 'books/add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save() 
        return redirect("/")
