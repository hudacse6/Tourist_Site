from django.shortcuts import render
from .models import Destination
from .models import News_blog


# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = 'mumbai'
    # dest1.dis = "dj hfahfahf ashfasjhf hashf fnsaflks"
    # dest1.price = 900
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = 'Dhaka'
    # dest2.dis = "city of mosque"
    # dest2.price = 650
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = 'Rajshahi'
    # dest3.dis = "Famous for mango"
    # dest3.price = 550
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = True
    #
    # dest4 = Destination()
    # dest4.name = 'Chittagong'
    # dest4.dis = "Famous for shipping and importing"
    # dest4.price = 760
    # dest4.img = 'destination_4.jpg'
    # dest4.offer = False
    #
    # dests = [dest1, dest2, dest3, dest4]

    dest = Destination.objects.all()
    blog = News_blog.objects.all()

    return render(request, 'index.html', {'dest': dest, 'blog': blog})



