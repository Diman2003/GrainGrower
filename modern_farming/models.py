from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Category(models.Model):
    crop_type = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.crop_type
    
    class Meta:
        verbose_name_plural = "Categories"


class ModernFarming(models.Model):
    tech_name = models.CharField(max_length=100)
    video = models.FileField(upload_to='modern_farming/',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    process = models.TextField(max_length=2000)
    required_tool = models.TextField(max_length=500)
    soil_report = models.TextField(max_length=500)
    season = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tech_name
    
    class Meta:
        ordering = ['-created',]
    