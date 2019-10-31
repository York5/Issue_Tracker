from django.urls import path
from accounts.views import login_view, logout_view, register_view, UserDetailView, UserChangeView,\
    UserChangePasswordView, UserIndexView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/update', UserChangeView.as_view(), name='user_update'),
    path('<int:pk>/password_change', UserChangePasswordView.as_view(), name='user_change_password'),
    path('users', UserIndexView.as_view(), name='user_index'),
]

app_name = 'accounts'
