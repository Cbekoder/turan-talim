from django.urls import path
from .views import HomeView, ExamsView, send_to_ai

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('exams/', ExamsView.as_view(), name='exams'),
    path('send-to-ai/', send_to_ai, name='send_to_ai'),
]