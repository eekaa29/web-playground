from django.urls import path
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path("", ProfileListView.as_view(), name="profile_list"),
    path("<username>/", ProfileDetailView.as_view(), name="profile_detail"),
]