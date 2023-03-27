from django.urls import path

from posts.views import IndexView, CreatePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/add', CreatePostView.as_view(), name='post_add')
]
