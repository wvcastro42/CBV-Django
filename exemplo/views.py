from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from exemplo.models import Cliente


class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')


class ClienteDetail(DetailView):
    queryset = Cliente.objects.all()


class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('exemplo:list')
