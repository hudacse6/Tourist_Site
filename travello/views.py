from django.shortcuts import render
from .models import Destination
from .models import News_blog


# Create your views here.

def index(request):
    dest = Destination.objects.all()
    blog = News_blog.objects.all()

    return render(request, 'index.html', {'dest': dest, 'blog': blog})
