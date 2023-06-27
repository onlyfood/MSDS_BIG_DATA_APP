from django.shortcuts import render
from .utils import fetch_data_and_store_in_db

# Create your views here.

from django.http import HttpRequest, HttpResponse

def myapp(request: HttpRequest) -> HttpResponse:
    user_input = request.GET.get('input', '')
    return render(request, 'myapp.html', {'user_input': user_input})




def fetch_data_view(request):
    fetch_data_and_store_in_db()
    return HttpResponse('Data fetched and stored successfully!')
