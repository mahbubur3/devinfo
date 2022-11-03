from django.urls import path

from .import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('account/', views.user_account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),
]
