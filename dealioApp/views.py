from django.shortcuts import render
from dealioApp.models import Restaurant
from dealioApp.models import Promotion
from django.views.generic.edit import CreateView
# Create your views here.


def index(request):
    return render(request, 'dealioApp/home.html') #render looks in templates directory


def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'dealioApp/restaurants.html', {'restaurants': restaurants}) #render looks in templates directory #can pass in content into render() such as dictionaries


def promotions(request, restaurant_id):#pass in a restaurant's id into this view to access its promotions via getPromotions
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'dealioApp/promotions.html', {'restaurant': restaurant})

<<<<<<< HEAD
def ownerLogin(request):
    return render(request, 'dealioApp/ownerLogin.html')
=======

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['name', 'proms', 'category', 'review_link']

class PromotionCreate(CreateView):
    model = Promotion
    fields = ['title', 'description', 'rating']

def gAPIComplete(request):
    return render(request, 'dealioApp/gAPIComplete.html')
>>>>>>> a2a5da3e4e807ca9b7a462472f553bcbb27da005
