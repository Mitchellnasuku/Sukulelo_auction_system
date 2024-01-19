'''from django.contrib import admin  
from django.urls import path  
from . import views  

urlpatterns = [  
    path('admin/', admin.site.urls),

    
    #urls in use:
    # path('main', views.main, name='main'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_user', views.create_user, name='create_user'),
    path('view_user/<int:id>', views.view_user, name='view_user'), 
    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),  
    path('create_item', views.create_item, name='create_item'), 
    path('update_item/<int:id>', views.update_item, name='update_item'), 
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),  
    path('create_bid', views.create_bid, name='create_bid'), 
    path('update_bid/<int:id>', views.update_bid, name='update_bid'), 
    path('delete_bid/<int:id>', views.delete_bid, name='delete_bid'),  
    path('make_payment/<int:id>', views.make_payment, name='make_payment'),  
]  


'''

from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

    
    # Your custom URL patterns go here
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_user/', views.create_user, name='create_user'),
    path('view_user/<int:id>/', views.view_user, name='view_user'), 
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),  
    path('create_item/', views.create_item, name='create_item'), 
    path('update_item/<int:id>/', views.update_item, name='update_item'), 
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),  
    path('create_bid/', views.create_bid, name='create_bid'), 
    path('update_bid/<int:id>/', views.update_bid, name='update_bid'), 
    path('delete_bid/<int:id>/', views.delete_bid, name='delete_bid'),  
    path('make_payment/<int:id>/', views.make_payment, name='make_payment'),  
    
    path('custom-login-redirect/', views.custom_login_redirect, name='custom_login_redirect'),
]

