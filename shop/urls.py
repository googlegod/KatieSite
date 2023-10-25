from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('cups/', views.cups, name='cups'),
    path('decorations/', views.decorations, name='decorations'),
]
