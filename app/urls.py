from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('administrador/', views.administrador), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('postmessage', views.postmessage),
    path('postcomment', views.postcomment),
    path('delete/<int:id>', views.borrar), 
]

""" el id en el delete es el nombre que le puse en views en la línea 39 """