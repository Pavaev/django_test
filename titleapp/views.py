from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse


from .models import Header
# Create your views here.


def title(request):
    return render_to_response('title.html', {"header": Header.objects.get(id=1)})