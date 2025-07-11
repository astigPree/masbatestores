#frontend
from django.urls import path
from website.views import *

urlpatterns = [
  path('', view=home_page, name='homepage'),
  path('merchant-login/', view=merchant_login, name='merchantlogin'),
  path('merchant-page/', view=merchant_page, name='merchantpage')
]