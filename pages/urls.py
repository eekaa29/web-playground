from django.urls import path
from .views import PageListView, PageDetailView

urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),#IMPORTANTE, el atributo que ahora se llama pk, antes se llamaba --page_id--, pero lo tengo que cambiar ya que al usar los Class Base View, solo acepta que el parametro se llame --pk-- (viene de primary key) 
]