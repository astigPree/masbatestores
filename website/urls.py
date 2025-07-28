from django.urls import path
from website.views import *

urlpatterns = [ 
    path('', homepage, name='homepage'),
    
    # ============== MERCHANT PAGE ================
    path('merchant_login/', view=merchant_login, name='merchant_login'),
    path('merchant_page/', view=merchant_page, name='merchant_page'),
    path('merchant_review/', view=merchant_review, name='merchant_review'),
    # ============== USER PAGE ================
    path('user_login/', user_login_page, name='user_login_page'),
    path('user_register/', user_register_page, name='user_register_page'),
    path('user_profile/', user_profile_page, name='user_profile_page'),
    path('user_settings/', user_settings_page, name='user_settings_page'),
    path('user_settings_update_username/', user_settings_update_username_page, name='user_settings_update_username_page'),
    path('user_settings_update_security/', user_settings_update_security_page, name='user_settings_update_security_page'),
    path('user_favorites_stores/', user_fav_stores_page, name='user_favorites_stores_page'),
    path('user_shopping_list/', user_shopping_list_page, name='user_shopping_list_page'),
    # ============== USER PAGE ================
    path('user_login/', user_login_page, name='user_login_page'),
    path('user_register/', user_register_page, name='user_register_page'),
    path('user_profile/', user_profile_page, name='user_profile_page'),
    path('user_settings/', user_settings_page, name='user_settings_page'),
    path('user_settings_update_username/', user_settings_update_username_page, name='user_settings_update_username_page'),
    path('user_settings_update_security/', user_settings_update_security_page, name='user_settings_update_security_page'),
    path('user_favorites_stores/', user_fav_stores_page, name='user_favorites_stores_page'),
    path('user_shopping_list/', user_shopping_list_page, name='user_shopping_list_page'),
    path('user_calculator/', user_calculator_page, name='user_calculator_page'),
    path('user_map/', user_map_page, name='user_map_page'),
    
    # ============== TINDAHAN PAGE ===============
    path('store_login/', store_login_page, name='store_login_page'),
    path('store_register/', store_register_page, name='store_register_page'),
    path('store_profile/', store_profile_page, name='store_profile_page'),
]
