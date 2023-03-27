from django import forms

from posts.models import Post


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