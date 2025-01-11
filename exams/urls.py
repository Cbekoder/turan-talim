from django.urls import path

from .views import *


urlpatterns = [
    path('direction/<int:direction>', ExamListView.as_view(), name='direction-detail'),
    path('detail/<int:exam_id>', ExamDetailView.as_view(), name='exam-detail'),
    path('test/<int:exam_id>', ExamTestView.as_view(), name='exam-test'),
]