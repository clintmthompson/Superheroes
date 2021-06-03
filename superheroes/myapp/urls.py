from . import views
from django.urls import path

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:myapp_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_hero'),
    path('delete/<int:myapp_id>/', views.delete, name='delete'),
]
