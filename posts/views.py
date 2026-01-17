from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

class MessageBoardView(ListView):
    model = Post
    template_name = "posts/message_board.html"
