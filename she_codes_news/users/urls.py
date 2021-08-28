from django.urls import path
from .views import CreateAccountView
from .views import UserProfile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),

]

#urlpatterns = [
 #   path('User-Profile/', UserProfile.as_view(), #latest error HERE
#name='User Profile'),
#]