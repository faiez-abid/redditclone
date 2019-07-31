from crispy_forms.layout import Submit, Button
from django import forms
from crispy_forms.helper import FormHelper
from .models import Post
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


class FeedForm(forms.Form):

    name = forms.CharField(max_length=100)
    feedback = forms.CharField(max_length=100, widget=forms.Textarea)
    email = forms.EmailField()



    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["softcatalyst.com"]
        if domain not in domain_list:
            raise forms.ValidationError("Email is invalid. The email should be a softcatalyst email")
        return data
