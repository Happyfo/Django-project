from django.urls import path

from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:portfolio_id>/', views.detail, name='detail'),

]
