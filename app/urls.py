from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('display/', views.display), # aqui usar /<int:id>
    path('edit/', views.edit), # aqui usar /<int:id>
    path('delete/', views.delete), # aqui usar /<int:id>
    path('other/', views.other), # aqui usar /<int:id>


    path('registro/', views.registro),
    path('login/', views.login), 
    path('logout/', views.logout),
    
]
