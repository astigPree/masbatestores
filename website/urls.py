#frontend
from django.urls import path
from website.views import *

urlpatterns = [
  path('', view=home_page, name='homepage'),
]