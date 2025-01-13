from django.urls import path
from .views import MultilevelListView, MultilevelDetailView, MultilevelTestListeningView, MultilevelTestReadingView, \
    MultilevelTestWritingView

urlpatterns = [
    path('', MultilevelListView.as_view(), name='multilevel-list'),
    path('detail/<int:pk>', MultilevelDetailView.as_view(), name='multilevel-list'),
    path('test/listening/<int:pk>', MultilevelTestListeningView.as_view(), name='multilevel-listening'),
    path('test/reading/<int:pk>', MultilevelTestReadingView.as_view(), name='multilevel-reading'),
    path('test/writing/<int:pk>', MultilevelTestWritingView.as_view(), name='multilevel-writing'),
]