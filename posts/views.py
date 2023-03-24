from django.views.generic import ListView

from posts.models import Post


class IndexView(ListView):
    template_name = 'posts.html'

    context_object_name = 'posts'
    model = Post
    ordering = ['-updated_at']

    # def get_context_data(self, **kwargs):
    #     kwargs['user'] = self.get_profile_form()
    #     return super().get_context_data(**kwargs)

    # paginate_by = 9
    # paginate_orphans = 1

    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=None, **kwargs)
    #     context['form'] = self.form
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset().exclude(is_deleted=True)
    #     if self.search_value:
    #         query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
    #         queryset = queryset.filter(query)
    #     return queryset
    #
    # def get_search_form(self):
    #     return SimpleSearchForm(self.request.GET)
    #
    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None

