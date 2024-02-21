from django.urls import path
from . import views

app_name = 'addusers'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:user_id>/', views.delete, name='delete'),
]