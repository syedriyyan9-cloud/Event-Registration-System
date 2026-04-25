from django.urls import path
from . import views
app_name = 'events'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('<int:pk>/edit', views.edit_event, name='edit_event'),
]