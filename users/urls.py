from django.urls import path
from .views import LoginRegisterView, ProfileView, logoutView

urlpatterns = [
    path('signing/', LoginRegisterView.as_view(), name='signing'),
    path('logout/', logoutView, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]