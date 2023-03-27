from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, subscribe_on_account, \
    unsubscribe_on_account

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
    path('profile/<int:pk>/subscribe', subscribe_on_account, name='subscribe'),
    path('profile/<int:pk>/unsubscribe', unsubscribe_on_account, name='unsubscribe'),
]

