from django import forms
from django.forms import TextInput

from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'description')
        labels = {
            'image': 'Картинка',
            'description': 'Описание'
        }

# class SearchForm(forms.Form):
    # search = forms.CharField(max_length=40, required=False, label='Найти')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': TextInput(attrs={'placeholder': 'Добавьте комментарий...'})
        }
