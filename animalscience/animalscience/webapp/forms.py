from django import forms

from animalscience.webapp.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('project_title', 'author','description')