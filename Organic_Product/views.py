from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView,DeleteView,DetailView,CreateView
from Organic_Product.models import Product,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from Organic_Product.forms import CommentForm
# Create your views here.

class Products(ListView):
    model = Product
    template_name = 'Organic_Product/Products.html'
    
    
class ProductDetail(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'Organic_Product/product_detail.html'
    
    
                
    
    

class SellProduct(LoginRequiredMixin,CreateView):
    model = Product
    template_name = 'Organic_Product/sell_product.html'
    fields = ('mainimage','name','crop_name','category','preview_text','detail_text','price','old_price',)
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.seller = self.request.user
 
        obj.save()
        messages.success(self.request,"Product Posted Successfully !!!")
        return HttpResponseRedirect(reverse('home'))
    
def comment(request,pk):
        product = Product.objects.get(pk=pk)
        comment_form = CommentForm()
        
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.product = product
                comment.save(commit=True)
                    
        return render(request,'Organic_Product/product_detail.html',context={'comment_form':comment_form})