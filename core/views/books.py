from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from core.models import *

class AddAuthorView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Author
    fields = ('__all__')
    template_name = 'books/add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save() 
        return redirect("/")

class AddGenreView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Genre
    fields = ('__all__')
    template_name = 'books/add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save() 
        return redirect("/")

class AddBookView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
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
