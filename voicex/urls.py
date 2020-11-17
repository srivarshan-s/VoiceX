from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='voicex-home'),
    path('text_editor/', views.text_editor, name='voicex-text_editor'),
    path('recommend/', views.recommend, name='voicex-recommend'),
]
