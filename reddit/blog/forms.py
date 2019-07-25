from django import forms

from .models import Post,Feed
from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'post-title',
                'placeholder': 'The title',
            }),
            'text': forms.TextInput(attrs={
                'id': 'post-text',
                'placeholder': 'The text'
            }),
        }


class FeedForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ('name', 'feedback', 'email',)
