from django import forms
from .models import Post

class PostForm(forms.ModelForm):

  title = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "Your title"}))
  text = forms.CharField(
                      required=False, 
                      widget=forms.Textarea(
                              attrs={
                                  "placeholder": "Your post content",
                                  "class": "new-class-name two",
                                  "id": "my-id-for-textarea",
                                  "rows": 20,
                                  'cols': 120
                              }
                          )
                      )

  # Notes to ask
  # Class in form, whats that all about?
  # Why do we claim id in attrs
  # Wait what are attrs in general
  # widget too, whats going on there? 
  # Widget is probably a good place to look
    class Meta:
        model = Post
        fields = ('title', 'text',)