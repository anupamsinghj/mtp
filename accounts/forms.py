from django import forms
from .models import Book, uploadf

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'csv')

class uploadfForm(forms.ModelForm):
    class Meta:
        model = uploadf
        fields = ('title','csv')
