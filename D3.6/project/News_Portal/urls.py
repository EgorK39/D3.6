from django.urls import path
from .views import News, New

urlpatterns = [
    path('', News.as_view()),
    path('<int:pk>', New.as_view()),
]
