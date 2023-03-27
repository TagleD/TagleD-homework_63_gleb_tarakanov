from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView

from posts.forms import PostForm
from posts.models import Post


class IndexView(ListView):
    template_name = 'posts.html'

    context_object_name = 'posts'
    model = Post
    ordering = ['-updated_at']

    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)
    #
    # def get_search_form(self):
    #     return SearchForm(self.request.GET)
    #
    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset().exclude(is_deleted=True)
    #     if self.search_value:
    #         query = Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value)
    #         queryset = queryset.filter(query)
    #     return queryset
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context

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

