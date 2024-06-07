from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('qabul', views.QabulView.as_view(), name='qabul'),
    path('yonalishlar', views.YonalishView.as_view(), name='yonalishlar'),
    path('rahbariyat', views.RahbariyatView.as_view(), name='rahbariyat'),
    path('yangiliklar', views.NewsView.as_view(), name='news'),
    path('yangiliklar/<int:pk>/', views.NewsDetailView.as_view(), name='new_detail'),
]
