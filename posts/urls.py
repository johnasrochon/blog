from django.urls import path
from .views import (
    MessageBoardView,
    PostDraftListView,
    PostArchivedListView
)

urlpatterns = [
    path("", MessageBoardView.as_view(), name="message_board"),
    path("drafts/", PostDraftListView.as_view(), name="post_drafts"),
    path("archived/", PostArchivedListView.as_view(), name="post_archived"),
]
