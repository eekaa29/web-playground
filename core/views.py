from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Mi super increíble Web Playground"})

class SamplePage(TemplateView):
    template_name = "core/sample.html"