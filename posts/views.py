from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Q
from django.shortcuts import redirect, get_object_or_404
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
            if not posts:
                posts = posts.exclude(author=self.request.user)
            return posts.annotate(
                is_liked=Count(
                    'user_likes',
                    filter=Q(user_likes=self.request.user),
                    distinct=True
                ),
                likes_number=Count(
                    'user_likes',
                    distinct=True
                )
            )
        else:
            return Post.objects.all().order_by('created_at').exclude(author=self.request.user).annotate(
                likes_number=Count(
                    'user_likes',
                    distinct=True
                )
            )


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


def like_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        request.user.liked_posts.add(post)
        return redirect('index')
    return redirect('login')


def unlike_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        request.user.liked_posts.remove(post)
        return redirect('index')
    return redirect('login')
