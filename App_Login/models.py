from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy

# Automatic create One To One objects
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class MyUserManager(BaseUserManager):
    
    def _create_user(self,email,password,**extra_fields):
        
        if not email:
            raise ValueError("The email must be set !!")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email,password,**extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True,null=False)
    is_staff = models.BooleanField(
        gettext_lazy('Staff Status'),default=False,
        help_text=gettext_lazy('Designate whether the user can log in the site')
    )
    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=gettext_lazy('Designate whether this user should be treatea as active')
    )
    USERNAME_FIELD = 'email'
    object = MyUserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username = models.CharField(max_length=264,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    type=(
        ('FARMER','FARMER'),
        ('AGRONOMISTS','AGRONOMISTS'),
        ('FOR_WASTE','FOR_WASTE'),
        ('SELLER','SELLER')
    )
    user_type = models.CharField(max_length=40,choices=type,default='FARMER')
    full_name = models.CharField(max_length=264,blank=True)
    address_1 = models.TextField(max_length=350,blank=True)
    city = models.CharField(max_length=40,blank=True)
    zipcode = models.CharField(max_length=8,blank=True)
    country = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.username + "'S Profile"
    
    def is_fully_filled(self):
        fields_name = [f.name for f in self._meta.get_fields()]
        
        for field_name in fields_name:
            value = getattr(self,field_name)
            if value is None or value == '':
                return False
            
        return True
    
    @receiver(post_save,sender = User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user = instance)
            
            
    @receiver(post_save,sender=User)
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()
        


class slider(models.Model):
    title = models.CharField(max_length = 100,blank=False)
    description = models.TextField(max_length=800,blank = False)
    image = models.ImageField(upload_to = 'slider',blank = False)

    def __str__(self):
        return self.title        