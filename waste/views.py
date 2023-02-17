from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import get_object_or_404
                              
from App_Login.models import User,Profile
from .forms import WasteForm
from django.urls import reverse, reverse_lazy
from .models import Waste
from django.views.generic import CreateView,UpdateView,ListView,DetailView,TemplateView,DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class WastePost(LoginRequiredMixin,CreateView):
    model = Waste
    template_name = 'waste/waste.html'
    fields = ('title','location','pincode','image','caption',)
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
 
        obj.save()
        messages.success(self.request,"Waste Posted Successfully !!!")
        return HttpResponseRedirect(reverse('home'))
    
    
class WasteList(ListView):
    context_object_name = 'waste'
    model = Waste
    template_name = 'waste/waste_list.html'
    
    
class MyWaste(LoginRequiredMixin,TemplateView):
    template_name = 'waste/my_waste.html'
    
class WasteDelete(LoginRequiredMixin,DeleteView):
    model = Waste
    success_url ="/"
    template_name = 'waste/delete_waste.html'
    
class WasteDetail(LoginRequiredMixin,DetailView):
    model = Waste
    template_name = 'waste/detail_waste.html'