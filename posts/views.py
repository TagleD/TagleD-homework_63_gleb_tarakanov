from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from posts.forms import PostForm
from posts.models import Post


class IndexView(ListView):
    template_name = 'posts.html'

    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        if self.request.user.is_authenticated:
            posts = Post.objects.filter(author__in=self.request.user.subscriptions.all()).order_by('created_at')
            if posts:
                return posts
            else:
                return Post.objects.all().order_by('created_at').exclude(author=self.request.user)
        else:
            return Post.objects.all().order_by('created_at').exclude(author=self.request.user)


class CreatePostView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostForm
    success_message = 'Пост создан'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        user = get_user_model()
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('index')
