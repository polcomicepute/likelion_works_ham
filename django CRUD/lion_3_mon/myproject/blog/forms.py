from django import forms
from .models import Blog

class BlogUpdate(forms.ModelForm):
    class Meta: #정보답기
        model = Blog
        fields = ['title', 'body']