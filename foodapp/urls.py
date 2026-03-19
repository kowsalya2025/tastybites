from django.urls import path
from . import views
 
urlpatterns = [
    path('',          views.home,        name='home'),
     path("search/", views.search, name="search"),
    path('blogs/',    views.blogs,       name='blogs'),
    path('recipes/',  views.recipes,     name='recipes'),
    path('write/',    views.write,       name='write'),
    path('search/',   views.search,      name='search'),
    path('account/', views.account_view, name='account'),
    path('logout/',   views.logout_view, name='logout'),
    path('profile/',  views.profile,     name='profile'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('write/', views.write, name='write_blog'),
    path('create-blog/', views.create_blog, name='create_blog'),
]