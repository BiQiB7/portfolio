from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import render, redirect
# Create your views here.
class Art3DView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'art3D.html'
        return render(request, template_name)