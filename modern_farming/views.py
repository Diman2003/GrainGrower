from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import get_object_or_404
                              
from App_Login.models import User,Profile

from django.urls import reverse, reverse_lazy
from .models import ModernFarming
from django.views.generic import CreateView,UpdateView,ListView,DetailView,TemplateView,DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class FarmingTech(LoginRequiredMixin,ListView):
    context_object_name = 'modern_farming'
    model = ModernFarming
    template_name = 'modern_farming/farming_technique.html'
    
    
class FarmingTechDetail(LoginRequiredMixin,DetailView):
    context_object_name = 'tech_detail'
    model = ModernFarming
    template_name = 'modern_farming/technique_detail.html'
