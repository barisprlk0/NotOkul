from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import  TemplateView
from .models import Clup
#Create your views here.

class ClupChartView(TemplateView):
    template_name = 'sorucoz/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Clup.objects.all()
        return context
