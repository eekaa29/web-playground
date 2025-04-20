from django.urls import path
from .views import HomePage, SamplePage

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('sample/', SamplePage.as_view(), name="sample"),
]