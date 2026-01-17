from django.urls import path
from .views import MessageBoardView

urlpatterns = [
    path("", MessageBoardView.as_view(), name="message_board"),
]
