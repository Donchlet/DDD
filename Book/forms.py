from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'