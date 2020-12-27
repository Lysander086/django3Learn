from .views import CurrentUserAPIView

from django.urls import path



urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name='current-user')
]
