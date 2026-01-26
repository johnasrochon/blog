from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

class MessageBoardView(ListView):
    model = Post
    template_name = "posts/message_board.html"

class PostDraftListView(ListView):
    model = Post
    template_name = "posts/post_draft_list.html"

    def get_queryset(self):
        return Post.objects.filter(status=Post.DRAFT)


class PostArchivedListView(ListView):
    model = Post
    template_name = "posts/post_archived_list.html"

    def get_queryset(self):
        return Post.objects.filter(status=Post.ARCHIVED)
