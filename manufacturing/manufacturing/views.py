from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'home.html'
