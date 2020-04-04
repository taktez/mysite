from django.urls import path
from . import views

app_name = 'app_accounts'

urlpatterns = [
    path('', views.profile, name='profile'),
]
