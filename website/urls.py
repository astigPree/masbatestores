from django.urls import path
from website.views import *

urlpatterns = [ 
    path('', homepage, name='homepage'),
    
    # ============== MERCHANT PAGE ================
    path('merchant_login/', view=merchant_login, name='merchant_login'),
    path('merchant_page/', view=merchant_page, name='merchant_page'),

    # ============== USER PAGE ================
    path('user_login/', user_login_page, name='user_login_page'),
    path('user_register/', user_register_page, name='user_register_page'),
    path('user_profile/', user_profile_page, name='user_profile_page'),
    path('user_settings/', user_settings_page, name='user_settings_page'),
    path('user_settings_update_username/', user_settings_update_username_page, name='user_settings_update_username_page'),
    path('user_settings_update_security/', user_settings_update_security_page, name='user_settings_update_security_page'),
    path('user_favorites_stores/', user_fav_stores_page, name='user_favorites_stores_page'),
    path('user_shopping_list/', user_shopping_list_page, name='user_shopping_list_page'),

]
