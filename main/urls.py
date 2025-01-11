from django.urls import path
from .views import HomeView, ExamsView, send_to_ai, MultilevelListView, MultilevelDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('exams/', ExamsView.as_view(), name='exams'),
    path('multilevel/', MultilevelListView.as_view(), name='multilevel-list'),
    path('multilevel/detail/<int:pk>', MultilevelDetailView.as_view(), name='multilevel-list'),
    path('send-to-ai/', send_to_ai, name='send_to_ai'),
]