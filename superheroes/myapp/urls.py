from . import views
from django.urls import path

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:myapp_id>/', views.detail, name='detail')
]