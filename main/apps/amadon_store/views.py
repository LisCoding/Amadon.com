from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request,'amadon_store/index.html')
def process(request):
    price = {
        "1" : 19.99,
        "2" : 29.99,
        "3" : 4.99,
        "4" : 49.99,
    }
    quantity = request.POST['quantity']
    product = request.POST['product_id']
    request.session["total_price"] = int(quantity)* price[product]

    if "total_purchase" not in request.session:
        request.session["total_purchase"] = request.session["total_price"]
        request.session["item"] = int(quantity)
    else:
        request.session["total_purchase"] += request.session["total_price"]
        request.session["item"] += int(quantity)
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon_store/checkout.html')

def back(request):
    return redirect('/amadon')
