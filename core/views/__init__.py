from django.shortcuts import render
from .auth import *

def index_view(request):
    return render(request, 'index.html')