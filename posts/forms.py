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