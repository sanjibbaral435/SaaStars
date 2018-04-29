from django import forms

# from animalscience.webapp.models import Post

class PostForm(forms.Form):
    title = forms.CharField(label="Article Title",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Article Title'}),required = False)
    year = forms.CharField(label="Year of Publication",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Year of Publication'}),required = False)
    author = forms.CharField(label="Author Name",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Author Name'}),required = False)
    keyword = forms.CharField(label="Keywords",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Keywords'}),required = False)