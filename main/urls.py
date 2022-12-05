from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('portfolio/<int:id>/', views.portfolio_view, name='portfolio-detail'),
]
