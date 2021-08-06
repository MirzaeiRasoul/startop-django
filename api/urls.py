from django.urls import path
from . import views

urlpatterns = [
    path('startops/', views.startop_list),
    path('startops/<int:pk>/', views.startop_detail),
]
