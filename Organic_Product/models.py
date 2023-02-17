from django.db import models
from App_Login.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"
        
        
class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller',null=True)
    mainimage= models.ImageField(upload_to='Product',verbose_name='Product Image')
    name = models.CharField(max_length=264)
    crop_name = models.CharField(max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    preview_text = models.TextField(max_length=200,verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000,verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created',]
        
        
        
class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment = models.TextField(max_length=1000)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-comment_date'] 
    
    def __str__(self):
        return self.comment