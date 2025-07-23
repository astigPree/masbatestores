from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home/index.html')







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
