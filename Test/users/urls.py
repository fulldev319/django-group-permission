from django.urls import path
from . import views

urlpatterns = [
    path('view1', views.view1),
    path('view2', views.view2)
]
