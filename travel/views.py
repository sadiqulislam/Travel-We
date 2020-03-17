from django.shortcuts import render
from .models import Destination


# Create your views here.


def index(req):
    dest1 = Destination()

    dest1.name = "Cox's Bazar"
    dest1.desc = "Cox's Bazar Is The Largest Sea-Beach In The World"
    dest1.img = 'destination_1.jpg'
    dest1.price = "5000"
    dest1.offer = True

    dest2 = Destination()

    dest2.name = "Saint Martin"
    dest2.desc = "The Only Coral Island In Bangladesh"
    dest2.img = 'destination_2.jpg'
    dest2.price = "5500"
    dest2.offer = True

    dest3 = Destination()

    dest3.name = "Rangamati"
    dest3.desc = "City Of Mountain"
    dest3.img = 'destination_3.jpg'
    dest3.price = "4500"
    dest3.offer = False

    dest4 = Destination()

    dest4.name = "Sajek Valley"
    dest4.desc = "City Of Cloud"
    dest4.img = 'destination_4.jpg'
    dest4.price = "6000"
    dest4.offer = False

    dest5 = Destination()

    dest5.name = "Sylhet"
    dest5.desc = "City Of Love"
    dest5.img = 'destination_5.jpg'
    dest5.price = "3500"
    dest5.offer = False

    dest6 = Destination()

    dest6.name = "Foy's Lake"
    dest6.desc = "Place Of Enjoy"
    dest6.img = 'destination_6.jpg'
    dest6.price = "6000"
    dest6.offer = True

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    return render(req, 'index.html', {'dests': dests})
