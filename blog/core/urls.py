from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('blog/<int:id>/',views.blog , name='blog_details'),
    path('update-blog/<int:id>/',views.update,name='update-blog'),
    path('delete-blog/<int:id>',views.delete,name='delete-blog'),
    path('create-blog',views.create,name='create-blog'),
]