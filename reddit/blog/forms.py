from django import forms

from .models import Post,Feed

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class FeedForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ('name', 'feedback', 'email',)
