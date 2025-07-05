#frontend
from django.urls import path
from website.views import *

urlpatterns = [
  path('', view=homepage, name='homepage'),
]