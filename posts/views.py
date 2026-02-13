from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = "about.html"

from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "body", "status"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

