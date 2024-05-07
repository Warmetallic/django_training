from django.http import HttpResponse, HttpRequest
from django.shortcuts import render



# Create your views here.
def views_home(request: HttpRequest) -> HttpResponse:

    return render(request, 'views/base.html')