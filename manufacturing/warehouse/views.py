from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (FormView, CreateView, UpdateView, DeleteView)
from django.views.generic.list import ListView

from warehouse.forms import (AsmbForm, ProgForm)
from warehouse.models import Task
#-------------------Make views here-------------------------#

class AsmbFormView(LoginRequiredMixin, FormView):
    login_url = '/'
    template_name = 'warehouse/form.html'
    form_class = AsmbForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save(commit=False)
        t= Task(
            versa_sn = form.cleaned_data['versa_sn'],
            task_type = '1',
            starter = self.request.user
        )
        t.save()
        form.instance.task_id = t
        form.save()
        return super(AsmbFormView, self).form_valid(form)


class ProgFormView(LoginRequiredMixin, FormView):
    login_url = '/'
    template_name = 'warehouse/form.html'
    form_class = ProgForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save(commit=False)
        t= Task(
            versa_sn = form.cleaned_data['versa_sn'],
            task_type = '2',
            starter = self.request.user
        )
        t.save()
        form.instance.task_id = t
        form.save()
        return super(ProgFormView, self).form_valid(form)


class ReportView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'report.html'
