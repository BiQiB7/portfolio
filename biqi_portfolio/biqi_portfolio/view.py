# views.py
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import render, redirect

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'home.html'
        
        # C://Users/User/web/biqi_portfolio/
        return render(request, template_name)
