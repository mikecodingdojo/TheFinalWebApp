from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('process_message', views.process_message),
    path('add_comment/<int:id>', views.post_comment),
    path('user_dashboard', views.dashboard),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.delete_comment),
    path('edit/<int:id>', views.edit),
    path('mdelete/<int:id>', views.delete_message), 
    path('linklogin', views.linklogin),
    path('regpage', views.regpage),
    
    path('add-images',views.add_images),
    path('largerpicture', views.largerpicture), 
    path('dashpost', views.dashpost),
    path('photodel/<int:id>', views.photodel), 
    
    
    
    
    
    
]