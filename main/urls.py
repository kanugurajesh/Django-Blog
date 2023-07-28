from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('create-post', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('news', views.index, name='index'),
    path('details',views.news_details,name='news_details'),
]