from crispy_forms.layout import Submit, Button
from django import forms
from crispy_forms.helper import FormHelper
from .models import Post,Feed
from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False
    helper.form_class = "post-form"
    helper.add_input(Submit('submit', 'Save'))

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
