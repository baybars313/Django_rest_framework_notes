from django.shortcuts import redirect,render
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')
