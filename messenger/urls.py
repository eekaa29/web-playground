from django.urls import path
from .views import ThreadDetailView, ThreadListView, add_message, start_thread


urlpatterns = [
    path("", ThreadListView.as_view(), name="thread_list"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="thread_detail"),
    path("thread/<int:pk>/add/", add_message, name="add_message"),
    path("thread/start/<username>", start_thread, name="start"),
]