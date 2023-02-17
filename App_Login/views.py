from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

from App_Login.models import Profile,slider
from waste.models import Waste
from modern_farming.models import ModernFarming
from Organic_Product.models import Product
from App_Login.forms import ProfileForm,SignUpForm
from django.contrib import messages

# Create your views here.


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully!!")
            return HttpResponseRedirect(reverse('App_Login:login'))
        
    return render(request,'App_Login/signup.html',context={'form':form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            
    return render(request,'App_Login/login.html',context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,'You are Logged out')
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully !!!")
            form = ProfileForm(instance=profile)
    return render(request,'App_Login/change_profile.html',context={'form':form})



def Home(request):
    sliderdata = slider.objects.all()
    wastedata = Waste.objects.all()
    productdata = Product.objects.all()
    farmingdata = ModernFarming.objects.all()
    
    context = {
        'slider':sliderdata,
        'waste':wastedata,
        'product':productdata,
        'farmingdata':farmingdata,
    }
    
    return render(request,'base.html',context)


@login_required
def profile(request):
    
    return render(request,'App_Login/profile.html')