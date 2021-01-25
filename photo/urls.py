from django.urls import path

from . import views


urlpatterns = [
    path('cadastro/', views.PhotoFormCreateView.as_view(), name='photo_cadastro'),
    path('<str:username>/delete/<int:photo_id>/', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('<str:username>/update/<int:photo_id>/', views.PhotoUpdateView.as_view(), name='photo_update'),
]   