from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["text", "status"]
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = ["text", "status"]
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

