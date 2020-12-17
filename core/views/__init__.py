from django.shortcuts import render
from .auth import *
from .books import *
from .profile import *

def index_view(request):
    return render(request, 'index.html')