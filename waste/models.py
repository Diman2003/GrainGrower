from django.db import models
from App_Login.models import User,Profile
# Create your models here.

class Waste(models.Model):
    title = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_sender')
    location = models.TextField(max_length=300)
    pincode = models.CharField(max_length=6)
    image = models.ImageField(upload_to='waste/')
    caption = models.TextField(max_length=300)
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-post_date']