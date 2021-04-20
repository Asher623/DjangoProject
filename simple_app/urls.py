from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.registration, name = 'registration'),
    path('login', views.user_login, name = 'user_login'),
    path('create_view', views.create_view, name = 'create_view'),
    path('list_post', views.list_post, name = 'list_post'),
    path('<int:id>/', views.post_detail, name = 'post_detail'),
    path('<int:id>/update', views.post_edit, name = 'post_edit'),
    path('<int:id>/delete', views.post_delete, name = 'post_delete'),
    path('profile', views.profile_info, name = 'profile_info'),
    path('profile_edit', views.profile_edit, name = 'profile_edit'),
    path('<int:id>/users_post_list', views.users_post_list, name = 'users_post_list'),
    path('favourite_list', views.favourite_list, name = 'favourite_list'),
    path('<int:id>/add_favourite_post', views.add_favourite_post, name ='add_favourite_post'),
    path('your_posts', views.your_posts, name = 'your_posts'),
    path('<int:id>/likes_post', views.likes_post, name = 'likes_post'),



]
