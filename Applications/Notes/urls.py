from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerNote/', views.registerNote),
    path('editNote/<title>', views.editNote),
    path('editingNote/', views.editingNote),
    path('deleteNote/<title>', views.deleteNote)
]