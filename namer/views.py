from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Matrix


def index(request):
    p = request.POST['year']
    print p
    return render(request, 'namer/index.html')

