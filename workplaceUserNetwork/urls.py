from django.urls import path
from . import views

app_name = 'workplaceUserNetwork'

urlpatterns = [
    # Home (Index) page
    path('', views.index, name='index'),

    # Add new workplace user network
    path('create/', views.create, name='create'),

    # Edit workplace user network
    path('edit/<int:id>/', views.edit, name='edit'),

    # Delete workplace user network
    path('delete/<int:id>/', views.delete, name='delete'),
    
    path('update/<int:id>/', views.update, name='update'),

    # Detail page for a specific workplace user network
    path('detail/<int:id>/', views.detail, name='detail'),
]