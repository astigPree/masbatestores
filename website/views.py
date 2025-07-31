from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home/index.html')


# =============== MERCHANT PAGE ================

def merchant_login(request):
    return render(request, 'merchant_login/index.html')

def merchant_page(request):
    return render(request, 'merchant_page/index.html')

def merchant_review(request):
    return render(request, 'merchant_review/index.html')

def merchant_product(request):
    return render(request, 'merchant_product/index.html')

# =============== USER PAGE ================
def user_login_page(request):
    return render(request, 'user_login/index.html')

def user_profile_page(request):
    return render(request, 'user_profile/index.html')

def user_register_page(request):
    return render(request, 'user_register/index.html')

def user_settings_page(request):
    return render(request, 'user_settings/index.html')


def user_settings_update_username_page(request):
    return render(request, 'user_settings_update_username/index.html')

def user_settings_update_security_page(request):
    return render(request, 'user_settings_update_security/index.html')


def user_fav_stores_page(request):
    return render(request, 'user_fav_stores/index.html')


def user_shopping_list_page(request):
    return render(request, 'user_shopping_list/index.html')


def user_calculator_page(request):
    return render(request, 'user_calculator/index.html')

def user_map_page(request):
    return render(request, 'user_map/index.html')




# =============== TINDAHAN PAGE ================
def store_login_page(request):
    return render(request, 'store_login/index.html')

def store_register_page(request):
    return render(request, 'store_register/index.html')


def store_profile_page(request):
    return render(request, 'store_profile/index.html')

