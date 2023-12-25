from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import render, redirect
# Create your views here.
class DragonProjectView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'mythical_creature.html'
        return render(request, template_name)