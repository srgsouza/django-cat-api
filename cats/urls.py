from django.urls import path
from . import views

urlpatterns = [
  path('api/cats/', views.CatList.as_view(), name='cat-list'),
  path('api/cats/<int:pk>', views.CatDetail.as_view(), name='cat-detail'),
]
