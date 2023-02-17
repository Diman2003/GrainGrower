from django import forms 
from Organic_Product.models import Comment,Product



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('comment',)