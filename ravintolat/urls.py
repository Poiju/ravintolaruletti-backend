from django.urls import path
from ravintolat import views

urlpatterns = [
    path('ravintolat/', views.RavintolaList.as_view()),
    path('ravintolat/<int:pk>/', views.RavintolaDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]