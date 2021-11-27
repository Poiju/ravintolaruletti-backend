from django.urls import path
from ravintolat import views

urlpatterns = [
    path('ravintolat/', views.ravintola_list),
    path('ravintolat/<int:pk>/', views.ravintola_detail),
]