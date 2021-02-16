from django.urls import path
from .views import JoinView, LoginView, logout

app_name = 'User'

urlpatterns =[
    path('signup', JoinView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout, name='logout'),
]