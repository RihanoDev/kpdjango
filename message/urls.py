from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]