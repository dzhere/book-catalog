from django.shortcuts import render, redirect
from core.models import Profile, Book

def profile_view(request):
    if request.user.is_authenticated:
        profile, is_created = Profile.objects.get_or_create(user=request.user)
        return render(request, "profile/index.html", {"books_list": profile.books_list.all()})
    else:
        return redirect('/')

def add_book_to_list(request, id):
    if request.user.is_authenticated:
        profile, is_created = Profile.objects.get_or_create(user=request.user)
        book = Book.objects.get(pk=id)
        profile.books_list.add(book)
        return redirect('/profile')
    else:
        return redirect('/')
