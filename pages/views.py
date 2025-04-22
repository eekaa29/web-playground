from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Page
from django.urls import reverse, reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect


class StaffRequiredMixin(object):#Necesito reforzar las brechas de seguridad, de esta manera configuro que si el usuario no es parte del staff no pueda realizar acciones específicas sin antes registrarse.
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
class PageListView(ListView):
    template_name = "pages/pages.html"
    model= Page

class PageDetailView(DetailView):
    template_name = "pages/page.html"
    model = Page

@method_decorator(staff_member_required, name="dispatch")
class PageCreate(CreateView):#Le pongo la clase creada anteriormente primero para que tenga prioridad sobre --CreateView--
    template_name = "pages/page_create.html"
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("pages:pages")

    
@method_decorator(staff_member_required, name="dispatch")
class PageUpdate(UpdateView):
    form_class=PageForm
    model = Page
    template_name_suffix  = "_update_form"
    #En caso de quere mandarlo directamente a la vista donde aparecen todas las páginas=>success_url = reverse_lazy("pages:pages")
    #Pero voy a hacerlo un poco más currado, voy a enseñar como queda el propio formulario editado, y luego dar posibilidad de ver la página ya editada en page.html

    def get_success_url(self):
        return reverse_lazy("pages:update", args=[self.object.id]) + "?ok"
    

@method_decorator(staff_member_required, name="dispatch")
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")
    