from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "home/index.html")

def merchant_login(request):
    return render(request, "merchant-login/index.html")

def merchant_page(request):
    return render(request, "merchant-page/index.html")