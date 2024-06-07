from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Yangiliklar


class IndexView(ListView):
    template_name = 'index.html'
    model = Yangiliklar
    context_object_name = 'news'

    def get_queryset(self):
        queryset = Yangiliklar.objects.all()
        return queryset

class AboutView(TemplateView):
    template_name = 'about.html'


class QabulView(TemplateView):
    template_name = 'qabul.html'


class YonalishView(TemplateView):
    template_name = 'yonalishlar.html'


class RahbariyatView(TemplateView):
    template_name = 'rahbariyat.html'


class NewsView(ListView):
    template_name = 'yangiliklar.html'
    model =Yangiliklar
    paginate_by = 12
    context_object_name='news'


class NewsDetailView(DetailView):
    template_name = 'yangiliklar_detail.html'
    model =Yangiliklar

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        news = Yangiliklar.objects.all()[:4]
        context['news'] = news
        return context