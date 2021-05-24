from django.urls import path
from django.urls.conf import include
from .views import home_page,create_expenses,update_expenses,rem_expenses


urlpatterns = [
    path('', home_page,name="home-page"),
    path('create_expenses/', create_expenses,name="create-page"),
    path('update_expenses/<int:pk>/', update_expenses,name="update-page"),
    path('delete_expenses/<int:pk>/', rem_expenses,name="delete-page"),
    
]