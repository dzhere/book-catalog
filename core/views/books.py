from django.views.generic import CreateView
from django.shortcuts import redirect, render
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

def book_view(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "books/book.html", {"book": book})

def author_view(request, id):
    author = Author.objects.get(pk=id)
    books = Book.objects.all().filter(author=author)
    return render(request, "books/author.html", {"author": author, "books": books})
